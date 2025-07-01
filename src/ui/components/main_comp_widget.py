from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
)


class MainCompWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Ana widget oluşturma
        self.setObjectName("mainCompWidget")

        # Ana düzen oluşturma
        mainLayout = QVBoxLayout(self)
        mainLayout.setSpacing(0)
        mainLayout.setContentsMargins(0, 0, 0, 0)

        label = QLabel("Test")
        mainLayout.addWidget(label)
        self.setLayout(mainLayout)

    def updateWid(self):
        pass
