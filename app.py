import speech_recognition as sr
import pyttsx3
from datetime import datetime
import requests
from bs4 import BeautifulSoup
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
    MySpeech = r.recognize_google(audio,language="en-in")
    MySpeech=MySpeech.lower()
    print(MySpeech)
            
if "time" in MySpeech:
    with sr.Microphone() as source1:
        SpeakText("The time is " +current_time)
        print("The time is ", current_time)
elif "weather" and "today" in MySpeech:
    with sr.Microphone() as source2:
        SpeakText("Which city's weather do you want to know?")
        city = r.listen(source2)
        text = r.recognize_google(city)
        url = "https://www.google.com/search?q="+"weather"+text
        html = requests.get(url).content
        soup = BeautifulSoup(html, 'html.parser')
        temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
        str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
        data = str.split('\n')
        time = data[0]
        sky = data[1]
        SpeakText("Temperature is" + temp)
        SpeakText("Time: " + time)
        SpeakText("Sky Description: " + sky)
else:
    SpeakText("I am sorry I was unable to understand it. Can you please repeat it?")