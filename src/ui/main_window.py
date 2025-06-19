from PyQt6.QtWidgets import (
    QMainWindow,
    QPushButton,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QStackedWidget,
    QFrame,
    QSizePolicy,
    QComboBox,
)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize

from src.theme.theme_manager import ThemeManager
from src.ui.categories import Categories
import src.static.config as cfg


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Ana widget oluşturma
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        self.theme_manager = ThemeManager()
        self.theme_manager.apply_theme(dark_mode=cfg.IS_THEME_DARK)

        # Theme selector combo box
        self.themeCombo = QComboBox()
        self.themeCombo.addItems(["Koyu Tema", "Açık Tema"])
        self.themeCombo.setCurrentText("Dark Theme")
        self.themeCombo.currentTextChanged.connect(self.on_theme_changed)

        # Ana düzen oluşturma
        mainLayout = QHBoxLayout(centralWidget)
        mainLayout.setSpacing(0)
        mainLayout.setContentsMargins(0, 0, 0, 0)

        # SOL PANEL - Kategoriler
        self.leftPanel = QFrame()
        self.leftPanel.setObjectName("leftPanel")
        self.leftPanel.setFixedWidth(200)
        leftLayout = QVBoxLayout(self.leftPanel)
        leftLayout.setContentsMargins(0, 0, 0, 0)
        leftLayout.setSpacing(0)

        self.categories = Categories()

        leftLayout.setSpacing(5)  # Butonlar arasındaki boşluk
        # İçerik alanı
        self.contentStack = QStackedWidget()
        self.contentStack.setObjectName("contentStack")

        self.categoryButtons = []
        for text, icon, widget in self.categories.categories_list:
            button = QPushButton(f" {text}")
            button.setIcon(QIcon(f"data/icons/{icon}"))
            button.setIconSize(QSize(24, 24))
            button.setObjectName("categoryButton")
            button.setCheckable(True)

            # Butonun boyut politikasını ayarla
            button.setSizePolicy(
                QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
            )

            button.clicked.connect(
                lambda checked, i=len(self.categoryButtons): self.changeCategory(i)
            )
            leftLayout.addWidget(button)
            self.categoryButtons.append(button)

            self.contentStack.addWidget(widget)

        leftLayout.addWidget(self.themeCombo)

        # SAĞ PANEL - Ana içerik alanı ve butonlar
        rightPanel = QWidget()
        rightLayout = QVBoxLayout(rightPanel)
        rightLayout.setContentsMargins(0, 0, 0, 0)

        # Butonlar paneli
        buttonPanel = QWidget()
        buttonPanel.setFixedHeight(60)
        buttonPanel.setObjectName("buttonPanel")
        buttonLayout = QHBoxLayout(buttonPanel)

        self.prevButton = QPushButton("Önceki")
        self.prevButton.setObjectName("navButton")
        self.prevButton.clicked.connect(self.prevPage)

        self.nextButton = QPushButton("Sonraki")
        self.nextButton.setObjectName("navButton")
        self.nextButton.clicked.connect(self.nextPage)

        buttonLayout.addStretch()
        buttonLayout.addWidget(self.prevButton)
        buttonLayout.addWidget(self.nextButton)

        # Sağ paneldeki widget'ları ekle
        rightLayout.addWidget(self.contentStack, 1)
        rightLayout.addWidget(buttonPanel)

        # Ana düzene panelleri ekle
        mainLayout.addWidget(self.leftPanel)
        mainLayout.addWidget(rightPanel, 1)  # 1 değeri genişleyebilir olduğunu belirtir

        # Pencere ayarları
        self.setWindowTitle("Bismih KDE Karşılayıcı")
        self.setMinimumSize(800, 600)

        # İlk kategoriyi seç
        self.categoryButtons[0].setChecked(True)
        self.changeCategory(0)

    def on_theme_changed(self, theme):
        """Tema değiştiğinde çağrılır."""
        if theme == "Dark Theme":
            cfg.IS_THEME_DARK = True
            self.theme_manager.apply_theme(dark_mode=True)
        else:
            cfg.IS_THEME_DARK = False
            self.theme_manager.apply_theme(dark_mode=False)

        # Temayı uyguladıktan sonra arayüzü yeniden çiz
        self.update()
        for _, _, widget in self.categories.categories_list:
            widget.update()

    def changeCategory(self, index):
        # Tüm butonların seçimini kaldır
        for button in self.categoryButtons:
            if button != self.sender() and isinstance(self.sender(), QPushButton):
                button.setChecked(False)

        # İlgili kategoriyi seç
        if isinstance(self.sender(), QPushButton):
            self.sender().setChecked(True)
        else:
            self.categoryButtons[index].setChecked(True)

        # İçerik sayfasını değiştir
        self.contentStack.setCurrentIndex(index)

        # Gezinme butonlarını güncelle
        self.updateNavigationButtons()

    def prevPage(self):
        currentIndex = self.contentStack.currentIndex()
        if currentIndex > 0:
            self.contentStack.setCurrentIndex(currentIndex - 1)
            self.updateNavigationButtons()

    def nextPage(self):
        currentIndex = self.contentStack.currentIndex()
        if currentIndex < self.contentStack.count() - 1:
            self.contentStack.setCurrentIndex(currentIndex + 1)
            self.updateNavigationButtons()

    def updateNavigationButtons(self):
        currentIndex = self.contentStack.currentIndex()
        self.prevButton.setEnabled(currentIndex > 0)
        self.nextButton.setEnabled(currentIndex < self.contentStack.count() - 1)
        self.categoryButtons[currentIndex].setChecked(True)
        for i, button in enumerate(self.categoryButtons):
            if i != currentIndex:
                button.setChecked(False)
            else:
                button.setChecked(True)
