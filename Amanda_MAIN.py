import pyttsx3
import datetime
import speech_recognition as sr
import Amanda_PROCESSOR as ap 
import nltk
import tensorflow


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
newVoiceRate = 180
engine.setProperty('rate',newVoiceRate)

def speak(audio) :
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 10 and hour < 12 :
        speak('Good Morning')
    
    elif hour >= 12 and hour < 18 :
        speak('Good Afternoon!')
    
    else :
        speak ('Good Evening!')
    
    speak("I am Amanda! How may I help you?")

def takeInput() :
    #For Input Source (Microphone Array)
    Recognizer = sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening...")
        Recognizer.pause_threshold = 1
        Recognizer.energy_threshold = 2000   
        Recognizer.dynamic_energy_threshold = True
        Recognizer.dynamic_energy_ratio = 1.5
        Recognizer.dynamic_energy_adjustment_damping = 0.15
        Recognizer.operation_timeout = None   
        audio = Recognizer.listen(source)

    try:
        print('Recognizing..')
        query = Recognizer.recognize_google(audio,language='en-in')
        print(f"user said : {query}\n")
        
    except Exception as e : 
        print(e)
        print('Recognized : NULL')
        queryx = 'say again please'
        return queryx

    return query

if __name__ == "__main__":
    wishMe()
    taskProcessor = ap.ProcessorAmanda()
    
    while True :
        query = takeInput().lower()
        taskProcessor.ExecuteTask(query)


    