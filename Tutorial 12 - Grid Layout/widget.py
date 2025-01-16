from PySide6.QtWidgets import QWidget, QSizePolicy, QHBoxLayout, QVBoxLayout, QGridLayout, QLineEdit, QPushButton

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QGridLayout Demo")