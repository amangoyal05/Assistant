import speech_recognition as sr
import pyttsx3, requests, wikipedia, pyjokes
from datetime import datetime
from bs4 import BeautifulSoup
from serpapi import GoogleSearch
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
r = sr.Recognizer()

engine = pyttsx3.init()
if('5:00:00'<current_time<'12:00:00'):
    engine.say("Good morning. How may I help you?")
elif('12:00:01'<current_time<'17:00:00'):
    engine.say("Good afternoon. How may I help you?")
elif('17:00:01'<current_time<'20:00:00'):
    engine.say("Good evening. How may I help you?")
else:
    engine.say("Yes master. How may I help you?")
engine.runAndWait()

def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

def search(query):         
    query = query.split(' ') 
    query = " ".join(query[0:])
    SpeakText("I am searching for " + query)
    print(wikipedia.summary(query, sentences = 3))
    SpeakText(wikipedia.summary(query, sentences = 3))

with sr.Microphone() as source:
    while True:
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
                print("Temperature is" + temp)
                print("Time: " + time)
                print("Sky Description: " + sky)
                SpeakText("Temperature is" + temp)
                SpeakText("Time: " + time)
                SpeakText("Sky Description: " + sky)
        elif (MySpeech == 'search'):
            speech = r.recognize_google(audio)
            search(speech)
        #elif "google":
    
        elif "tell" or "joke":
            joke = pyjokes.get_joke(language="en", category="neutral")
            SpeakText(joke)
        elif "shutdown":
            break
        else:
            SpeakText("I am sorry I was unable to understand it. Can you please repeat it?")
            search(audio)