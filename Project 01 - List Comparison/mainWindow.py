from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QMainWindow, QStackedWidget, QStatusBar, QToolBar, QWidget, QPushButton
from widget import CSVMethod, TextboxMethod
from PySide6.QtGui import QAction

# Class that handles the main window of the application
class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()

        # Initialize window with basic settings
        self.app = app # declare an app member
        self.setWindowTitle("List Comparison Tool")
        self.setGeometry(100, 100, 800, 400)

        # Menu bar settings
        menu_bar = self.menuBar()
        menu_bar.addMenu("Main")
        menu_bar.addMenu("Help")

        # Toolbar Settings
        toolbar = QToolBar("Input Selection")
        self.addToolBar(toolbar)

        # Texbox toolbar button
        textbox_input = QAction("Textbox", self)
        textbox_input.setStatusTip("Paste your list into textboxes")
        textbox_input.triggered.connect(lambda: self.stack.setCurrentIndex(0))
        toolbar.addAction(textbox_input)

        compare_button = QPushButton("Compare the Lists")
        compare_button.setStatusTip("Receive a report comparing the items between your two lists")

        # CSV toolbar button
        csv_input = QAction("CSV", self)
        csv_input.setStatusTip("Drag and drop your CSV files")
        csv_input.triggered.connect(lambda: self.stack.setCurrentIndex(1))
        toolbar.addAction(csv_input)

        # Show the status messages
        self.setStatusBar(QStatusBar(self))

        # Set up the menu for inputting with textboxes
        text_box_method1 = TextboxMethod()
        text_box_method2 = TextboxMethod()
        text_box_view = QWidget() 

        h_layout = QHBoxLayout()
        h_layout.addWidget(text_box_method1)
        h_layout.addWidget(text_box_method2)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(compare_button)
        text_box_view.setLayout(v_layout) # Wraps both into a single widget to add it to the stack

        compare_button.clicked.connect(lambda: list_printer(text_box_method1))

        # Set up the menu for inputting with csv files
        csv_method = CSVMethod()

        # Main layout
        self.stack = QStackedWidget()
        self.stack.addWidget(text_box_view)
        self.stack.addWidget(csv_method)
        self.setCentralWidget(self.stack)

def list_printer(self):
    print(self.text_edit.toPlainText())

def analyze(list_1, list_2):
    overlap = []

    for i in list_1:
        if i in list_2:
            overlap.append(i)

    print(overlap)