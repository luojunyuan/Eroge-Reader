import os
import sys

from PySide2.QtWidgets import QApplication
from reader import Reader
import resources  # load resources built by pyside2-rcc

os.environ['QT_QUICK_CONTROLS_STYLE'] = "Universal"

# Create an instance of the application
# QApplication MUST be declared in global scope to avoid segmentation fault
app = QApplication(sys.argv)

reader = Reader()
sys.exit(app.exec_())
