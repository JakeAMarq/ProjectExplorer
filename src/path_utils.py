import os

SEPARATOR_WORD = "slash"

def remove_spaces(string):
    return "".join(string.split(" "))

def convert_to_snake_case(string):
    return "_".join(string.split(" "))

DIRECTORY_VARIATION_TRANSFORMERS = [lambda x: x, remove_spaces, convert_to_snake_case]

def get_possible_directory_variations(directory):
    return [transform(directory) for transform in DIRECTORY_VARIATION_TRANSFORMERS]

def parse_path(string):
    if not isinstance(string, str):
        raise ValueError("string argument must be a str")

    path = string.lower().replace(SEPARATOR_WORD, "/")
    path = path.replace(" /", "/")
    path = path.replace("/ ", "/")
    return path

def path_exists(path):
    return os.path.exists(path)

def open_path(path):
    path = "C:/" + path
    path = os.path.realpath(path)
    os.startfile(path)  

def convert_list_to_path(list):
    return "/".join(list)

def convert_path_to_list(path):
    return path.split("/")

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
    drive = directories.pop(0)
    validPathVariations = [[drive]]

    if not path_exists(drive):
        return []

    for directory in directories:
        if len(validPathVariations) == 0:
            return []

        possibleVariations = get_possible_directory_variations(directory)

        newValidPathVariations = []
        for path in validPathVariations:
            pathString = convert_list_to_path(path)

            for possibleVariation in possibleVariations:
                possiblePath = pathString + "/" + possibleVariation
                if path_exists(possiblePath):
                    newValidPathVariations.append(path + [possibleVariation])

        validPathVariations = newValidPathVariations[::]


    return [convert_list_to_path(path) for path in validPathVariations]