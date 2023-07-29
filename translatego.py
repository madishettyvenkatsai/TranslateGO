import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser
from deep_translator import GoogleTranslator
from text_to_speech import speak
import playsound
from datetime import date
import pyAudioAnalysis
from pyperclip import paste
from sys import argv
import os
import flet
from flet import IconButton, Page, Text, icons

def main(page: Page):
    page.title = "Icon button with 'click' event"
    
    r = sr.Recognizer()    
    def button_clicked(e):
        with sr.Microphone() as source:
            print("Talk")
            speak('Talk')
            audio_text = r.listen(source)
            r.pause_threshold = 1
            page.update()
        page.vertical_alignment = "center"
        page.horizontal_alignment = "center"
        a = IconButton(icon=icons.PLAY_CIRCLE_FILL_OUTLINED, on_click=button_clicked, data=0)
        t = Text()
        page.add(b, t)
        try:
            speech=r.recognize_google(audio_text, language ="te")
            # using google speech recognition
            print("Text: "+speech)
        except:
            print("Sorry, I did not get that")
        text=speech
        translated = GoogleTranslator(source='auto', target='en').translate(text=text)
        speak(translated , "hi", save=True,file= "gayatri.mp3" , speak=True)
        
        if 'Google'in translated:
            webbrowser.open('https://www.google.com/')
            translated = GoogleTranslator(source='auto', target='te').translate(text=text)
            speak(translated)
        elif 'Play' or 'Song' in translated:
            song = translated.replace('play',' ')
            speak('playing' +song)
            pywhatkit.playonyt(song)
            speak("Video is being played on youtube")
        elif 'HDFC Bank' in translated:
            webbrowser.open('https://www.hdfcbank.com/')
            speak("Opening HDFC Website")
        elif 'Bing' in translated:
            webbrowser.open('https://www.bing.com/')
            speak("Opening Bing")
        elif 'time' in translated:
            time = datetime.datetime.now().strftime('%I:%M%p')
            print(time)
            speak('Current time is' +time)
        elif 'Search' or 'about' or 'About' in translated:
            person = translated.replace('wikipedia',' ')
            info = wikipedia.summary(person,3)
            print(info)
            text=info
            translated1= GoogleTranslator(source='auto', target='hi').translate(text=text)
            print(translated1)
            speak(translated1)
        elif 'Whatsapp'in translated:
            webbrowser.open('https://web.whatsapp.com/')
            speak("Opening whatsapp")
        elif 'hungry' in translated:
            text='eat something,be health consious'
            c=GoogleTranslator(source='auto',target='te').translate(text=text)
            speak('eat something,be health consious')
        elif 'vande Mataram' in translated:
            speak('vande mataram , we are indians')
        elif 'what is your name' in translated:
            print('My name is TranslateGo.')
            speak('My name is TranslateGo.')
        elif 'TG' in translated:
            speak('Namaskar , my name is TG')
        elif 'date' in translated:
            now = datetime.datetime.now()
            date_time_str = now.strftime("%d-%M-%Y %I:%M%p")
            print('DateTime:', date_time_str)
            speak(f"The Date is {date_time_str}")
        elif 'Docs' in translated:
            webbrowser.open('https://docs.google.com/document/')
            speak('Google docs')
        elif 'Meditation' in translated:
            text='please relax while listening'
            a=GoogleTranslator(source='auto',target='te').translate(text=text)
            speak(a)
            webbrowser.open('https://www.youtube.com/watch?v=JEoxUG898qY')
        elif 'go' or 'Go' in translated:
            with sr.Microphone() as source:
                address = r.listen(source)
                r.pause_threshold = 1
                try:
                    speech=r.recognize_google(address, language ="te")
                    # using google speech recognition
                    print("Text: "+speech)
                    text=speech
                    b=GoogleTranslator(source='auto',target='te').translate(text=text)
                    speak(b)
                except:
                    text='please tell again'
                    print('please tell again')
            webbrowser.open("http://www.google.com/maps/place/"+b)
flet.app(target=main)

