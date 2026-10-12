import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "ea6a49ef5dc0485cb85f7172361a717d"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    if "open google" in c.lower():
         webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
         webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
         webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
         webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=ea6a49ef5dc0485cb85f7172361a717d")
        if r.status_code == 200:
            #Parse the JSON response
            data = r.json()

            # Extract articles
            articles = data.get("articles", [])

            # Display headlines
            for article in articles:
                speak(article['title'])

    else:
        # Let Openai follow the request
        pass

if __name__ == "__main__":
    speak("Initializing Jarvis.......")
    while True:
        #Listen for the wake word "charlos"
        # obtain audio from the microphone
        r = sr.Recognizer()

        print("recognizing....")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("ya")
            #Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processcommand(command)



        except Exception as e:
            print("Error; {0}".format(e))

