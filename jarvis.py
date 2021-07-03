import pyttsx3 
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyaudio

print('Initializing Jarvis')

MASTER = "Sir"

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Moorning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
        speak("")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language="en-us")
        print(f"user said: {query}\n")

    except Exception as e:
        print("Say that again please")
        query = None
    return query

speak("Hallo sir, my name is Jarvis, i can help you sir !")
wishMe()
query = takeCommand()

if "wikipedia" in query.lower():
    speak("open wikipedia...")
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    print(results)
    speak(results)
elif "open youtube" in query.lower():
    url = "youtube.com"
    chrom_path = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"
    webbrowser.get(chrom_path).open(url)