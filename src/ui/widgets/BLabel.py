from PyQt6.QtWidgets import (
    QLabel,
    QSizePolicy,
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt



class BLabel(QLabel):
    def __init__(self, text, font_size=16, is_bold=True, alignment="Center", parent=None):
        super().__init__(text, parent)
        if alignment == "Center":
            self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        elif alignment == "Left":
            self.setAlignment(Qt.AlignmentFlag.AlignLeft)
        elif alignment == "Right":
            self.setAlignment(Qt.AlignmentFlag.AlignRight)

        if is_bold:
            self.setFont(QFont("Arial", font_size, QFont.Weight.ExtraBold))
        else:
            self.setFont(QFont("Arial", font_size))
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

    def setText(self, text):
        super().setText(text)
        self.adjustSize()  # Metin değiştiğinde boyutu ayarla