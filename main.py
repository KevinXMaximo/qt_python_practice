# QApplication handles the main GUI application settings and QMainWindow + QPushButton are widget classes
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton 

# Commandline functionality
import sys 

# Instance of QApplication with a list of command-line arguments
app = QApplication(sys.argv) 

# Instance of the MainWindow widget
window = QMainWindow()
window.setWindowTitle("My first MainWindow app")

# Instance of the button widget
button = QPushButton()
button.setText("Press me")

# Attatches button widget to the window
window.setCentralWidget(button)

# setVisible(true) and Main event loop until exit()
window.show()
app.exec() 