# QMainWindow + QPushButton are widget classes
from PySide6.QtWidgets import QMainWindow, QPushButton

# Button class inheriting from QMainWindow
class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Button Holder App")
        # Instance of the button widget
        button = QPushButton("Press Me!")

        # Set up the button as the central widget
        self.setCentralWidget(button)
