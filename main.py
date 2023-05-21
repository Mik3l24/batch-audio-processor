from app import MainWindow
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    print("placeholderowy main")
    # Run app
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()

