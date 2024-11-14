import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open flipkart" in c.lower():
        webbrowser.open("https://flipkart.com")
    elif "open amazon" in c.lower():
        webbrowser.open("https://amazon.in")
    elif "open zomato" in c.lower():
        webbrowser.open("https://zomato.com")
    elif "open swiggy" in c.lower():
        webbrowser.open("https://swiggy.com")
    elif "open lenskart" in c.lower():
        webbrowser.open("https://lenskart.com")
    elif "open dominos" in c.lower():
        webbrowser.open("https://dominos.co.in")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)    


if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
        # Recognise speech using Sphinx
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source,timeout = 2, phrase_time_limit=1)

            word = r.recognize_google(audio)
            if "jarvis" in word.lower():
                speak("Ya")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source,timeout = 2, phrase_time_limit=1)
                    command = r.recognize_google(audio)
                    processCommand(command)
                    print(command)
            
        except Exception as e:
            print("Error, {0}".format(e))