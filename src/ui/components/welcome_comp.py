from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QCheckBox,
)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt, QSize
from src.ui.widgets.BLabel import BLabel
import src.static.config as cfg
import os


class WelcomeComp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Ana düzen oluşturma
        self.mainLayout = QVBoxLayout(self)
        self.mainLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mainLayout.setContentsMargins(20, 20, 20, 20)
        self.mainLayout.setSpacing(0)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)

        # İkon gösterimi için QLabel oluştur
        self.icon_label = QLabel()
        self.icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mainLayout.addWidget(self.icon_label)

        # Başlık ve açıklama ekle
        self.title = BLabel("kde Linux'a Hoş Geldiniz", 27, is_bold=True)
        self.mainLayout.addWidget(self.title)
        self.mainLayout.addSpacing(20)

        self.description = BLabel(
            "Kullanıcı dostu arayüzü ve güçlü araçlarıyla\n "
            "Linux deneyiminizi zenginleştirir.\n"
            "Başlamak için aşağıdaki kılavuzları takip edin.",
            is_bold=False,
        )
        self.description.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mainLayout.addWidget(self.description)

        self.chkbox_autostart = QCheckBox("Başlangıçta çalıştır")
        self.chkbox_autostart.setChecked(True)
        self.chkbox_autostart.stateChanged.connect(self.on_checkbox_toggled)
        self.mainLayout.addWidget(
            self.chkbox_autostart, alignment=Qt.AlignmentFlag.AlignCenter
        )

        self.setLayout(self.mainLayout)

        # İkonu güncelle
        self.updateWid()

    def on_checkbox_toggled(self, checked):
        """Checkbox durumunu güncelle"""
        if checked:
            os.system(f"cp -rf {cfg.DESKTOP_ROOT_PATH} {cfg.DESKTOP_PATH}")
        else:
            if os.path.exists(cfg.DESKTOP_PATH):
                os.remove(cfg.DESKTOP_PATH)

    def updateWid(self):
        # İkon yolunu temaya göre güncelle
        p = "data/images/kde_icon_"
        icon_path = p + ("dark" if not cfg.IS_THEME_DARK else "light") + ".png"
        print(f"Icon path: {icon_path}")
        icon_pixmap = QIcon(icon_path).pixmap(QSize(256, 256))
        self.icon_label.setPixmap(icon_pixmap)
