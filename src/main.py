import speech_recognition as sr
import os
import re

def parsePath(string):
    wordList = re.sub("[^\w]", " ",  string).split()
    wordList = wordList[2:]
    for word in wordList:
        if (word == "slash"):
            word = "/"
    return wordList.join()

def openPath(path):
    path = "C:/" + path
    path = os.path.realpath(path)
    os.startfile(path)  

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
                path = parsePath(voiceInput)
                openPath(voiceInput)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

main()