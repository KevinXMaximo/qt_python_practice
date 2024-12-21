# QApplication handles the main GUI application settings 
from PySide6.QtWidgets import QApplication
# From a separate file import the ButtonHolder class
from button_holder import ButtonHolder
# CLI functionality 
import sys

# Instance of QApplication with a list of command-line arguments
app = QApplication(sys.argv) 

# Instance of the ButtonHolder class
window = ButtonHolder()

# setVisible(true) and Main event loop until exit()
window.show()
app.exec() 