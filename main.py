import os
import sys

from PySide2.QtWidgets import QApplication

from reader import Reader
import resources  # load resources built by pyside2-rcc

if __name__ == "__main__":

    root_dir = os.path.dirname(os.path.realpath(__file__))
    pro_dir = root_dir + '\\reader'
    os.environ['READER_PATH'] = pro_dir
    # os.environ["QT_QUICK_CONTROLS_CONF"] = os.path.join(
    #     root_dir, "qmlTest01", "qtquickcontrols2.conf"
    # )
    # os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    os.environ['QT_QUICK_CONTROLS_STYLE'] = "Universal"

    # Create an instance of the application
    # QApplication MUST be declared in global scope to avoid segmentation fault
    app = QApplication(sys.argv)

    reader = Reader()
    sys.exit(app.exec_())
