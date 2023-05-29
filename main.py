import sys

from app import MainWindow
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication()

    window = MainWindow()
    window.resize(800, 600)
    window.show()

    sys.exit(app.exec())

