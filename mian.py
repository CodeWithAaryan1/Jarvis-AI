import datetime
import pyttsx3
import speech_recognition as sr
import os
import wikipedia
import webbrowser
import pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis. How may I assist you?")


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open chrome' in query:
            codepath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            speak("Opening Chrome")
            os.startfile(codepath)

        elif 'open code' in query:
            codepath =  "C:\\Users\\codew\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("Opening VS Code")
            os.startfile(codepath)

        elif 'open website' in query:
            speak("Which website would you like me to open?")
            website= takeCommand()
            url = f"https://www.{website}.com"
            webbrowser.open(url)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'play music' in query:
            speak("Which song would like me to play")
            song = takeCommand()
            pywhatkit.playonyt(song)
            speak("playing"+ song)

        elif 'GoodBye':
            speak("Thank you for using me")
            exit()
