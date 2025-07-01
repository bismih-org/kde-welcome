from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
)
from PyQt6.QtCore import Qt
from src.ui.widgets.BLabel import BLabel
from src.ui.widgets.gif_viewer import GifViewer


class SoundComp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Ana düzen oluşturma
        mainLayout = QHBoxLayout(self)
        mainLayout.setSpacing(0)
        mainLayout.setContentsMargins(0, 0, 0, 0)

        lyt_blow_panel = QVBoxLayout()
        lb_b_panel = BLabel(
            "Alt panelde her uygulamanın \nsesi kısılıp ayarlanabilmektedir.",
            is_bold=True,
        )
        gif_blow_panel = GifViewer("data/gifs/ses_alt.gif", fixed_size=(400, 400))

        lyt_blow_panel.addWidget(lb_b_panel, alignment=Qt.AlignmentFlag.AlignCenter)
        lyt_blow_panel.addWidget(gif_blow_panel, alignment=Qt.AlignmentFlag.AlignCenter)
        mainLayout.addLayout(lyt_blow_panel, stretch=1)

        lyt_menu = QVBoxLayout()
        lb_menu = BLabel(
            "Özel menü içerisindeki ses \nefektleriyle gürültü engelleme \nyapılabilmektedir.",
            is_bold=True,
        )
        gif_menu = GifViewer("data/gifs/menu.gif", fixed_size=(400, 400))

        lyt_menu.addWidget(lb_menu, alignment=Qt.AlignmentFlag.AlignCenter)
        lyt_menu.addWidget(gif_menu, alignment=Qt.AlignmentFlag.AlignCenter)

        lyt_top_panel = QVBoxLayout()
        lb_top_panel = BLabel(
            "Üst panelden detaylı \nses ayarlarına ulaşabilirsiniz.", is_bold=True
        )
        gif_top_panel = GifViewer("data/gifs/panel_ust.gif", fixed_size=(400, 400))

        lyt_top_panel.addWidget(lb_top_panel, alignment=Qt.AlignmentFlag.AlignCenter)
        lyt_top_panel.addWidget(gif_top_panel, alignment=Qt.AlignmentFlag.AlignCenter)

        mainLayout.addLayout(lyt_blow_panel, stretch=1)
        mainLayout.addLayout(lyt_menu, stretch=1)
        mainLayout.addLayout(lyt_top_panel, stretch=1)

        self.setLayout(mainLayout)

    def updateWid(self):
        pass
