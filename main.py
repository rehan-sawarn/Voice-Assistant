import pyttsx3 as p
import speech_recognition as sr
from wikipedia_search import infow
import randfacts
import datetime


engine= p.init() #initializing the speech engine
engine.setProperty('rate', 180)
voices= engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
rate = engine.getProperty('rate')
#engine.say("Hello, I am your assistant R2D2")
#engine.runAndWait() #running the speech engine

r= sr.Recognizer()  #recognizer class,helps retrive audio from microphone

def speak(text):
    engine.say(text)
    engine.runAndWait()

today= datetime.datetime.now()
speak("Hello, I am your assistant, Dwight") 
speak(f"Today is {today.strftime('%A')} and the time is {today.strftime('%H:%M')}")
speak("How are you doing today?")


with sr.Microphone() as source:
    r.energy_threshold= 10000 #minimum audio energy to consider for recording
    r.adjust_for_ambient_noise(source,1.2) #adjusting the recognizer to the ambient noise
    print("Listening...")
    audio= r.listen(source)
    print("Done Listening...")
    text= r.recognize_google(audio)
    print(text)


if "what" and "about" and "you" in text:
    speak("I am doing great. Thank you for asking")
speak("How can I help you today?")


with sr.Microphone() as source:
    r.energy_threshold= 10000 #minimum audio energy to consider for recording
    r.adjust_for_ambient_noise(source,1.2) #adjusting the recognizer to the ambient noise
    print("Listening...")
    audio= r.listen(source)
    print("Done Listening...")
    text2= r.recognize_google(audio)

if "information" or "Wikipedia" in text2:
    speak("You need information to which topic. Please tell me what you want to know")
    
    with sr.Microphone() as source:
        r.energy_threshold= 10000 #minimum audio energy to consider for recording
        r.adjust_for_ambient_noise(source,1.2) #adjusting the recognizer to the ambient noise
        print("Listening...")
        audio= r.listen(source)
        print("Done Listening...")
        infor= r.recognize_google(audio)
    speak(f"Searching for {infor} on wikipedia")
    assist = infow()
    assist.get_info(infor) 

elif "play" or "Youtube" in text2:
    speak("What video do you want me to play for you?")
    
    with sr.Microphone() as source:
        r.energy_threshold= 10000 #minimum audio energy to consider for recording  
        r.adjust_for_ambient_noise(source,1.2)
        print("Listening...")
        audio= r.listen(source)
        print("Done Listening...")
        video= r.recognize_google(audio)
    speak(f"Playing {video} on youtube")
    from YT_search import music
    assist = music()
    assist.play(video)

elif "news" in text2:
    speak("Here are the top 5 news headlines for you")
    from news import news
    ar=news()
    for i in range(5):
        print(ar[i])
        speak(ar[i])
        #write code so that it will ask for description and if we need it or not

elif "fact" or "facts" in text2:
    speak("Here is a random fact for you")
    fact= randfacts.get_fact()
    print(fact)
    speak(fact)
    print(text2)

elif "joke" or "jokes" or "funny" in text2:
    if "funny" in text2:
        speak("Here is a funny joke for you")
    else:
        speak("Here is a joke for you")
    from jokes import joke
    arr=joke()
    print(arr[0])
    speak(arr[0])
    print(arr[1])
    speak(arr[1])


