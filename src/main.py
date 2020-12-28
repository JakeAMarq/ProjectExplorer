import speech_recognition as sr
import re
from path_utils import *

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
