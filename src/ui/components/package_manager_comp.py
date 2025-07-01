from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QHBoxLayout
from PyQt6.QtGui import QDesktopServices
from PyQt6.QtCore import Qt, QUrl

import subprocess

from src.ui.widgets.BLabel import BLabel
from src.ui.widgets.gif_viewer import GifViewer


class PackageManagerComp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 30, 10, 10)
        # layout.setSpacing(20)

        desc = """
Program yüklemek için internette dolaşma
Bismih Linux, Mağaza ve Uçbirim desteği ile kolaylıkla program yükle
"""
        lb_desc = BLabel(desc)

        layout.addWidget(lb_desc)

        # Mağaza sistemi

        lyt_stores = QHBoxLayout()
        lyt_stores.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lyt_pardus_store = QVBoxLayout()
        lyt_kesfet_store = QVBoxLayout()
        lyt_pardus_store.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lyt_kesfet_store.setAlignment(Qt.AlignmentFlag.AlignCenter)

        lb_pardus_store = BLabel(
            "Pardus Mağaza ile Tüm Sistem paketleri", 10, is_bold=True
        )
        lb_kesfet_store = BLabel(
            "Kesfet Mağaza ile Daha Güncel ve Fazla Seçenek", 10, is_bold=True
        )
        gif_pardus_store = GifViewer(
            "data/gifs/pardus_magasa.gif", fixed_size=(200, 200)
        )
        gif_kesfet_store = GifViewer("data/gifs/kesfet.gif", fixed_size=(200, 200))

        btn_pardus_store = QPushButton("Pardus Mağaza")
        btn_pardus_store.clicked.connect(lambda: self.open_app("pardus-software"))
        btn_kesfet_store = QPushButton("Kesfet Mağaza")
        btn_kesfet_store.clicked.connect(lambda: self.open_app("plasma-discover"))

        lyt_pardus_store.addWidget(lb_pardus_store)
        lyt_pardus_store.addWidget(gif_pardus_store)
        lyt_pardus_store.addWidget(btn_pardus_store)

        lyt_kesfet_store.addWidget(lb_kesfet_store)
        lyt_kesfet_store.addWidget(gif_kesfet_store)
        lyt_kesfet_store.addWidget(btn_kesfet_store)

        lyt_stores.addLayout(lyt_pardus_store)
        lyt_stores.addStretch(1)  # Araya boşluk ekle
        lyt_stores.addLayout(lyt_kesfet_store)

        lyt_extra = QHBoxLayout()
        lyt_nala = QVBoxLayout()
        lyt_krunner = QVBoxLayout()
        lyt_extra.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lyt_krunner.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lyt_nala.setAlignment(Qt.AlignmentFlag.AlignCenter)

        lb_nala = BLabel("Uç birimden hızlı ve görsel yükleme", 10, is_bold=True)
        gif_nala = GifViewer("data/gifs/nala.gif", fixed_size=(200, 200))
        lyt_nala.addWidget(lb_nala)
        lyt_nala.addWidget(gif_nala)

        lb_krunner = BLabel("KRunner ile Hızlı Arama", 10, is_bold=True)
        gif_krunner = GifViewer("data/gifs/krunner.gif", fixed_size=(200, 200))
        lyt_krunner.addWidget(lb_krunner)
        lyt_krunner.addWidget(gif_krunner)

        lyt_extra.addLayout(lyt_nala)
        lyt_extra.addStretch(1)  # Araya boşluk ekle
        lyt_extra.addLayout(lyt_krunner)

        layout.addLayout(lyt_stores)
        layout.addLayout(lyt_extra)

        # Belgeler Butonu
        docBtn = QPushButton("📘 Paket Yönetimi Belgeleri")
        docBtn.clicked.connect(
            lambda: QDesktopServices.openUrl(
                QUrl("https://github.com/bismih-org/.github/wiki")
            )
        )
        layout.addWidget(docBtn)

        self.setLayout(layout)

    def open_app(self, app_name: str):
        subprocess.Popen(app_name, shell=True)

    def updateWid(self):
        pass
