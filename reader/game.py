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

    def open_game(self, retries=2):
        """运行游戏，7秒后再次注入一遍以防附加进程
        
        :param retries: 重试次数, defaults to 2
        :type retries: int, optional
        """
        assert self.path is not None, "No current game path"
    
        def updateLater(verbose=False):
            ret = retries > 0
            if ret:
                if verbose: 
                    print(f'retry {3-retries} times... wait for game to start')
                # QTimer.singleShot(7000, 
                #                 partial(self.open_game, retries=retries-1))
            return ret

        self.proc_name = utils.get_proc_name_by_path(self.path)
        # 程式没有在运行
        if self.proc_name is None:
            pass
            # LocaleEmulator.instace.excute_game_with_le(self.path)

            # self.pids = utils.find_pids(self.proc_name, self.path)
            # if self.pids: 
            #     map(Hooker.instance.attach, pids)
            #     # 找到pid了，但是延迟7秒再次重新获取pid列表注入
            #     if updateLater(): return
            # # 没能找到pid，重新运行LE执行游戏
            # elif updateLater(verbose=True):
            #     return
            # else:
            #     print('Lunch game faied!')
        # （第二次或）程序可能在运行了
        if self.proc_name:
            self.pids = utils.find_all_pids(self.proc_name)
            list(map(Hooker.instance.attach, self.pids))
        return
