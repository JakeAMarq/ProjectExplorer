from infi.systray import SysTrayIcon
from sys import exit
from src.constants import Constants
from src.path_utils import *
import logging
import os
import speech_recognition as sr

# logging configuration
logs_dir = os.path.join(Constants.PROJECT_DIRECTORY, "logs")
if not path_exists(logs_dir):
    os.mkdir(logs_dir)
log_file_path = os.path.join(logs_dir, "logs.log")
logging.basicConfig(filename=log_file_path, format="%(asctime)s :: "
                                                   "%(levelname)-8s :: "
                                                   "%(name)s :: "
                                                   "%(funcName)s :: "
                                                   "%(message)s", level=logging.NOTSET)

logger = logging.getLogger(__name__)


def hello(sys_tray_icon):
    print("Hello World.")


def example_setting_1(sys_tray_icon):
    print("Example setting 1 clicked")


def example_setting_2(sys_tray_icon):
    print("Example setting 2 clicked")


def exit_application(sys_tray_icon):
    # Whatever we need to take care of before application exits
    logger.info("Exiting application")
    exit()


def do_nothing(sys_tray_icon):
    pass


def process_input(voice_input):
    path = parse_path(voice_input)

    if not path_exists(path):
        path_variations = get_valid_path_variations(path)
        if len(path_variations) == 0:
            logger.info(f"Could not find any valid paths for: \"{voice_input}\"")
            return
        path = path_variations[0]

    try:
        open_path(path)
    except Exception as exception:
        print("Exception caught attempting to open path: " + str(exception))
        logger.error("Exception caught attempting to open path: " + str(exception))


def listen():
    logger.info("Listening...")
    while True:
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
            voice_input = recognizer.recognize_google(audio).lower()
            print("Google Speech Recognition thinks you said: \"" + voice_input + "\"")
            logger.info("Google Speech Recognition thinks you said: \"" + voice_input + "\"")
            if voice_input.startswith(Constants.ACTIVATION_PHRASE):
                process_input(voice_input[len(Constants.ACTIVATION_PHRASE):])

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            logger.error("Could not request results from Google Speech Recognition service; {0}".format(e))


def main():
    try:
        logger.info("Application started")

        application_icon_path = os.path.join(Constants.PROJECT_DIRECTORY, "icons", "python_icon.ico")
        menu_options = (('Say Hello', application_icon_path, hello),
                        (
                            "Settings", application_icon_path,
                            (("Example setting 1", application_icon_path, example_setting_1),
                             ("Example setting 2", application_icon_path, example_setting_2),
                             ))
                        )

        sys_tray_icon = SysTrayIcon(application_icon_path, Constants.PROJECT_NAME,
                                    menu_options, on_quit=exit_application, default_menu_index=1)
        sys_tray_icon.start()

        listen()

    except Exception as exception:
        logger.critical("Application crashed\nException:\n" + str(exception))
        exit_application(None)


if __name__ == "__main__":
    main()
