from PySide6.QtWidgets import QApplication, QPushButton

def button_clicked():
    print("You clicked the button")

app = QApplication()
button = QPushButton("Press me")

button.clicked.connect(button_clicked)

button.show()
app.exec()