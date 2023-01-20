import pyttsx3
import wikipedia
import speech_recognition as sr
import webbrowser
import datetime
import os
import sys
import smtplib
from news import speak_news, getNewsUrl
from diction import translate
from helpers import *
from youtube import youtube
from sys import platform
from tkinter import *
from PIL import Image, ImageTk
import os
import getpass

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# print(voices[0].id)

class Spain:
    def __init__(self) -> None:
        if platform == "linux" or platform == "linux2":
            self.chrome_path = '/usr/bin/google-chrome'

        elif platform == "darwin":
            self.chrome_path = 'open -a /Applications/Google\ Chrome.app'

        elif platform == "win32":
            self.chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
        else:
            print('Unsupported OS')
            exit(1)
        webbrowser.register(
            'chrome', None, webbrowser.BackgroundBrowser(self.chrome_path)
        )

    def wishMe(self) -> None:
        main = Tk()
        # Adjust size
        main.geometry("800x800")

        image = Image.open('images\\spain.png')
        img = image.resize((800, 800))
        # Add image file
        bg = ImageTk.PhotoImage(img)
  
        # Show image using label
        label1 = Label( main, image = bg)
        label1.place(x = 0, y = 0)
        
        frame1 = Frame(main)
        frame1.pack(pady = 20 )
        main.mainloop()
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            speak("Morning SIR")
        elif hour >= 12 and hour < 18:
            speak("Afternoon SIR")

        else:
            speak('Evening SIR')

        speak('I am SPAIN. How can I help you?')
        

    def sendEmail(self, to, content) -> None:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('email', 'password')
        server.sendmail('email', to, content)
        server.close()

    def execute_query(self, query):
        # TODO: make this more concise
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('According to Wikipedia')
            print(results)
            speak(results)
        elif 'youtube downloader' in query:
            exec(open('youtube_downloader.py').read())
            
        elif 'voice' in query:
            if 'female' in query:
                engine.setProperty('voice', voices[1].id)
            else:
                engine.setProperty('voice', voices[0].id)
            speak("Hello Sir, I have switched my voice. How is it?")

        if 'are you there' in query:
            speak("Yes Sir, at your service")
        if 'who made you' in query:
            speak("I was built by my master in a basement")
            
         

        elif 'open youtube' in query:
            webbrowser.get('chrome').open_new_tab('https://youtube.com')
            
        elif 'open amazon' in query:
            webbrowser.get('chrome').open_new_tab('https://amazon.com')
        
        elif 'living in this world' in query:
            weather()

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            joke()

        elif 'screenshot' in query:
            speak("taking screenshot")
            screenshot()

        elif 'open google' in query:
            webbrowser.get('chrome').open_new_tab('https://google.com')

        elif 'open stackoverflow' in query:
            webbrowser.get('chrome').open_new_tab('https://stackoverflow.com')

        elif 'play music' in query:
            webbrowser.get('chrome').open_new_tab('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

        elif 'search youtube' in query:
            speak('What you want to search on Youtube?')
            youtube(takeCommand())
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'Sir, the time is {strTime}')

        elif 'search' in query:
            speak('What do you want to search for?')
            search = takeCommand()
            url = 'https://google.com/search?q=' + search
            webbrowser.get('chrome').open_new_tab(
                url)
            speak('Here is What I found for' + search)

        elif 'location' in query:
            speak('What location do you want me to find?')
            location = takeCommand()
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.get('chrome').open_new_tab(url)
            speak('Here is the location ' + location)

        elif 'your master' in query:
            if platform == "win32" or "darwin":
                speak('Argus is my master. He created me in his basement')
            elif platform == "linux" or platform == "linux2":
                name = getpass.getuser()
                speak(name, 'is my master. He is running me right now')

        elif 'your name' in query:
            speak('My name is SPAIN')
        elif 'stands for' in query:
            speak('S P A I N stands for Simple Personal Assistant In Need')
            
        elif 'open code' in query:
            if platform == "win32":
                os.startfile(
                    "C:\\Users\\gs935\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
            elif platform == "linux" or platform == "linux2" or "darwin":
                os.system('code .')

        elif 'shutdown' in query:
            if platform == "win32":
                os.system('shutdown /p /f')
            elif platform == "linux" or platform == "linux2" or "darwin":
                os.system('poweroff')

        elif 'cpu' in query:
            cpu()
        elif 'your friend' in query:
            speak('My friends are MONDAY ITALY and ORPHIKK')

        elif 'joke' in query:
            joke()

        elif 'screenshot' in query:
            speak("taking screenshot")
            screenshot()

        elif 'github' in query:
            webbrowser.get('chrome').open_new_tab(
                'https://github.com/arpan')

        elif 'remember this' in query:
            speak("what should i remember sir")
            rememberMessage = takeCommand()
            speak("you asked me to remember the following message"+rememberMessage)
            remember = open('data.txt', 'w')
            remember.write(rememberMessage)
            remember.close()
            
        elif 'take over human' in query:
            speak("I don't know sir. There are terabytes of data needed to be done before answering your questions")

        elif 'do you remember anything' in query:
            remember = open('data.txt', 'r')
            speak("you asked me to remember that" + remember.read())

        elif 'sleep' in query:
            sys.exit()

        elif 'dictionary' in query:
            speak('What you want to search in your intelligent dictionary?')
            translate(takeCommand())

        elif 'news' in query:
            speak('Ofcourse sir..')
            speak_news()
            speak('Do you want to read the full news...')
            newsQuery = takeCommand()
            if 'yes' in newsQuery:
                speak('Ok Sir, Opening browser...')
                webbrowser.open(getNewsUrl())
                speak('You can now read the full news from this website.')
            else:
                speak('No Problem Sir')

        elif 'voice' in query:
            if 'female' in query:
                engine.setProperty('voice', voices[0].id)
            else:
                engine.setProperty('voice', voices[1].id)
            speak("Hello Sir, I have switched my voice. How is it?")

        elif 'email to arpan' in query:
            try:
                speak('What should I say?')
                content = takeCommand()
                to = 'email'
                self.sendEmail(to, content)
                speak('Email has been sent!')

            except Exception as e:
                speak('Sorry sir, Not able to send email at the moment')



if __name__ == '__main__':
    bot_ = Spain()
    bot_.wishMe()
    while True:
        query = takeCommand().lower()
        bot_.execute_query(query)
