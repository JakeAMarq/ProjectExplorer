from src import *
import logging
import os
import subprocess

logger = logging.getLogger(__name__)


def parse_path(string):
    if not isinstance(string, str):
        logger.error("parse_path :: non-str argument given")
        return ""

    path = string.strip()
    path = path.lower().replace(USER_SETTINGS.get(SETTINGS_SECTION_KEYWORDS, SETTINGS_KEY_SEPARATOR), SEPARATOR_CHAR)
    path = path.replace("/", SEPARATOR_CHAR)
    path = path.replace("\\", SEPARATOR_CHAR)
    path = path.replace(" " + SEPARATOR_CHAR, SEPARATOR_CHAR)
    path = path.replace(SEPARATOR_CHAR + " ", SEPARATOR_CHAR)

    path = path.split(SEPARATOR_CHAR)

    if DRIVES.count(path[0].upper()) > 0:
        path[0] = path[0] + ":"

    return SEPARATOR_CHAR.join(path)


def open_path(path):
    path = os.path.realpath(path)
    if OPERATING_SYSTEM == WINDOWS:
        os.startfile(path)
    elif OPERATING_SYSTEM == MAC_OS:
        subprocess.Popen(["open", path])
    else:
        subprocess.Popen(["xdg-open", path])


def convert_list_to_path(list):
    return SEPARATOR_CHAR.join(list)


def convert_path_to_list(path):
    return path.split(SEPARATOR_CHAR)


DIRECTORY_VARIATION_TRANSFORMERS = [lambda dir: dir,                        # no variation
                                    lambda dir: "".join(dir.split(" ")),    # remove spaces
                                    lambda dir: "_".join(dir.split(" ")),   # separate with underscores
                                    lambda dir: "-".join(dir.split(" "))]   # separate with hyphens


def get_possible_directory_variations(directory):
    if directory.find(" ") < 0:
        return [directory]

    return [transform(directory) for transform in DIRECTORY_VARIATION_TRANSFORMERS]


def get_valid_path_variations(path):
    """
    Given a path, returns a list of paths found in the file system that either
    exactly match the given path or match the path after applying common directory naming conventions

    Keyword arguments:
    path -- the path (string)
    """

    if not isinstance(path, str):
        logger.error("get_valid_path_variations :: non-str argument given")
        return []

    if path == "":
        logger.error("get_valid_path_variations :: empty str argument given")
        raise []

    directories = convert_path_to_list(path)

    root = ""
    while root == "":
        root = directories.pop(0)

    if OPERATING_SYSTEM != "Windows":
        root = "/" + root

    valid_path_variations = [[root]]

    if not os.path.exists(root):
        return []

    for directory in directories:
        if len(valid_path_variations) == 0:
            return []

        possible_variations = get_possible_directory_variations(directory)

        new_valid_path_variations = []
        for path in valid_path_variations:
            path_string = convert_list_to_path(path)

            for possibleVariation in possible_variations:
                possible_path = path_string + SEPARATOR_CHAR + possibleVariation
                if os.path.exists(possible_path):
                    new_valid_path_variations.append(path + [possibleVariation])

        valid_path_variations = new_valid_path_variations[::]

    return [convert_list_to_path(path) for path in valid_path_variations]
