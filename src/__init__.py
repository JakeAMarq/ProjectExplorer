import logging
import os
import platform
import sys


def get_application_root_path():
    if getattr(sys, "frozen", False):
        # Running as PyInstaller one-folder .exe
        return sys._MEIPASS
    else:
        # Running from dev environment
        path = os.getcwd()
        path = path.split(SEPARATOR_CHAR)
        while path[-1] != PROJECT_NAME:
            path.pop()
        return SEPARATOR_CHAR.join(path)


def get_drive_letters():
    return [d for d in [chr(i) for i in range(ord('A'), ord('Z') + 1)] if os.path.exists(f'{d}:')]


# Defining global constants/objects
WINDOWS = "Windows"
MAC_OS = "Darwin"
OPERATING_SYSTEM = platform.system()
SEPARATOR_CHAR = "\\" if OPERATING_SYSTEM == WINDOWS else "/"
PROJECT_NAME = "ProjectExplorer"
PROJECT_DIRECTORY = get_application_root_path()
DRIVES = get_drive_letters() if OPERATING_SYSTEM == WINDOWS else []

# settings.ini-related constants
SETTINGS_FILE_NAME = "settings.ini"
SETTINGS_SECTION_KEYWORDS = "keywords"
SETTINGS_KEY_ACTIVATION = "activation"
SETTINGS_KEY_SEPARATOR = "separator"
SETTINGS_SECTION_SHORTCUTS = "shortcuts"

# default settings
SETTINGS_DEFAULT_ACTIVATION = "go to"
SETTINGS_DEFAULT_SEPARATOR = "slash"
SETTINGS_DEFAULT_SHORTCUTS = {'Program Files': 'C:\\Program Files\\'}

# global object to read/write settings
from src.usersettings import UserSettings  # importing here bc UserSettings depends on some constants defined above

USER_SETTINGS = UserSettings()

# logging configuration
logs_dir = os.path.join(PROJECT_DIRECTORY, "logs")
if not os.path.exists(logs_dir):
    os.mkdir(logs_dir)
log_file_path = os.path.join(logs_dir, "logs.log")
logging.basicConfig(filename=log_file_path, format="%(asctime)s :: "
                                                   "%(levelname)-8s :: "
                                                   "%(name)s :: "
                                                   "%(funcName)s :: "
                                                   "%(message)s", level=logging.NOTSET)
del logs_dir, log_file_path
