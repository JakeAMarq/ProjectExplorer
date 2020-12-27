import speech_recognition as sr
import os
import re

SEPARATOR_WORD = "slash"

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

def convert_to_snake_case(string):
    return "_".join(string.split(" "))

def remove_spaces(string):
    return "".join(string.split(" "))

def get_possible_directory_variations(directory):
    return [directory, remove_spaces(directory), convert_to_snake_case(directory)]

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

def main():
    while (True):
        # obtain audio from the microphone
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = recognizer.listen(source)

        # recognize speech using Google Speech Recognition
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            voiceInput = recognizer.recognize_google(audio)
            print("Google Speech Recognition thinks you said " + voiceInput)
            if (voiceInput.startsWith("go to")):
                path = parse_path(voiceInput[6:])
                open_path(path)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

main()
# testcases = ["c: slash program files slash riot games", None, "", "c: idk", "c: slash idk"]

# for case in testcases:
#     print("Input: " + str(case))
#     try:
#         print("Output: " + str(get_valid_path_variations(parse_path(case))))
#     except ValueError as error:
#         print("Error raised: " + str(error))
