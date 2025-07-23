from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame
from PyQt6.QtCore import Qt
from src.ui.widgets.BLabel import BLabel
from src.ui.widgets.gif_viewer import GifViewer


class PanelComp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        gif_panel = GifViewer("data/gifs/panel.gif", fixed_size=(1000, 250))

        layout.addWidget(gif_panel, alignment=Qt.AlignmentFlag.AlignCenter)
        # Giriş Açıklaması
        intro = BLabel(
            "Panel, sisteminizin kontrol merkezidir. Aşağıda panel üzerindeki ögelerin kısa açıklamalarını bulabilirsiniz:",
            12,
            is_bold=True,
        )
        layout.addWidget(intro)

        def section(title: str, desc: str):
            box = QVBoxLayout()
            titleLabel = QLabel(f"🔹 {title}")
            titleLabel.setStyleSheet("font-weight: bold; font-size: 12pt;")
            descLabel = QLabel(desc)
            descLabel.setWordWrap(True)
            descLabel.setStyleSheet("font-size: 11pt; color: gray;")
            box.addWidget(titleLabel)
            box.addWidget(descLabel)
            return box

        # Panel bölümlerini anlat
        layout.addLayout(
            section(
                "Yapay Zeka Asistanları",
                "Panelde yer alan 5 farklı yapay zeka asistanına hızlı erişim sunar. Sistemle etkileşim kurmak için birini seçin ve kullanın.",
            )
        )

        layout.addLayout(
            section(
                "Renk Seçici",
                "Paneldeki renk damlası simgesi ile herhangi bir bölgeden renk kodu seçebilirsiniz. Tasarımcılar için idealdir.",
            )
        )

        layout.addLayout(
            section(
                "Masaüstü Geçişleri",
                "Çoklu masaüstü arasında geçiş yapmanızı sağlar. Verimliliği artırmak için sanal alanlar oluşturabilirsiniz.",
            )
        )

        layout.addLayout(
            section(
                "Donanım İzleme (CPU, RAM, Ağ)",
                "Gerçek zamanlı grafikler ile sistem kaynak kullanımını takip edebilirsiniz.",
            )
        )

        layout.addLayout(
            section(
                "Hava Durumu ve Takvim",
                "Anlık hava durumu bilgisi ve entegre takvim ile gününüzü planlayın.",
            )
        )

        layout.addLayout(
            section(
                "Sistem Tepsisi",
                "Bluetooth, Wi-Fi, güç durumu, ses gibi sistem bileşenlerine hızlı erişim sağlar.",
            )
        )

        layout.addLayout(
            section(
                "Genel Menü Düğmesi",
                "Sol üst köşede yer alan ikonla menüye erişebilir, uygulamaları başlatabilirsiniz.",
            )
        )

        # İsteğe bağlı separator
        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.HLine)
        separator.setFrameShadow(QFrame.Shadow.Sunken)
        layout.addWidget(separator)

        self.setLayout(layout)

    def updateWid(self):
        pass
