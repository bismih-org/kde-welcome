from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPlainTextEdit,
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

from src.ui.widgets.BLabel import BLabel


class SystemImprovementComp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Ana düzen
        mainLayout = QVBoxLayout(self)
        mainLayout.setSpacing(10)
        mainLayout.setContentsMargins(15, 15, 15, 15)

        # Başlık
        label = BLabel("", font_size=13,alignment="left")
        mainLayout.addWidget(label)

        improvements_text = (
            "Öne Çıkan Sistem İyileştirmeleri:\n\n"
            "1. Gelişmiş Kernel Desteği\n"
            "   - Stable, Backports ve Rolling (Liquorix) çekirdek seçenekleri\n\n"
            "2. Geniş Donanım Uyumluluğu\n"
            "   - WiFi, Bluetooth, GPU gibi tüm firmware paketleri önceden yüklü\n\n"
            "3. Modern Ses Sistemi\n"
            "   - Pipewire + WirePlumber, PulseAudio yerine tercih ediliyor\n\n"
            "4. KDE Masaüstü Özelleştirmeleri\n"
            "   - Hafifletilmiş KDE kurulumu\n"
            "   - Kapanma sorunlarını önleyen systemd servisi\n\n"
            "5. Pardus Entegrasyonu\n"
            "   - pardus-about, pardus-installer, pardus-update gibi araçlar dahil\n\n"
            "6. Flatpak & Flathub Desteği\n"
            "   - Flatpak yapılandırılmış ve bazı popüler uygulamalar önceden kurulu\n\n"
            "7. Kullanıcı Dostu Ek Yazılımlar\n"
            "   - LibreOffice, VLC, Thunderbird, OnlyOffice, Timeshift vb.\n\n"
            "8. Terminal ve Shell Geliştirmeleri\n"
            "   - Varsayılan shell: Zsh\n"
            "   - Ek araçlar: zoxide, nala, bash-completion\n\n"
            "9. AppImage ve WebApp Entegrasyonu\n"
            "   - AppImageLauncher ve WebApp Manager hazır\n\n"
            "10. Temiz ISO Üretimi\n"
            "   - Loglar ve geçici dosyalar temizlenerek küçük boyutlu ISO üretilir"
        )

        label.setText(improvements_text)

        self.setLayout(mainLayout)

    def updateWid(self):
        pass
