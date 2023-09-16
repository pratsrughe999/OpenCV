import speech_recognition as sr
import os

def say(text):
    os.system(f"say {text}")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1         #changing the threshold file can be customised
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e :
            return "Some error occured"

if __name__== '__main__':
    print('Pycharm')
    say("Hello Pratik,  I am Jarvis A.I")
    while True:
        print("Listening...")
        text = takeCommand()
        say(text)

