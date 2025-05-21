from PyQt6.QtWidgets import QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QMovie
from PyQt6.QtCore import Qt


class GifViewer(QWidget):
    def __init__(self, gif_path: str=""):
        super().__init__(gif_path)
        self.gif_path = gif_path
        self.initUI()

    def initUI(self):
        # Ana düzen
        layout = QVBoxLayout(self)

        # QLabel oluştur
        self.gifLabel = QLabel(self)
        self.gifLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # QMovie ile GIF yükle
        self.movie = QMovie(self.gif_path)  # Buraya GIF dosyasının yolunu yazın
        self.gifLabel.setMovie(self.movie)

        # GIF'i oynat
        self.movie.start()

        # QLabel'i düzen içine ekle
        layout.addWidget(self.gifLabel)
        self.setLayout(layout)
