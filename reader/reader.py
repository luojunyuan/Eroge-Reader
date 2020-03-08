from PySide2.QtCore import QUrl, QObject
from PySide2.QtQml import QQmlApplicationEngine

from .le import LocaleEmulator
from .hooker import Hooker
from .game import GameManager

class Reader(QObject):
    def __init__(self):
        super().__init__()

        self.le = LocaleEmulator()
        self.hooker = Hooker()
        self.game = GameManager()


        # Create QML engine
        self.engine = QQmlApplicationEngine()
        self.engine.addImportPath('qrc:reader/ui/modules/')
        # Load the qml file into the engine
        self.engine.load('qrc:reader/ui/main.qml') # is QUrl needed?

        # Qml file error handling
        # assert self.engine.rootObjects(), "unless fail to load main.qml"

        self._connect()

    def _connect(self):
        self.engine.rootObjects()[0].gameStart.connect(self.game.game_start_process)
        self.engine.rootObjects()[0].test.connect(self.qml_button_test)
        self.hooker.onRawTexts.connect(self.test)
        self.hooker.start()
        print('_connect() finish')
    
    def test(self, data):
        print(data.index, data.code, data.text)

    def qml_button_test(self):
        self.hooker.attach(1)