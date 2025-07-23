from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QPushButton, QHBoxLayout,
                             QFrame, QScrollArea, QGridLayout, QSizePolicy)
from PyQt6.QtGui import QDesktopServices, QPalette, QFont
from PyQt6.QtCore import Qt, QUrl, pyqtSignal

import subprocess

from src.ui.widgets.BLabel import BLabel
from src.ui.widgets.gif_viewer import GifViewer


class StoreCard(QFrame):
    """Her mağaza için özel kart widget'ı"""
    clicked = pyqtSignal(str)

    def __init__(self, title, description, gif_path, app_name, button_text):
        super().__init__()
        self.app_name = app_name
        self.setupUI(title, description, gif_path, button_text)

    def setupUI(self, title, description, gif_path, button_text):
        # Kart stilini ayarla
        self.setFrameStyle(QFrame.Shape.Box)
        self.setStyleSheet("""
            StoreCard {
                background-color: rgba(255, 255, 255, 0.05);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 12px;
                padding: 15px;
            }
            StoreCard:hover {
                background-color: rgba(255, 255, 255, 0.08);
                border: 1px solid rgba(255, 255, 255, 0.2);
            }
        """)

        layout = QVBoxLayout(self)
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)

        # Başlık
        title_label = BLabel(title, 12, is_bold=True)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)

        # Açıklama
        desc_label = BLabel(description, 9)
        desc_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        desc_label.setWordWrap(True)
        layout.addWidget(desc_label)

        # GIF viewer
        gif_viewer = GifViewer(gif_path, fixed_size=(220, 220))
        layout.addWidget(gif_viewer)

        # Buton
        button = QPushButton(button_text)

        button.clicked.connect(lambda: self.clicked.emit(self.app_name))
        layout.addWidget(button)

        # Minimum genişlik ayarla
        self.setMinimumWidth(320)
        self.setMaximumWidth(360)


class FeatureCard(QFrame):
    """Özellik kartları için widget"""

    def __init__(self, title, gif_path):
        super().__init__()
        self.setupUI(title, gif_path)

    def setupUI(self, title, gif_path):
        # Kart stilini ayarla
        self.setFrameStyle(QFrame.Shape.Box)
        self.setStyleSheet("""
            FeatureCard {
                background-color: rgba(255, 255, 255, 0.03);
                border: 1px solid rgba(255, 255, 255, 0.08);
                border-radius: 10px;
                padding: 10px;
            }
            FeatureCard:hover {
                background-color: rgba(255, 255, 255, 0.05);
            }
        """)

        layout = QVBoxLayout(self)
        layout.setSpacing(12)
        layout.setContentsMargins(15, 15, 15, 15)

        # Başlık
        title_label = BLabel(title, 10, is_bold=True)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)

        # GIF viewer
        gif_viewer = GifViewer(gif_path, fixed_size=(200, 200))
        layout.addWidget(gif_viewer)

        self.setMinimumWidth(260)
        self.setMaximumWidth(300)


class PackageManagerComp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Ana scroll area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)


        # İçerik widget'ı
        content_widget = QWidget()
        layout = QVBoxLayout(content_widget)
        layout.setContentsMargins(20, 30, 20, 30)
        layout.setSpacing(30)

        # Başlık ve açıklama bölümü
        header_layout = QVBoxLayout()
        header_layout.setSpacing(15)

        # Ana başlık
        title_label = BLabel("📦 Paket Yöneticisi", 16, is_bold=True)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header_layout.addWidget(title_label)

        # Açıklama
        desc = """Program yüklemek için internette dolaşma
Bismih Linux, Mağaza ve Uçbirim desteği ile kolaylıkla program yükle"""

        desc_label = BLabel(desc, 11)
        desc_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        desc_label.setWordWrap(True)

        header_layout.addWidget(desc_label)

        layout.addLayout(header_layout)

        # Mağaza bölümü
        stores_section = QVBoxLayout()
        stores_section.setSpacing(20)

        # Mağaza başlığı
        stores_title = BLabel("🏪 Mağazalar", 14, is_bold=True)
        stores_title.setStyleSheet("color: #4CAF50; margin-bottom: 10px;")
        stores_section.addWidget(stores_title)

        # Mağaza kartları container
        stores_container = QHBoxLayout()
        stores_container.setSpacing(20)
        stores_container.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Pardus Mağaza kartı
        pardus_card = StoreCard(
            "Pardus Mağaza",
            "Tüm sistem paketleri için resmi mağaza",
            "data/gifs/pardus_magasa.gif",
            "pardus-software",
            "Pardus Mağaza'yı Aç"
        )
        pardus_card.clicked.connect(self.open_app)
        stores_container.addWidget(pardus_card)

        # Kesfet Mağaza kartı
        kesfet_card = StoreCard(
            "Kesfet Mağaza",
            "Daha güncel ve fazla seçenek için modern mağaza",
            "data/gifs/kesfet.gif",
            "plasma-discover",
            "Kesfet Mağaza'yı Aç"
        )
        kesfet_card.clicked.connect(self.open_app)
        stores_container.addWidget(kesfet_card)

        stores_section.addLayout(stores_container)
        layout.addLayout(stores_section)

        # Ek özellikler bölümü
        features_section = QVBoxLayout()
        features_section.setSpacing(20)

        # Özellikler başlığı
        features_title = BLabel("⚡ Hızlı Erişim Araçları", 14, is_bold=True)
        features_section.addWidget(features_title)

        # Özellik kartları container
        features_container = QHBoxLayout()
        features_container.setSpacing(30)
        features_container.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Nala kartı
        nala_card = FeatureCard(
            "Uç birimden hızlı ve görsel yükleme",
            "data/gifs/nala.gif"
        )
        features_container.addWidget(nala_card)

        # KRunner kartı
        krunner_card = FeatureCard(
            "KRunner ile Hızlı Arama",
            "data/gifs/krunner.gif"
        )
        features_container.addWidget(krunner_card)

        features_section.addLayout(features_container)
        layout.addLayout(features_section)

        # Belgeler bölümü
        docs_section = QVBoxLayout()
        docs_section.setSpacing(15)

        # Belgeler başlığı
        docs_title = BLabel("📖 Belgeler", 14, is_bold=True)
        docs_title.setStyleSheet("color: #2196F3; margin-bottom: 10px;")
        docs_section.addWidget(docs_title)

        # Belgeler butonu
        docs_button = QPushButton("📘 Paket Yönetimi Belgelerini Görüntüle")
        docs_button.clicked.connect(
            lambda: QDesktopServices.openUrl(
                QUrl("https://github.com/bismih-org/.github/wiki")
            )
        )
        docs_section.addWidget(docs_button)

        layout.addLayout(docs_section)

        # Layout'a esnek alan ekle
        layout.addStretch()

        # Scroll area'yı ayarla
        scroll_area.setWidget(content_widget)

        # Ana layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(scroll_area)

        self.setLayout(main_layout)

    def open_app(self, app_name: str):
        """Uygulamayı güvenli bir şekilde başlat"""
        try:
            subprocess.Popen(app_name, shell=True)
        except Exception as e:
            print(f"Uygulama başlatılamadı: {app_name}, Hata: {e}")

    def updateWid(self):
        """Widget güncelleme fonksiyonu"""
        pass
