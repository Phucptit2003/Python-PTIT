from langdetect import detect
from gtts import gTTS
import os
import pyttsx3

engine = pyttsx3.init()
def speak(text,lang):
    engine.setProperty('rate',150)
    engine.setProperty('voice',lang)
    engine.say(text)
    engine.runAndWait

text=input()

detect_lang= detect(text)
if detect_lang=='vi':
    speak(text,'vi')
else:
    speak(text,'en')
speak(text,'en')