from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


class SystemImprovementComp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Ana düzen oluşturma
        mainLayout = QVBoxLayout(self)
        mainLayout.setSpacing(0)
        mainLayout.setContentsMargins(0, 0, 0, 0)

        font = QFont("Arial", 16, QFont.Weight.Bold)

        label = QLabel("Sistem İyileştirmeleri")
        label.setObjectName("shortcutLabel")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setFont(font)
        mainLayout.addWidget(label)

        self.setLayout(mainLayout)

    def updateWid(self):
        pass
