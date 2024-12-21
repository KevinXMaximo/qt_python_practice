# QApplication handles the main GUI application settings and QMainWindow + QPushButton are widget classes
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
# CLI functionality 
import sys

# Button class inheriting from QMainWindow
class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Button Holder App")
        # Instance of the button widget
        button = QPushButton("Press Me!")

        # Set up the button as the central widget
        self.setCentralWidget(button)

# Instance of QApplication with a list of command-line arguments
app = QApplication(sys.argv) 

# Instance of the ButtonHolder class
window = ButtonHolder()

# setVisible(true) and Main event loop until exit()
window.show()
app.exec() 