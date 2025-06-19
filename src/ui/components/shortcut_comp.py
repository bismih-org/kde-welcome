from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QHBoxLayout, QGridLayout, QFrame
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


class ShortcutItem(QHBoxLayout):
    def __init__(self, action: str, shortcut: str):
        super().__init__()
        actionLabel = QLabel(action)
        actionLabel.setStyleSheet("font-size: 12px;")
        shortcutLabel = QLabel(shortcut)
        shortcutLabel.setStyleSheet("font-weight: bold; font-size: 12px; color: #00AAFF;")
        shortcutLabel.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.addWidget(actionLabel)
        self.addStretch()
        self.addWidget(shortcutLabel)


class ShortcutComp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(12)
        layout.setContentsMargins(20, 20, 20, 20)

        # Başlık: Klavye Kısayolları
        title1 = QLabel("⌨️ Klavye Kısayolları")
        title1.setStyleSheet("font-size: 14px; font-weight: bold;")
        layout.addWidget(title1)

        # Klavye kısayolları listesi
        keyboardShortcuts = [
            ("Uygulama Menüsünü Aç", "Super"),
            ("Terminal Aç", "Ctrl + Alt + T"),
            ("Dosya Yöneticisi", "Super + E"),
            ("Ekran Görüntüsü Al", "PrintScreen"),
            ("Masaüstünü Göster", "Ctrl + Alt + D"),
            ("Pencereyi Kapat", "Alt + F4"),
        ]
        for action, keys in keyboardShortcuts:
            layout.addLayout(ShortcutItem(action, keys))

        # Ayırıcı çizgi
        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.HLine)
        separator.setFrameShadow(QFrame.Shadow.Sunken)
        layout.addWidget(separator)

        # Başlık: Dokunmatik Hareketler
        title2 = QLabel("🖐️ Dokunmatik Panel Hareketleri")
        title2.setStyleSheet("font-size: 14px; font-weight: bold;")
        layout.addWidget(title2)

        # Hareket açıklamaları
        gestures = [
            ("Üç Parmak Yukarı", "Pencereyi büyüt"),
            ("Üç Parmak Aşağı", "Tüm pencereleri küçült"),
            ("Üç Parmak Sağa/Sola", "Çalışma alanları arasında geçiş"),
            ("Dört Parmak Yukarı", "Görev görünümünü aç"),
            ("İki Parmak Kaydırma", "Sayfa yukarı/aşağı"),
            ("İki Parmak Yakınlaştırma", "Zoom in/out (destekleyen uygulamalarda)"),
        ]
        for gesture, desc in gestures:
            layout.addLayout(ShortcutItem(desc, gesture))

        self.setLayout(layout)

    def update(self):
        pass
