import speech_recognition as sr
import pyttsx3
from datetime import datetime

r = sr.Recognizer()
#def Begin():
#    engine = pyttsx3.init()
#    engine.say("Good morning master. How may I help you?")
#    engine.runAndWait()

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
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    with sr.Microphone() as source1:
        SpeakText("The time is " +current_time)
        print("The time is ", current_time)
else:
    SpeakText("I am sorry I was unable to understand it. Can you please repeat it?")