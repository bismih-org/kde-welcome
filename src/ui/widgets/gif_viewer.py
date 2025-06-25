from PyQt6.QtWidgets import QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QMovie
from PyQt6.QtCore import Qt


class GifViewer(QWidget):
    def __init__(self, gif_path: str="", fixed_size=(300, 300)):
        super().__init__()
        self.gif_path = gif_path
        self.initUI()
        self.setFixedSize(*fixed_size)
        if self.gif_path:
            self.set_gif_size(*fixed_size)
        

    def set_gif_size(self, width, height):
        """GIF'i kırpmadan boyutlandır"""
        if hasattr(self, 'movie'):
            # Orijinal boyutları al
            original_size = self.movie.scaledSize()
            if original_size.isEmpty():
                original_size = self.movie.currentImage().size()
            
            # Aspect ratio'yu koru
            scaled_size = original_size.scaled(width, height, Qt.AspectRatioMode.KeepAspectRatio)
            self.movie.setScaledSize(scaled_size)
            self.gifLabel.setFixedSize(scaled_size)
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
