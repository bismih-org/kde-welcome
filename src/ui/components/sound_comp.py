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

class SoundComp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

        

    def initUI(self):
        # Ana düzen oluşturma
        mainLayout = QVBoxLayout(self)
        mainLayout.setSpacing(0)
        mainLayout.setContentsMargins(0, 0, 0, 0)

        font = QFont("Arial", 16, QFont.Weight.Bold)

        label = QLabel("Ses ayarlarını özelleştirin.")
        label.setObjectName("shortcutLabel")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setFont(font)
        mainLayout.addWidget(label)


        self.setLayout(mainLayout)