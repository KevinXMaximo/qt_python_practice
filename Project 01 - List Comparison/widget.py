from PySide6.QtWidgets import QWidget, QTextEdit, QHBoxLayout, QVBoxLayout, QPushButton

class TextboxMethod(QWidget):
    def __init__(self):
        super().__init__()

        self.text_edit = QTextEdit()

        # Buttons
        paste_button = QPushButton("Paste")
        paste_button.clicked.connect(self.paste) # Go through a custom slot

        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(self.text_edit.clear) 

        h_layout = QHBoxLayout()
        h_layout.addWidget(paste_button)
        h_layout.addWidget(clear_button)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(self.text_edit)

        self.setLayout(v_layout)

    def paste(self):
        self.text_edit.paste()