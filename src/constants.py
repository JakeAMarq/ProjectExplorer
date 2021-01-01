import platform
import os
import sys


class Constants:

    WINDOWS = "Windows"
    MAC_OS = "Darwin"
    OPERATING_SYSTEM = platform.system()
    ACTIVATION_PHRASE = "go to"
    SEPARATOR_WORD = "slash"
    SEPARATOR_CHAR = "\\" if OPERATING_SYSTEM == WINDOWS else "/"
    PROJECT_NAME = "ProjectExplorer"

    # Getting path to project root directory
    if getattr(sys, "frozen", False):
        # Running as PyInstaller one-folder .exe
        PROJECT_DIRECTORY = sys._MEIPASS
    else:
        # Running from dev environment
        path = os.getcwd()
        path = path.split(SEPARATOR_CHAR)
        while path[-1] != PROJECT_NAME:
            path.pop()
        PROJECT_DIRECTORY = SEPARATOR_CHAR.join(path)

    # Getting drive letters
    dr = [chr(i) for i in range(ord('A'), ord('Z')+1)]
    DRIVES = [d for d in dr if os.path.exists(f'{d}:')]
