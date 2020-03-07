import os
import subprocess

RunAsAdmin = 0b1000
RedirectRegistry = 0b0100
IsAdvancedRedirection = 0b0010
RunWithSuspend = 0b0001
guids = {0b0100: '0fdf5139-e69d-4809-b221-7a973527948f',
         0b0010: 'pass',
         0b0001: 'pass'}
default_guid_flag = 0b0100

class LocaleEmulator:

    instance = None

    def __init__(self):
        a = os.environ.get('READER_PATH')
        self.path_of_le = 'C:\\Users\\ljy77\\应用\\LocaleEmulator\\LEProc.exe'
        LocaleEmulator.instance = self

    def excute_game_with_le(self, path, flag=default_guid_flag):
        """
        :param path: Game absolute path
        """
        cmd = [self.path_of_le, '-runas', guids[flag], path]
        subprocess.run(cmd)
