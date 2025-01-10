from PySide6.QtWidgets import QMainWindow, QToolBar, QPushButton, QStatusBar
from PySide6.QtGui import QAction
from widget import TextboxMethod

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app # declare an app member
        self.setWindowTitle("List Comparison Tool")
        self.setGeometry(100, 100, 800, 600)

        # Menu bar and menus
        menu_bar = self.menuBar()
        main_menu = menu_bar.addMenu("Main")
        help_menu = menu_bar.addMenu("Help")

        # Working with toolbars
        toolbar = QToolBar("Input Selection")
        self.addToolBar(toolbar)

        # Add quit action to toolbar
        textbox_input = QAction("Textbox Input", self)
        textbox_input.setStatusTip("Paste your list into textboxes")
        #textbox_input.triggered.connect(self.toolbar_button_click)
        textbox_input.setCheckable(True)
        toolbar.addAction(textbox_input)

        csv_input = QAction("CSV input", self)
        csv_input.setStatusTip("Drag and drop your csv files")
        #csv_input.triggered.connect(self.toolbar_button_click)
        csv_input.setCheckable(True)
        toolbar.addAction(csv_input)

        # Working with status bars
        self.setStatusBar(QStatusBar(self))

        TextBoxMethod = TextboxMethod()
        self.setCentralWidget(TextBoxMethod)