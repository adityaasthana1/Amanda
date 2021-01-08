import pyttsx3
import speech_recognition as sr
from gtts import gTTS
import playsound as ps
import random
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
newVoiceRate = 180
engine.setProperty('rate',newVoiceRate)

class AmandaComm():
    def __init__(self):
        self.a = 100
        self.b = 200

    
    def speak(self,audio):
        
        engine.say(audio)
        engine.runAndWait()

        '''
        print("we are here")
        tts = gTTS(text = audio, lang = 'en', slow = False)
        randomNum = random.randrange(0,200)
        tts.save("{}.mp3".format(randomNum))
        ps.playsound("{}.mp3".format(randomNum))
        os.remove("{}.mp3".format(randomNum))
        '''

    def takeInput(self) :
    #For Input Source (Microphone Array)
        Recognizer = sr.Recognizer()
        with sr.Microphone() as source :
            print("Listening...")
            Recognizer.pause_threshold = 0.5
            Recognizer.energy_threshold = 10000
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
    
