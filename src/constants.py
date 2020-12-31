import platform
import os


class Constants:
    OPERATING_SYSTEM = platform.system()
    ACTIVATION_PHRASE = "go to"
    SEPARATOR_WORD = "slash"
    SEPARATOR_CHAR = "\\" if OPERATING_SYSTEM == "Windows" or OPERATING_SYSTEM == "" else "/"
    PROJECT_NAME = "ProjectExplorer"

    # Getting path to project root directory
    path = os.getcwd()
    path = path.split(SEPARATOR_CHAR)
    while path[-1] != PROJECT_NAME:
        path.pop()

    PROJECT_DIRECTORY = SEPARATOR_CHAR.join(path)

    # Gettings drive letters
    dr = [chr(i) for i in range(ord('A'), ord('Z')+1)]
    DRIVES = [d for d in dr if os.path.exists(f'{d}:')]
