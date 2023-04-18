import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'Jarvis' in command:
                command = command.replace('Jarvis', '')
                print(command)
    except:
        command = None
    return command


def run_alexa():
    command = take_command()
    if command is not None:
        print(command)
        if 'play' in command:
            song = command.replace('play', '')
            talk('Yes sir, playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
        elif 'who is' in command:
            person = command.replace('who is ', '')
            try:
                info = wikipedia.summary(person, 1)
                print(info)
                talk(info)
            except wikipedia.exceptions.PageError:
                talk("I'm sorry, I couldn't find any information about " + person)
        elif 'date' in command:
            talk('sorry, i have a headache')
        elif 'are you single' in command:
            talk('I am in a relationship with wifi')
        elif 'wake up' in command:
            talk('Yes sir, i am here for you')
        elif 'joke' in command:
            talk(pyjokes.get_joke())
        else:
            talk('Please say the command again.')


while True:
    run_alexa()
