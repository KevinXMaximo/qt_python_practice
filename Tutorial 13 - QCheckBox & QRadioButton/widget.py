from PySide6.QtWidgets import QWidget, QCheckBox, QHBoxLayout, QVBoxLayout, QGroupBox

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QCheckBox and QRadioButton")