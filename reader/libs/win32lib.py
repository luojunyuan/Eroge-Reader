import win32gui
import win32process

def _candidate_hwnd_callback(hwnd, lParam):
    """Only called by iterprocess()"""
    lParam.append(hwnd)

def iterprocess():
    """Generator of candidate process pid

    :yield: ProcessObject
    """
    hwnd_list = []
    win32gui.EnumWindows(_candidate_hwnd_callback, hwnd_list)
    for hwnd in hwnd_list:
        _, pid = win32process.GetWindowThreadProcessId(hwnd)

        yield pid
