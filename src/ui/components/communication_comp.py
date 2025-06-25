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
import webbrowser
from src.ui.widgets.BLabel import BLabel
from src.ui.widgets.gif_viewer import GifViewer

class CommunicationComp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

        

    def initUI(self):
        # Ana düzen oluşturma
        mainLayout = QVBoxLayout(self)
        mainLayout.setSpacing(0)
        mainLayout.setContentsMargins(0, 0, 0, 0)


        label = BLabel("İletişim Bilgileri")
        mainLayout.addWidget(label)

        lyt_btn = QHBoxLayout()

        btn_github = QPushButton("GitHub")
        btn_github.clicked.connect(lambda: self.open_link("https://github.com/bismih-org"))

        btn_forum = QPushButton("Forum")
        btn_forum.clicked.connect(lambda: self.open_link("https://github.com/orgs/bismih-org/discussions"))

        lyt_btn.addWidget(btn_github, alignment=Qt.AlignmentFlag.AlignCenter)
        lyt_btn.addWidget(btn_forum, alignment=Qt.AlignmentFlag.AlignCenter)

        mainLayout.addLayout(lyt_btn)

        self.setLayout(mainLayout)

    def updateWid(self):
        pass
