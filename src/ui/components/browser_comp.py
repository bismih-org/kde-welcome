from PyQt6.QtWidgets import (
    QPushButton,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt, QSize
import webbrowser


from src.ui.widgets.BLabel import BLabel


class BrowserComp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Ana düzen oluşturma
        mainLayout = QVBoxLayout(self)
        mainLayout.setSpacing(0)
        mainLayout.setContentsMargins(20, 20, 20, 20)

        # PNG görselini ekle
        png_label = QLabel()
        pixmap = QIcon("data/images/zen_browser.png").pixmap(QSize(650, 650))
        png_label.setPixmap(pixmap)
        png_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        mainLayout.addWidget(png_label)

        desc = """Zen Browser, kullanıcıların web tarayıcılarını daha verimli ve görsel bir şekilde kullanmalarını sağlayan bir tarayıcıdır.
Tavsiye edilen eklentiler:
- Ublock: Reklam engelleme eklentisi
- Dark Reader: Karanlık mod eklentisi
- Tabliss: Yeni sekme sayfasını özelleştirme eklentisi
- Sideberyy: Kenar çubuğu eklentisi
- Skip Silence: Sesli içeriklerde sessizlikleri atlama eklentisi
"""

        lb_desc = BLabel(desc, alignment="Left", is_bold=False)
        lb_desc.setWordWrap(True)
        mainLayout.addWidget(lb_desc, alignment=Qt.AlignmentFlag.AlignCenter)

        lyt_ext_btns = QHBoxLayout()
        lyt_ext_btns.setContentsMargins(0, 0, 0, 0)
        lyt_ext_btns.setSpacing(10)

        btn_ublock = QPushButton("Ublock")
        btn_ublock.clicked.connect(
            lambda: self.open_link(
                "https://addons.mozilla.org/tr/firefox/addon/ublock-origin/"
            )
        )
        btn_dark_reader = QPushButton("Dark Reader")
        btn_dark_reader.clicked.connect(
            lambda: self.open_link(
                "https://addons.mozilla.org/tr/firefox/addon/darkreader/"
            )
        )
        btn_tabliss = QPushButton("Tabliss")
        btn_tabliss.clicked.connect(
            lambda: self.open_link(
                "https://addons.mozilla.org/tr/firefox/addon/tabliss/"
            )
        )
        btn_sideberyy = QPushButton("Sideberyy")
        btn_sideberyy.clicked.connect(
            lambda: self.open_link(
                "https://addons.mozilla.org/tr/firefox/addon/sidebery/"
            )
        )

        btn_skip_slience = QPushButton("Skip Silence")
        btn_skip_slience.clicked.connect(
            lambda: self.open_link(
                "https://addons.mozilla.org/tr/firefox/addon/skip-silence/"
            )
        )

        lyt_ext_btns.addWidget(btn_ublock)
        lyt_ext_btns.addWidget(btn_dark_reader)
        lyt_ext_btns.addWidget(btn_tabliss)
        lyt_ext_btns.addWidget(btn_sideberyy)
        lyt_ext_btns.addWidget(btn_skip_slience)

        mainLayout.addLayout(lyt_ext_btns)

        self.setLayout(mainLayout)

    def open_link(self, url: str):
        webbrowser.open(url)

    def updateWid(self):
        pass
