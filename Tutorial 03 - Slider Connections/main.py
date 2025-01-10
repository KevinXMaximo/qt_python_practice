# QApplication handles the main GUI application settings and QPushButton handles button widgets
from PySide6.QtWidgets import QApplication, QSlider
# Imports core functionalities which in this case will be needed to configure the slider
from PySide6.QtCore import Qt

# Function that prints response message for the slider being moved
def slider_moved(data):
    print("Slider moved to: ", data)

# Creates instances of QApplication
app = QApplication()

# Creates and configures an instance of QSlider
slider = QSlider(Qt.Horizontal)
slider.setMinimum(1)
slider.setMaximum(100)
slider.setValue(25)

# Handles slider movement calling the slider_moved function and passing the int data
slider.valueChanged.connect(slider_moved)

# setVisible(true) and Main event loop until exit()
slider.show()
app.exec()