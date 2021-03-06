import speech_recognition as sr
import time
from gtts import gTTS
import os
import threading
import sys
from env import WIT_AI_KEY

sys.stderr = object


def handler(response):

    if response.startswith("clock"):
        tts = gTTS(text='Yes?', lang='en')
        tts.save("hey.mp3")
        os.system("mpg123 hey.mp3")
        os.system("rm hey.mp3")


def speech():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Say something!")
        audio = r.listen(source)

    try:

        resp = r.recognize_wit(audio, key=WIT_AI_KEY)

        print("Wit.ai thinks you said " + resp)
        handler(resp)
        speech()

    except sr.UnknownValueError:

        print("Wit.ai could not understand audio")

    except sr.RequestError as e:

        print("Could not request results from Wit.ai service; {0}".format(e))


def run():
    print("yo") 


thread1 = threading.Thread(name='speech', target=speech)
thread2 = threading.Thread(name='run', target=run)

thread1.start()
thread2.start()
