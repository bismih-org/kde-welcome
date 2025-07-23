from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
)
from PyQt6.QtCore import Qt
from src.ui.widgets.BLabel import BLabel
from src.ui.widgets.gif_viewer import GifViewer


class QuickMenuComp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Ana düzen oluşturma
        mainLayout = QVBoxLayout(self)
        mainLayout.setContentsMargins(20, 20, 20, 20)

        # Başlık ve açıklama ekle
        self.title = BLabel("Hızlı Menü", 27, is_bold=True)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        mainLayout.addWidget(self.title)

        self.description = BLabel(
            """
Hızlı Menü ile bir çok kısyalo ve işlemi tek tıkla yapabilirsiniz.

Kullanmak için
ctrl+shift+j
"""
        )
        self.description.setAlignment(Qt.AlignmentFlag.AlignCenter)
        mainLayout.addWidget(self.description)

        gif_ozel_panel = GifViewer("data/gifs/ozel_panel.gif", fixed_size=(400, 400))
        mainLayout.addWidget(gif_ozel_panel, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(mainLayout)

    def updateWid(self):
        pass
