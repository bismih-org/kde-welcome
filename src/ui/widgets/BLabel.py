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
)
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt, QSize



class BLabel(QLabel):
    def __init__(self, text, font_size=16, is_bold=True, parent=None):
        super().__init__(text, parent)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        if is_bold:
            self.setFont(QFont("Arial", font_size, QFont.Weight.ExtraBold))
        else:
            self.setFont(QFont("Arial", font_size))
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

    def setText(self, text):
        super().setText(text)
        self.adjustSize()  # Metin değiştiğinde boyutu ayarla