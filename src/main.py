import speech_recognition as sr
from constants import Constants
from path_utils import *


def main():
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
            if voice_input.startswith(Constants.ACTIVATION_PHRASE):
                voice_input = voice_input[len(Constants.ACTIVATION_PHRASE):]
                path = parse_path(voice_input)
                
                try:
                    open_path(path)
                except Exception as exception:
                    print("Exception caught: " + str(exception))
                    
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))


if __name__ == "__main__":
    main()
