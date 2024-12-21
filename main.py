from PySide6.QtWidgets import QApplication, QWidget # QApplication handles the main GUI application settings and QWidget is the base class for all user interface objects

import sys # For commandline functionality

app = QApplication(sys.argv) # Creates an instance of QApplication with a list of command-line arguments

window = QWidget() # Creates an instance of the Qwidget class for the user interface 
window.show() # setVisible(true)

app.exec() # Starts main event loop until exit()