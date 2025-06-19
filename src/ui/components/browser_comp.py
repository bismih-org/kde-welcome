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

class BrowserComp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

        

    def initUI(self):
        # Ana düzen oluşturma
        mainLayout = QVBoxLayout(self)
        mainLayout.setSpacing(0)
        mainLayout.setContentsMargins(0, 0, 0, 0)

        font = QFont("Arial", 16, QFont.Weight.Bold)

        label = QLabel("Zen Tarayıcısı ile web'de gezinmenin yeni bir yolunu keşfedin.")
        label.setObjectName("shortcutLabel")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setFont(font)
        mainLayout.addWidget(label)


        self.setLayout(mainLayout)

    def update(self):
        pass
