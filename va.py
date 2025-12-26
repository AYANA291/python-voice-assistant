from gtts import gTTS
import pyglet
import time
import os
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes

# ---------------- Text-to-Speech ---------------- #
def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = "temp.mp3"
    tts.save(filename)
    
    music = pyglet.media.load(filename, streaming=False)
    music.play()
    time.sleep(music.duration)  # wait until finished
    
    os.remove(filename)

# ---------------- Speech-to-Text ---------------- #
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    except:
        print("Say that again please...")
        return "none"
    return query.lower()

# ---------------- Main Program ---------------- #
if __name__ == "__main__":
    speak("Hello! I am your assistant. How can I help you today?")

    while True:
        query = takeCommand()

        if "your name" in query:
            speak("My name is Peter")
            print("My name is Peter")

        elif "open youtube" in query:
            webbrowser.open("https://youtube.com")
            speak("Opening YouTube")

        elif "open google" in query:
            webbrowser.open("https://google.com")
            speak("Opening Google")

        elif "open website" in query:
            speak("Which website should I open?")
            site = takeCommand()
            if site != "none":
                if not site.startswith("http"):
                    site = "https://" + site
                webbrowser.open(site)
                speak(f"Opening {site}")

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
            print(strTime)

        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)
            print(joke)

        elif "exit" in query or "quit" in query:
            speak("Goodbye! Have a nice day!")
            break

        else:
            speak("I am searching that on Google for you.")
            webbrowser.open(f"https://www.google.com/search?q={query}")
