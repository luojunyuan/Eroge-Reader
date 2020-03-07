import psutil
from .libs import win32lib

def get_proc_name_by_path(path):
    for pid in win32lib.iterprocess():
        if path == psutil.Process(pid).exe():
            return psutil.Process(pid).name()

def find_all_pids(name: str) -> list:
    """通过进程名获取该进程所有pid
    
    :param name: Process name
    :type name: str
    :return: 某一进程的pid列表
    :rtype: list
    """
    pids_list = []
    for pid in psutil.pids():
        try:
            proc = psutil.Process(pid)
            if proc.name() == name:
                pids_list.append(proc.pid)
        except:
            # ignore NoSuchProcess
            continue
    return pids_list