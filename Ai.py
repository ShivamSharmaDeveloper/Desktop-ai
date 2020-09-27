import pyttsx3                      #pip install pyttsx3
import speech_recognition as sr     #pip install speechRecognition
import datetime
import wikipedia                    #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)

engine.setProperty('voices', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    
    elif hour>=12 and hour<18:
        speak("Good afternoon!")
    
    else:
        speak("Good evening!")

    speak("I am Jarvis sir. How can i help you")

def takecommand():
    #it takes command from here
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit = 5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to,command):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishme()
    while True:
    # if 1:
        query = takecommand().lower()

        # logic exicuting tasks based on query
        if 'wikipedia' in query:
            speak("Searching wikipedia....")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'H:\\New Folder'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Shivam sharma\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to harry' in query:
            try:
                speak("What should i say?")
                content = takecommand()
                to = "yourharrysemail@gmail.com"
                sendEmail(to,content)
                speak("Email has sent successfully")
            except Exception as e:
                print(e)
                speak("Sorry my friend, The email couldn't be sent")
        elif 'exit' in query:
            speak("Thank you sir, For your time.")
            exit()



