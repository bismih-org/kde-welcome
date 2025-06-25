from PyQt6.QtWidgets import (
    QMainWindow,
    QPushButton,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QStackedWidget,
    QFrame,
    QSizePolicy,
)
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt, QSize
from src.ui.widgets.BLabel import BLabel
from src.ui.widgets.gif_viewer import GifViewer

class TerminalComp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

        

    def initUI(self):
        # Ana düzen oluşturma
        mainLayout = QVBoxLayout(self)
        # mainLayout.setSpacing(0)
        mainLayout.setContentsMargins(20, 20, 20, 20)

        title = BLabel("Bir çok işinizi terminal ile daha görsel bir şekilde yapabilirsiniz", is_bold=True)
        gif_terminal = GifViewer("data/gifs/terminal.gif", fixed_size=(400, 400))
        mainLayout.addWidget(title, alignment=Qt.AlignmentFlag.AlignCenter)
        mainLayout.addWidget(gif_terminal, alignment=Qt.AlignmentFlag.AlignCenter)

        desc = """
Terminalde yapılabilecek işlemler:
- cd ile klasörler arasında gezinme
- up ile sistem depo güncelleme
- ... nokta sayısı kadar geri gitme
- uU birimden yapılan işlemin süresini görme
- Aliaslar için tamamlama desteği
- Eski yazılanı hatırlayıp geri getirme
- Uç birimi başlatmak Ctrl + Alt + T tuş kombinasyonunu kullanabilirsiniz
- Shift + Ctrl + 8 ile uç birim dikeyde ikiye bölünebilir
- Shift + Ctrl + 9 ile uç birim yatayda ikiye bölünebilir
- Shift + Ctrl + T ile uç birim yen sekme açılabilir
- Daha fazla detay için terminalden z yazıp .bashrc içine bakabilirsiniz.
"""

        lb_desc = BLabel(desc, alignment="Left", is_bold=False)
        # lb_desc.setWordWrap(True)
        mainLayout.addWidget(lb_desc, alignment=Qt.AlignmentFlag.AlignLeft)


        self.setLayout(mainLayout)

    def updateWid(self):
        pass