from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt, QSize
import os

from src.ui.widgets.BLabel import BLabel
from src.static import config as cfg


class ShortcutComp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.mainLayout = QHBoxLayout(self)
        self.mainLayout.setContentsMargins(10, 30, 10, 10)
        self.mainLayout.setSpacing(20)

        self.lyt_left = QVBoxLayout()
        self.lyt_left.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.lyt_left.setContentsMargins(0, 0, 0, 0)
        self.lyt_left.setSpacing(10)

        self.lyt_right = QVBoxLayout()
        self.lyt_right.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.lyt_right.setContentsMargins(0, 0, 0, 0)
        self.lyt_right.setSpacing(10)

        self.keyboard_part()
        self.touchpad_part()

        self.mainLayout.addLayout(self.lyt_left)
        self.mainLayout.addLayout(self.lyt_right)

    def keyboard_part(self):
        title = BLabel("Klavye Kısayolları", 20, is_bold=True)
        self.lyt_left.addWidget(title)

        shortcuts = [
            ("🖨️ Print", "Ekran Görüntüsü"),
            ("📸 Ctrl + Print", "Görselden Yazıya"),
            ("📁 Meta + E", "Dosya Yöneticisi"),
            ("🖥️ Meta + Ctrl ⇦ ⇨", "Sanal Masaüstlerinde Gezinme"),
            ("🖥️ Meta + Ctrl + Shift⇦ ⇨", "Sanal Masaüstlerinde Pencreyle Gezinme"),
            ("🖱️ Meta + Fare sağ", "Pencere Taşıma"),
            ("🔍 Meta + Fare Sol", "Pencere Büyütme/Küçültme"),
            ("🌐 Meta + F", "Tarayıcı"),
            ("⚡ Ctrl + Alt + T", "Uçbirim Açma"),
        ]

        for shortcut, description in shortcuts:
            widget = ShortcutWidget(shortcut, description)
            self.lyt_left.addWidget(widget)

    def touchpad_part(self):
        title = BLabel("Dokunmatik Yüzey Hareketleri", 20, is_bold=True)
        self.lyt_right.addWidget(title)

        gestures3 = [
            ("👆 Üç parmak Yukarı", "Pencere tam ekran"),
            ("👇 Üç parmak Aşağı", "Pencere aşağı indirme"),
            ("👈👉 Üç parmak Sağ Sol", "Pencereleri sağa \nsola yerleştirme"),
            ("🤏 Üç parmak içeri", "Pencere kapama"),
        ]

        image_path3 = "data/images/gestures/3gesture_"

        self.touchpad_wid2 = TouchpadWidget(
            [gesture[0] for gesture in gestures3],
            [gesture[1] for gesture in gestures3],
            image_path3,
        )
        self.lyt_right.addWidget(self.touchpad_wid2)

        gestures4 = [
            ("👆👆 Dört parmak Yukarı", "Sanal Masaüstü Izgarası"),
            ("👇👇 Dört parmak Aşağı", "KRunner Arama"),
            ("↔️ Dört parmak Sağ Sol", "Sanal Masaüstleri Arasında Gezinme"),
        ]

        image_path4 = "data/images/gestures/4gesture_"
        self.touchpad_wid4 = TouchpadWidget(
            [gesture[0] for gesture in gestures4],
            [gesture[1] for gesture in gestures4],
            image_path4,
        )
        self.lyt_right.addWidget(self.touchpad_wid4)

    def updateWid(self):
        self.touchpad_wid2.updateWid()


class ShortcutWidget(QWidget):
    def __init__(self, shortcut_name, description):
        super().__init__()
        self.shortcut_name = shortcut_name
        self.description = description
        self.initUI()

    def initUI(self):
        layout = QHBoxLayout(self)

        lb_shortcut = BLabel(self.shortcut_name, 11, alignment="Left")
        lb_description = BLabel(self.description, 9, alignment="Left")

        layout.addWidget(lb_shortcut)
        layout.addWidget(lb_description)

        self.setLayout(layout)

        # Set a fixed height for the widget
        self.setFixedHeight(45)


class TouchpadWidget(QWidget):
    def __init__(self, gesture_names, descriptions, image_path):
        super().__init__()
        self.gesture_names = gesture_names
        self.descriptions = descriptions
        self.image_path = image_path
        self.initUI()

    def initUI(self):
        layout = QHBoxLayout(self)
        lyt_image = QVBoxLayout()
        lyt_desc = QVBoxLayout()
        layout.addLayout(lyt_image)
        layout.addLayout(lyt_desc)
        self.label_image = QLabel()

        for name, desc in zip(self.gesture_names, self.descriptions):
            widget = ShortcutWidget(name, desc)
            lyt_desc.addWidget(widget)

        self.updateWid()
        lyt_image.addWidget(self.label_image)
        self.setLayout(layout)

    def updateWid(self):
        path = self.image_path + ("d" if not cfg.IS_THEME_DARK else "l") + ".png"
        if os.path.exists(path):
            icon_pixmap = QIcon(path).pixmap(QSize(64, 64))
            self.label_image.setPixmap(icon_pixmap)
        else:
            print(f"Image not found: {path}")
            self.label_image.clear()
