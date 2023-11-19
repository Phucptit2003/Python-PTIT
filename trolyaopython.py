import os

import speech_recognition
import pyttsx3
from datetime import date
from datetime import datetime

robot_mouth=pyttsx3.init()
robot_ear=speech_recognition.Recognizer()
robot_brain=""
while True:
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm listening")
        audio= robot_ear.listen(mic)

    print("Robot: ...")
    try:
        you=robot_ear.recognize_google(audio)
    except:
        you=""

    print("You: " + you)

    if you=="":
        robot_brain="I can't hear you, try again"
    elif you=="hello":
        robot_brain="Hello Phuc handsome"
    elif you=="what is the day today":
        today = date.today()
        robot_brain= today.strftime("%B %d, %Y")
    elif you=="what time is it":
        now=datetime.now()
        robot_brain=now.strftime("%H hours %M minutes %S seconds")
    elif "lovely" in you:
        robot_brain="Xuan"
    elif "morning" in you:
        robot_brain="Good morning, Phuc. Have a good day!"
    elif "tired" in you:
        robot_brain="You should go to the doctor and buy some medicine and you should rest more"
    elif "secretly" in you:
        robot_brain="Nobody :("
    elif "girlfriend" in you:
        robot_brain="Do you have a girlfriend ?.Lew lew"
        print("Robot: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    elif "bye" in you:
        robot_brain="Bye Phuc handsome"
        print("Robot: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    else:
        robot_brain="I'm fine. Thank you. And you"
    print("Robot: " + robot_brain)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()