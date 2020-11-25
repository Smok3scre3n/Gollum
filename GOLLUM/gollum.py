import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests

#setting up the speech engine,id 0 indicates a male voice while id 1 indicates a female voice
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')

#defining a function speak which converts text to speech,run and wait is used to block while processing all currently queued commands
def speak(text):
    engine.say(text)
    engine.runAndWait()

#initiates a function to greet the user
def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")

#setting up the command function for your AI assistant ,takecommand is used to understand human speech
#recognize_google function uses google audio to recognize speech.
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception :
            speak("Pardon me, please say that again")
            return "None"
        return statement

print("Loading your AI personal assistant Gollum")
speak("Loading your AI personal assistant Gollum")
wishMe()

#main
if __name__=='__main__':


    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant Gollum is shutting down,Good bye')
            print('your personal assistant Gollum is shutting down,Good bye')
            break


#fetching data from Wikipedia
        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

#accessing the Web Browsers 
        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

#predicting the weather
        elif "weather" in statement:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")


#predicting time
        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

#giving a description
        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am Gollum your personal assistant. I am programmed to perform minor tasks like'
                  'opening youtube,google chrome and gmail ,predict time,take a photo,search wikipedia,predict weather' 
                  'in different cities , get top headline news from the New York Times and you can ask me computational or geographical questions too!')

#figuring out the creator
        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Lisa")
            print("I was built by Lisa")

#opening a webpage
        elif "open a tragic story" in statement:
            webbrowser.open_new_tab("https://youtu.be/oNGq16nHr-Q")
            speak("Here is MADEMOISELLE NOIR")

#to fetch latest news
        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://www.nytimes.com/international/")
            speak('Here are some headlines from Newyork Times,Happy reading')
            time.sleep(6)

#capturing photo
        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0,"robo camera","img.jpg")

#Searching data from web
        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

#setting your AI assistant to answer geographical and computational questions
        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question=takeCommand()
            app_id="R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

#to log off your PC
        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

time.sleep(3)