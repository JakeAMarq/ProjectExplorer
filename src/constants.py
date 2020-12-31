import platform
from os import getcwd



class Constants:
    OPERATING_SYSTEM = platform.system()
    SEPARATOR_WORD = "slash"
    SEPARATOR_CHAR = "\\" if OPERATING_SYSTEM == "Windows" or OPERATING_SYSTEM == "" else "/"
    PROJECT_NAME = "ProjectExplorer"

    # Getting path to project root directory
    path = getcwd()
    path = path.split(SEPARATOR_CHAR)
    while path[-1] != PROJECT_NAME:
        path.pop()

    PROJECT_DIRECTORY = SEPARATOR_CHAR.join(path)
