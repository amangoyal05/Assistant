import speech_recognition as sr
import pyttsx3
#time
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
engine = pyttsx3.init()
recording = sr.Recognizer()

with sr.Microphone() as source:
    recording.adjust_for_ambient_noise(source)
engine.say("Hello! How may I help you?")
engine.runAndWait()
audio = recording.listen(source)
if audio == 'Time':
    engine.say('The time is ' + current_time)

try:
    print("You said: n" + recording.recognize_google(audio))
except Exception as e:
    print(e)