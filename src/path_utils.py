import os
import subprocess
from constants import Constants

DIRECTORY_VARIATION_TRANSFORMERS = [lambda dir: dir,                        # no variation
                                    lambda dir: "".join(dir.split(" ")),    # remove spaces
                                    lambda dir: "_".join(dir.split(" ")),   # separate with underscores
                                    lambda dir: "-".join(dir.split(" "))]   # separate with hyphens


def get_possible_directory_variations(directory):
    if directory.find(" ") < 0: 
        return [directory]

    return [transform(directory) for transform in DIRECTORY_VARIATION_TRANSFORMERS]


def parse_path(string):
    if not isinstance(string, str):
        raise ValueError("string argument must be a str")

    path = string.lower().replace(Constants.SEPARATOR_WORD, Constants.SEPARATOR_CHAR)
    path = path.replace(" " + Constants.SEPARATOR_CHAR, Constants.SEPARATOR_CHAR)
    path = path.replace(Constants.SEPARATOR_CHAR + " ", Constants.SEPARATOR_CHAR)
    return path


def path_exists(path):
    return (os.path.exists(path) or 
    os.path.exists(Constants.SEPARATOR_CHAR + path + Constants.SEPARATOR_CHAR) or
    os.path.exists(Constants.SEPARATOR_CHAR + path) or
    os.path.exists(path + Constants.SEPARATOR_CHAR))


def open_path(path):
    path = os.path.realpath(path)
    if Constants.OPERATING_SYSTEM == "Windows":
        os.startfile(path)
    elif Constants.OPERATING_SYSTEM == "Darwin":
        subprocess.Popen(["open", path])
    else:
        subprocess.Popen(["xdg-open", path])


def convert_list_to_path(list):
    return Constants.SEPARATOR_CHAR.join(list)


def convert_path_to_list(path):
    return path.split(Constants.SEPARATOR_CHAR)


def get_valid_path_variations(path):
    """
    Given a path, returns a list of paths found in the file system that either
    exactly match the given path or match the path after applying common directory naming conventions

    Keyword arguments:
    path -- the path (string)
    """

    if not isinstance(path, str):
        raise ValueError("path argument must be a str")

    if path == "":
        raise ValueError("path argument cannot be an empty str")

    directories = convert_path_to_list(path)

    root = ""
    while root == "":
        root = directories.pop(0)

    if Constants.OPERATING_SYSTEM != "Windows":
        root = "/" + root

    valid_path_variations = [[root]]

    if not path_exists(root):
        return []

    for directory in directories:
        if len(valid_path_variations) == 0:
            return []

        possible_variations = get_possible_directory_variations(directory)

        new_valid_path_variations = []
        for path in valid_path_variations:
            path_string = convert_list_to_path(path)

            for possibleVariation in possible_variations:
                possible_path = path_string + Constants.SEPARATOR_CHAR + possibleVariation
                if path_exists(possible_path):
                    new_valid_path_variations.append(path + [possibleVariation])

        valid_path_variations = new_valid_path_variations[::]

    return [convert_list_to_path(path) for path in valid_path_variations]
