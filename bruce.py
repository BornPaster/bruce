import os, ctypes
from datetime import datetime
import logging
import time


def _consolestamp(): # console timestamp (monochrome, white numbers and dark grey brackets)
    timestamp = str(datetime.fromtimestamp(time.time())).split(" ")[1]
    white_dots_and_colons = "\x1b[38;2;73;73;73m.\x1b[0m"
    white_colons = "\x1b[38;2;73;73;73m:\x1b[0m"
    formatted_timestamp = timestamp.replace(".", white_dots_and_colons).replace(":", white_colons)
    return f'\x1b[38;2;73;73;73m[\x1b[0m{formatted_timestamp}\x1b[38;2;73;73;73m]\x1b[0m '


def bracks(text): # brackets (monochrome)
    return f'\x1b[38;2;73;73;73m[\x1b[0m {text} \x1b[38;2;73;73;73m]\x1b[0m '


def init(): # initialize bruce to show ascii colors in terminal properly
    if os.name == 'nt':
        kernel32 = ctypes.windll.kernel32
        handle = kernel32.GetStdHandle(-11)
        mode = ctypes.c_ulong()
        kernel32.GetConsoleMode(handle, ctypes.byref(mode))
        mode.value |= 0x0004
        kernel32.SetConsoleMode(handle, mode)


class bruceformatter(logging.Formatter): # custom modified formatter to tranform terminal output
    def format(self, record):
        stamp = _consolestamp()
        original = super().format(record)
        return f"{stamp}  \x1b[38;2;73;73;73m-\x1b[0m  {original}"
