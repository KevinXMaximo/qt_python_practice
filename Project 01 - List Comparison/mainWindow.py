from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QMainWindow, QStackedWidget, QStatusBar, QToolBar, QWidget, QPushButton, QLabel
from widget import CSVMethod, TextboxMethod
from PySide6.QtGui import QAction, Qt

# Class that handles the main window of the application
class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()

        # Initialize window with basic settings
        self.app = app # declare an app member
        self.setWindowTitle("List Comparison Tool")
        self.setGeometry(100, 100, 800, 400)

        # Label for displaying analysis results
        self.analysis_label = QLabel(self)
        self.analysis_label.setText("\nAnalysis Results:")
        self.analysis_label.setWordWrap(True) # for multi-line results

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
        compare_button.setFixedWidth(300)
        compare_button.setStatusTip("Receive a report comparing the items between your two lists")

        invisible_offset = QWidget()

        # CSV toolbar button
        csv_input = QAction("CSV", self)
        csv_input.setStatusTip("Drag and drop your CSV files")
        csv_input.triggered.connect(lambda: self.stack.setCurrentIndex(1))
        toolbar.addAction(csv_input)

        # Show the status messages
        self.setStatusBar(QStatusBar(self))

        # Set up the menu for inputting with textboxes
        text_box_method1 = TextboxMethod()
        text_box_method1.text_edit.setPlaceholderText("ex: toast milk sour-cream avocado soda ramen")
        text_box_method2 = TextboxMethod()
        text_box_method2.text_edit.setPlaceholderText("ex: avocado milk ramen toast")
        text_box_view = QWidget() 

        v_layout1 = QVBoxLayout()
        v_layout1.addWidget(text_box_method1)
        v_layout1.addWidget(compare_button)
        v_layout1.setAlignment(Qt.AlignTop)

        v_layout2 = QVBoxLayout()
        v_layout2.addWidget(text_box_method2)
        v_layout2.addWidget(invisible_offset)
        v_layout2.setAlignment(Qt.AlignTop)

        h_layout1 = QHBoxLayout()
        h_layout1.addLayout(v_layout1)
        h_layout1.addLayout(v_layout2)

        h_layout2 = QHBoxLayout()
        h_layout2.addWidget(self.analysis_label)
        h_layout2.setAlignment(Qt.AlignTop)

        v_layout_main = QVBoxLayout()
        v_layout_main.addLayout(h_layout1)
        v_layout_main.addLayout(h_layout2)
        v_layout_main.setAlignment(Qt.AlignTop)

        text_box_view.setLayout(v_layout_main) # Wraps both into a single widget to add it to the stack

        compare_button.clicked.connect(lambda: self.analyze(text_box_method1, text_box_method2))

        # Set up the menu for inputting with csv files
        csv_method = CSVMethod()

        # Main layout
        self.stack = QStackedWidget()
        self.stack.addWidget(text_box_view)
        self.stack.addWidget(csv_method)
        self.setCentralWidget(self.stack)

    def analyze(self, text_box_method1, text_box_method2):
        list1 = text_box_method1.text_edit.toPlainText().split()
        list2 = text_box_method2.text_edit.toPlainText().split()

        overlap = determine_overlap(list1, list2)
        overlap_str = ", ".join(overlap) # Treat the overlap list so that the items are displayed correctly

        percentage = round(len(overlap)/len(list1) * 100, 2)

        self.analysis_label.setText(f"Analysis Results:\n\n{percentage}% of the first list is also present in the second list ({len(overlap)} items).\n\nThe overlapped items are as follows: \n\n {overlap_str}")

def determine_overlap(list_1, list_2):
    overlap = []

    for i in list_1:
        if i in list_2:
            overlap.append(i)

    return overlap