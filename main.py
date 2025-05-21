from src.ui import main_window
from PyQt6.QtWidgets import QApplication
import sys
from PyQt6.QtGui import QIcon, QFont


def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setWindowIcon(QIcon.fromTheme("preferences-system"))
    app.setFont(QFont("Arial", 10))
    
    window = main_window.MainWindow()
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()