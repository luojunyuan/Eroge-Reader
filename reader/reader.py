from PySide2.QtCore import QUrl, QObject
from PySide2.QtQml import QQmlApplicationEngine

class Reader(QObject):
    def __init__(self):
        super().__init__()

        # Create QML engine
        self.engine = QQmlApplicationEngine()
        # Load the qml file into the engine
        self.engine.load('qrc:reader/ui/main.qml') # is QUrl needed? and QStringLiteral
        # self.engine.load('qrc:reader/ui/attachWindow.qml')

        # Qml file error handling
        assert self.engine.rootObjects(), "unless fail to load main.qml"

    def _connect(self):
        pass
    