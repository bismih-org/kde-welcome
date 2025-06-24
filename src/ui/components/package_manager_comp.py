from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QTextBrowser
)
from PyQt6.QtGui import QFont, QDesktopServices
from PyQt6.QtCore import Qt, QUrl


class PackageManagerComp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(16)

        # Başlık
        title = QLabel("📦 Paket Yönetimi")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 16pt; font-weight: bold;")
        layout.addWidget(title)

        # Açıklayıcı metin
        description = QLabel(
            "Bismih Linux’ta yazılım yüklemek için hem grafik arayüz hem de terminal araçlarını kullanabilirsiniz.\n"
            "Flatpak, KDE Discover ve Nala entegrasyonları ile tam kontrol sizde."
        )
        description.setWordWrap(True)
        description.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(description)

        # Discover
        discoverTitle = QLabel("🛍️ KDE Discover")
        discoverTitle.setStyleSheet("font-size: 13pt; font-weight: bold;")
        layout.addWidget(discoverTitle)

        discoverDesc = QLabel(
            "- Uygulamaları kolayca kurun, güncelleyin.\n"
            "- Flatpak ve sistem paketleri desteklenir.\n"
            "- Arama çubuğundan uygulama ismiyle erişebilirsiniz."
        )
        discoverDesc.setWordWrap(True)
        layout.addWidget(discoverDesc)

        # KRunner
        krunnerTitle = QLabel("🚀 KRunner ile Hızlı Kurulum")
        krunnerTitle.setStyleSheet("font-size: 13pt; font-weight: bold;")
        layout.addWidget(krunnerTitle)

        krunnerDesc = QLabel(
            "- 'KRunner'ı açın (Alt + Space)\n"
            "- Uygulama adını yazın, yükleme için yönlendirme alın."
        )
        krunnerDesc.setWordWrap(True)
        layout.addWidget(krunnerDesc)

        # Nala
        nalaTitle = QLabel("💻 Nala (Terminal Üzerinden)")
        nalaTitle.setStyleSheet("font-size: 13pt; font-weight: bold;")
        layout.addWidget(nalaTitle)

        nalaDesc = QLabel(
            "- Modern, renkli ve hızlı bir APT arayüzü.\n"
            "- Kullanım örneği: nala install firefox\n"
            "- Daha fazla bilgi için: nala --help"
        )
        nalaDesc.setWordWrap(True)
        layout.addWidget(nalaDesc)

        # Belgeler Butonu
        docBtn = QPushButton("📘 Paket Yönetimi Belgeleri")
        docBtn.clicked.connect(lambda: QDesktopServices.openUrl(QUrl("https://bismihlinux.org/docs/paketler")))
        layout.addWidget(docBtn)

        self.setLayout(layout)


    def updateWid(self):
        pass
