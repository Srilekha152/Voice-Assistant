import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes


def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing....")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Not understandable")

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',120)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':
   
   
    if sptext().lower() == "hey jarvis":
        data1=sptext().lower()
        
        if "your name" in data1:
            name="my name is jarvis"
            speechtx(name)

        elif "old are you" in data1:
            age = "i am one year old"
            speechtx(age)        

        elif 'time' in data1:
            time = datetime.datetime.now().strftime("%I%M%p")
            speechtx(time)
        elif 'youtube' in data1:
            webbrowser.open("https://www.youtube.com/")

        elif 'whatsapp' in data1:
            webbrowser.open("https://web.whatsapp.com/")

        elif 'mail' in data1:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

        elif 'joke' in data1:
            jokes_1 = pyjokes.get_joke(language="en",category="neutral")
            print(jokes_1)
            speechtx(jokes_1)


        else:
          print("thanks")