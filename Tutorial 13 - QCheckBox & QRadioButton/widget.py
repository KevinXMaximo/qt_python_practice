from PySide6.QtWidgets import QWidget, QCheckBox, QHBoxLayout, QVBoxLayout, QGroupBox

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QCheckBox and QRadioButton")

        # Checkboxes: operating system
        os = QGroupBox("Choose operating system")
        windows = QCheckBox("Windows")
        windows.toggled.connect(self.windows_box_toggled)

        linux = QCheckBox("Linux")
        linux.toggled.connect(self.linux_box_toggled)

        mac = QCheckBox("Mac")
        mac.toggled.connect(self.mac_box_toggled)

        os_layout = QVBoxLayout()
        os_layout.addWidget(windows)
        os_layout.addWidget(linux)
        os_layout.addWidget(mac)
        os.setLayout(os_layout)

        layout = QVBoxLayout()
        layout.addWidget(os)

        self.setLayout(layout)
