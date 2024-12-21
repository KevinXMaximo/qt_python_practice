# QApplication handles the main GUI application settings and QWidget is the base class for all user interface objects
from PySide6.QtWidgets import QApplication, QWidget 

# Commandline functionality
import sys 

# Instance of QApplication with a list of command-line arguments
app = QApplication(sys.argv) 

# Instance of the Qwidget class for the user interface and setVisible(true)
window = QWidget() 
window.show() 

# Main event loop until exit()
app.exec() 