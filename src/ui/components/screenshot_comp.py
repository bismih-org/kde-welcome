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

from src.ui.widgets.BLabel import BLabel
from src.ui.widgets.gif_viewer import GifViewer
class ScreenShotComp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

        

    def initUI(self):
        # Ana düzen oluşturma
        mainLayout = QHBoxLayout(self)
        mainLayout.setContentsMargins(0, 0, 0, 0)


        lyt_flame = QVBoxLayout()
        lb_flame = BLabel("Print tuşu ile detaylı ekran görüntüsü",is_bold=True)
        gif_flame = GifViewer("data/gifs/ekran.gif", fixed_size=(550, 550))

        lyt_flame.addWidget(lb_flame, alignment=Qt.AlignmentFlag.AlignCenter)
        lyt_flame.addWidget(gif_flame, alignment=Qt.AlignmentFlag.AlignCenter)

        lyt_normcap = QVBoxLayout()
        lb_normcap = BLabel("Ctrl + Print tuşu ile resimden yazıya", is_bold=True)
        gif_normcap = GifViewer("data/gifs/ekran_yazi.gif", fixed_size=(550, 550))

        lyt_normcap.addWidget(lb_normcap, alignment=Qt.AlignmentFlag.AlignCenter)
        lyt_normcap.addWidget(gif_normcap, alignment=Qt.AlignmentFlag.AlignCenter)

        mainLayout.addLayout(lyt_flame, stretch=1)
        mainLayout.addLayout(lyt_normcap, stretch=1)


        self.setLayout(mainLayout)

    def updateWid(self):
        pass
