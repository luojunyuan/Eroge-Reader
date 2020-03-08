from .hooker import Hooker
from .le import LocaleEmulator
from . import utils

class GameManager:
    def __init__(self):
        self.pids = []
        self.proc_name = None
        self.path = None
        # self.proc_name_md5 = [""]
        # self.winid = ''

    def game_start_process(self, path):
        self.path = path
        self.open_game()
        print(self.pids, self.proc_name, self.path)
        # send over signal

    def open_game(self):
        """7秒后运行游戏"""
        assert self.path is not None, "No current game path"
    
        self.proc_name = utils.get_proc_name_by_path(self.path)
        if self.proc_name is None:
            LocaleEmulator.instance.excute_game_with_le(self.path)
            # XXX wait 7 seconds
            import time
            from PySide2.QtCore import QTime
            from PySide2.QtWidgets import QApplication
            delay = QTime.currentTime().addSecs(7)
            while QTime.currentTime() < delay:
                QApplication.processEvents()
                time.sleep(0.01)

            self.proc_name = utils.get_proc_name_by_path(self.path)

        self.pids = utils.find_all_pids(self.proc_name)
        list(map(Hooker.instance.attach, self.pids))
