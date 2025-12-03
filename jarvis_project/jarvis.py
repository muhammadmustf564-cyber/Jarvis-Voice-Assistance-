import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
import wikipedia
import pyjokes
import datetime
import random 
import string

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=2)
        audio = r.listen(source)
    try:
        print("Recognizing...")
        command = r.recognize_google(audio,language = "en-in")
        print(f"you said: {command}\n")
    except:
        print(f"sorry, i did not understand please say again")
        return ""
    return command.lower()

def generate_strong_password():
    letters = string.ascii_letters + string.digits + string.punctuation
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    password += [random.choice(letters) for _ in range(6)]
    random.shuffle(password)
    return "".join(password)

def respond(command):
    if "open google" in command:
        webbrowser.open("https://google.com")
    elif "open facebook" in command:
        webbrowser.open("https://facebook.com")
    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in command:
        webbrowser.open("https://linkedin.com")
    elif "play" in command:
        song = command.replace("play","")
        speak(f"playing {song}")
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"sir, the time is {time}")
    elif "who is" in command:
        person = command.replace("who is","")
        info = wikipedia.summary(person,sentences=1)
        speak(info)
    elif "joke" in command:
        joke = pyjokes.get_joke()
        speak(joke)
    elif "generate password" in command:
        pwd = generate_strong_password()
        speak(f"Your strong password is {pwd}")
        print("Your strong password:", pwd)
    else:
        speak("sorry sir,i cant do yet.")


speak("hey sir, i am jarvis. How can i help u?")
while True:
    command = listen()
    if "quit" in command or "exit" in command:
        speak("goodbay sir")
        break
    elif command != "" :

        respond (command)


