
import os
import pyttsx3
import string

while True:
    you=str(input())
    you=you.lower()
    if "chrome" in you:
        pyttsx3.speak("Open Chrome")
        os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe')
    elif "word" in you:
        pyttsx3.speak("Open Word")
        os.startfile('C:\Program Files\Microsoft Office\\root\Office16\WINWORD')
    elif "excel" in you:
        pyttsx3.speak("Open Excel")
        os.startfile('C:\Program Files\Microsoft Office\\root\Office16\EXCEL')
    elif "powerpoint" in you:
        pyttsx3.speak("Open Powerpoint")
        os.startfile('C:\Program Files\Microsoft Office\\root\Office16\POWERPNT.EXE')
    elif "close" in you:
        pyttsx3.speak("Bye Phuc handsome")
        break;
    else:
        print("Application is not exist. Try again!")
