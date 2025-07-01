from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
)
from PyQt6.QtCore import Qt
from src.ui.widgets.BLabel import BLabel
from src.ui.widgets.gif_viewer import GifViewer


class ThemeComp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Ana düzen oluşturma
        mainLayout = QVBoxLayout(self)
        mainLayout.setSpacing(0)
        mainLayout.setContentsMargins(0, 0, 0, 0)

        gif = GifViewer("data/gifs/tema.gif", fixed_size=(500, 500))
        mainLayout.addWidget(gif, alignment=Qt.AlignmentFlag.AlignCenter)

        lb_desc = BLabel(
            """
Tema ayarları, sistemin görünümünü ve hissini özelleştirmenizi sağlar. Bu ayarlar, renk paletleri, yazı tipleri ve genel tema seçeneklerini içerir. Tema ayarlarını değiştirerek, kullanıcı arayüzünü kişisel tercihlerinize göre uyarlayabilirsiniz. Bu, daha iyi bir kullanıcı deneyimi sağlar ve sistemin görsel estetiğini artırır. Tema ayarları sistem ayarları menüsünde bulunur ve kullanıcıların kolayca erişebileceği bir şekilde düzenlenmiştir. Ek olarak yeni temalar yükleyebilir veya mevcut temaları düzenleyebilirsiniz.
        """,
            alignment="Left",
            is_bold=False,
        )
        lb_desc.setWordWrap(True)
        mainLayout.addWidget(lb_desc, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(mainLayout)

    def updateWid(self):
        pass
