# QApplication handles the main GUI application settings and QPushButton handles button widgets
from PySide6.QtWidgets import QApplication, QPushButton

# Function that prints response message for button click
def button_clicked(data):
    print("You clicked the button. Checked: ", data)

# Creates instances of QApplication and QPushButton
app = QApplication()
button = QPushButton("Press me")

# Makes it so button works like a checkbox, starting out as False (unchecked)
button.setCheckable(True)

# Handles button click calling the button_clicked function and passing the boolean data
button.clicked.connect(button_clicked)

# setVisible(true) and Main event loop until exit()
button.show()
app.exec()