from PyQt6.QtWidgets import (
    QPushButton,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QFrame,
    QGridLayout,
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap, QFont
from src.ui.widgets.BLabel import BLabel
import webbrowser


class CommunicationComp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Ana düzen oluşturma
        mainLayout = QVBoxLayout(self)
        mainLayout.setSpacing(15)
        mainLayout.setContentsMargins(20, 20, 20, 20)

        # Başlık
        title_label = BLabel("İletişim Bilgileri")
        mainLayout.addWidget(title_label)

        # Açıklama metni
        desc_label = QLabel("Bizimle iletişime geçmek için aşağıdaki kanalları kullanabilirsiniz:")
        desc_label.setWordWrap(True)
        desc_label.setStyleSheet("color: #666; font-size: 14px; margin-bottom: 10px;")
        mainLayout.addWidget(desc_label)

        # İletişim kartları için grid layout
        cards_layout = QGridLayout()
        cards_layout.setSpacing(10)

        # GitHub kartı
        github_card = self.generate_contact_card(
            "GitHub",
            "Kaynak kod, issue'lar ve katkıda bulunma",
            "https://github.com/bismih-org",
            "#24292e"
        )
        cards_layout.addWidget(github_card, 0, 0)

        # Forum kartı
        forum_card = self.generate_contact_card(
            "Forum",
            "Topluluk tartışmaları ve destek",
            "https://github.com/orgs/bismih-org/discussions",
            "#0969da"
        )
        cards_layout.addWidget(forum_card, 0, 1)

        # Signal kartı
        discord_card = self.generate_contact_card(
            "Signal",
            "Anlık sohbet ve topluluk",
            "https://signal.group/#CjQKILD6taU2K6HXyYScZY08o4o2krF3xQDktDrxFIq16JNiEhAS6WpiAcJ6a2_Ii_2GFDrQ",  # Gerçek link ile değiştirin
            "#2530FD"
        )
        cards_layout.addWidget(discord_card, 1, 0)

        # Email kartı
        email_card = self.generate_contact_card(
            "E-posta",
            "Resmi iletişim ve destek",
            "mailto:halakmuhammet145@gmail.com",  # Gerçek email ile değiştirin
            "#ea4335"
        )
        cards_layout.addWidget(email_card, 1, 1)

        mainLayout.addLayout(cards_layout)

        # Ayırıcı çizgi
        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.HLine)
        separator.setStyleSheet("background-color: #ddd; margin: 10px 0;")
        mainLayout.addWidget(separator)

        # Ek bilgi
        info_label = QLabel("💡 İpucu: Hızlı yanıt için GitHub Issues veya Forum kullanınız.")
        info_label.setStyleSheet("color: #0969da; font-size: 12px; font-style: italic;")
        mainLayout.addWidget(info_label, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(mainLayout)

    def generate_contact_card(self, title: str, description: str, url: str, color: str):
        """İletişim kartı oluşturur"""
        card = QFrame()
        card.setFrameShape(QFrame.Shape.Box)
        card.setStyleSheet(f"""
            QFrame {{
                border: 2px solid {color};
                border-radius: 8px;
                background-color: rgba(255, 255, 255, 0.8);
                padding: 10px;
                margin: 5px;
            }}
            QFrame:hover {{
                background-color: rgba({self.hex_to_rgb(color)}, 0.1);
                border-color: {color};
            }}
        """)
        card.setMinimumHeight(100)
        card.setCursor(Qt.CursorShape.PointingHandCursor)

        layout = QVBoxLayout(card)
        layout.setSpacing(5)

        # Başlık
        title_label = QLabel(title)
        title_label.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        title_label.setStyleSheet(f"color: {color};")
        layout.addWidget(title_label)

        # Açıklama
        desc_label = QLabel(description)
        desc_label.setWordWrap(True)
        desc_label.setStyleSheet("color: #666; font-size: 11px;")
        layout.addWidget(desc_label)

        # Tıklama olayı
        card.mousePressEvent = lambda event: self.open_link(url)

        return card

    def hex_to_rgb(self, hex_color: str) -> str:
        """Hex rengi RGB'ye çevirir"""
        hex_color = hex_color.lstrip('#')
        return ', '.join(str(int(hex_color[i:i+2], 16)) for i in (0, 2, 4))

    def open_link(self, url: str):
        webbrowser.open(url)

    def updateWid(self):
        pass
