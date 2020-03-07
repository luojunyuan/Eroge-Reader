from subprocess import Popen, PIPE
from threading import Thread

from PySide2.QtCore import Signal, QObject

CRLF = '\r\n'


class TextObject:
    def __init__(self, line: str):
        self.index = -1
        self.code = ''
        self.text = ''
        self._data_cleansing(line.replace('\n', ''))

    def _data_cleansing(self, line: str):
        line = line.split('] ')

        handle = line[0].replace('[', '')
        self.text = line[-1]

        l = handle.split(':')
        self.index = index = l[0]
        self.code = ('/'+l[6]+':'+l[7]) if index != '0' and index != '1' else l[5]


class Hooker(QObject, Thread):
    """生成一个textractor脚手架进程
    
    可以根据pid附加入单个进程，或脱离单个进程，或指定hcode或rcode注入某一进程
    """
    instance = None
    onRawTexts = Signal(TextObject)

    def __init__(self):
        QObject.__init__(self)
        Thread.__init__(self)

        path = 'C:\\Users\\ljy77\\应用\\YUKI\\lib\\textractor\\TextractorCLI.exe'
        self.cli = Popen(path, encoding='utf-16-le', text=True, 
                        stdin=PIPE, stdout=PIPE, stderr=PIPE)
        Hooker.instance = self

    def run(self):
        """Start send raw text datas"""
        while self.cli.poll() is None:
            line = self.cli.stdout.readline()
            # FIXME 当剪切板出现以下情况，会导致错误
            if line.find('[') != 0:
                continue
            data = TextObject(line)
            self.onRawTexts.emit(data)
            
    def attach(self, pid: int) -> None:
        self.cli.stdin.write('attach -P' + str(pid) + CRLF)
        self.cli.stdin.flush()

    def detach(self, pid: int) -> None:
        self.cli.stdin.write('detach -P' + str(pid) + CRLF)
        self.cli.stdin.flush()

    def inject(self, pid: int, hookcode: str) -> None:
        self.cli.stdin.write(hookcode + ' -P' + str(pid) + CRLF)
        self.cli.stdin.flush()
