from PySide2.QtCore import QUrl, QObject
from PySide2.QtQml import QQmlApplicationEngine

class Reader(QObject):
    def __init__(self):
        super().__init__()

        # Create QML engine
        self.engine = QQmlApplicationEngine()
        # Load the qml file into the engine
        self.engine.load('qrc:reader/ui/main.qml') # is QUrl needed? and QStringLiteral

        # Qml file error handling
        assert self.engine.rootObjects(), "fail to load main.qml"
        #--------------------------------
        # from module.hooker import Hooker
        # from queue import Queue
        # from module.textman import TextManager
        # q = Queue()
        # textprogress = TextManager(q)
        # textractor = Hooker('C:\\Users\\ljy77\\应用\\YUKI\\lib\\textractor\\TextractorCLI.exe', q)
        
        # textractor.attach()


    def _connect(self):
        pass
    