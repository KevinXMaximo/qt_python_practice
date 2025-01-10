from PySide6.QtWidgets import QApplication, QWidget
from rockwidget import RockWidget

import sys
app = QApplication(sys.argv)

widget = RockWidget()
widget.show()

app.exec()