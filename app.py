import speech_recognition as sr
import pyttsx3
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
r = sr.Recognizer()

engine = pyttsx3.init()
if('5:00:00'<current_time<'12:00:00'):
    engine.say("Good morning master. How may I help you?")
elif('12:00:01'<current_time<'17:00:00'):
    engine.say("Good afternoon master. How may I help you?")
elif('17:00:01'<current_time<'20:00:00'):
    engine.say("Good evening master. How may I help you?")
else:
    engine.say("Yes master. How may I help you?")
engine.runAndWait()

def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=0.2)
    audio = r.listen(source)
    MyText = r.recognize_google(audio,language="en-in")
    MyText=MyText.lower()
    print(MyText)
            
if(MyText=='time'):
    with sr.Microphone() as source1:
        SpeakText("The time is " +current_time)
        print("The time is ", current_time)
else:
    SpeakText("I am sorry I was unable to understand it. Can you please repeat it?")
    SpeakText()