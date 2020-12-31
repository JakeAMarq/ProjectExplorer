# import speech_recognition as sr
# from constants import Constants
# from path_utils import *
#
#
#
# def main():
#     while True:
#         # obtain audio from the microphone
#         recognizer = sr.Recognizer()
#         with sr.Microphone() as source:
#             print("Say something!")
#             audio = recognizer.listen(source)
#
#         # recognize speech using Google Speech Recognition
#         try:
#             # for testing purposes, we're just using the default API key
#             # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
#             # instead of `r.recognize_google(audio)`
#             voice_input = recognizer.recognize_google(audio).lower()
#             print("Google Speech Recognition thinks you said: \"" + voice_input + "\"")
#             if voice_input.startswith(Constants.ACTIVATION_PHRASE):
#                 voice_input = voice_input[len(Constants.ACTIVATION_PHRASE):]
#                 path = parse_path(voice_input)
#
#                 try:
#                     open_path(path)
#                 except Exception as exception:
#                     print("Exception caught: " + str(exception))
#
#         except sr.UnknownValueError:
#             print("Google Speech Recognition could not understand audio")
#         except sr.RequestError as e:
#             print("Could not request results from Google Speech Recognition service; {0}".format(e))
from src.constants import Constants
from infi.systray import SysTrayIcon

application_icon_path = f"{Constants.PROJECT_DIRECTORY}{Constants.SEPARATOR_CHAR}icons{Constants.SEPARATOR_CHAR}python_icon.ico"


def hello(sys_tray_icon):
    print("Hello World.")


def example_setting_1(sys_tray_icon):
    print("Example setting 1 clicked")


def example_setting_2(sys_tray_icon):
    print("Example setting 2 clicked")


def exit_application(sys_tray_icon):
    # Whatever we need to take care of before application exits
    exit()


def do_nothing(sys_tray_icon):
    pass


def main():
    menu_options = (('Say Hello', application_icon_path, hello),
                    (
                    "Settings", application_icon_path, (("Example setting 1", application_icon_path, example_setting_1),
                                                        ("Example setting 2", application_icon_path, example_setting_2),
                                                        ))
                    )

    sysTrayIcon = SysTrayIcon(application_icon_path, Constants.PROJECT_NAME,
                              menu_options, on_quit=exit_application, default_menu_index=1)
    sysTrayIcon.start()


if __name__ == "__main__":
    main()
