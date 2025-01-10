from PySide6.QtWidgets import QHBoxLayout, QPushButton, QTextEdit, QVBoxLayout, QWidget

# Class that handles lists being inputted through text pasted or typed into textboxes
class TextboxMethod(QWidget):
    def __init__(self):
        super().__init__()

        self.text_edit = QTextEdit()

        # Buttons
        paste_button = QPushButton("Paste")
        paste_button.clicked.connect(self.paste) # Go through a custom slot

        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(self.text_edit.clear) 

        # Widget Layout
        h_layout = QHBoxLayout()
        h_layout.addWidget(paste_button)
        h_layout.addWidget(clear_button)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(self.text_edit)

        self.setLayout(v_layout)

    # Custom function for pasting text
    def paste(self):
        self.text_edit.paste()

# Class that handles lists being inputted through drag-and-drop csv files
class CSVMethod(QWidget):
    def __init__(self):
        super().__init__()