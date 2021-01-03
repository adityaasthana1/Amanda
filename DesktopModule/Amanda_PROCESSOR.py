import pyttsx3
import os
import sys
import webbrowser
import wikipedia
import YoutubeModule
import CommunicationInterface
import EmotionModule as EM
import json
import random
import FirebaseModule as fm

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

class ProcessorAmanda() :
    def __init__(self): 
        with open('intents.json') as file:
            self.data = json.load(file) 

    def speak(self,AudioInput):
        engine.say(AudioInput)
        engine.runAndWait()
    
    def ExecuteTask(self,query,tag):
        Emotion_wordset = EM.EmotionInterface().key_wordset
        Amanda = CommunicationInterface.AmandaComm()
        for tg in self.data["intents"]:
            if tg['tag'] == tag:
                responses = tg['responses']

        if 'WikipediaInstruct' in tag:
            Amanda.speak(random.choice(responses))
            Amanda.speak("what would you like me to search?")
            searchInput = Amanda.takeInput().lower()
            Amanda.speak('Searching Wikipedia')

            try: 
                results = wikipedia.summary(searchInput,sentences=2)
            except Exception as e :
                print(e)
                self.speak('couldnot find that. Try something else.')    

            self.speak('according to wikipedia')
            self.speak(results)
            print(results)

        elif "YoutubeSearch" in tag : #  any(x in query for x in Youtube_wordset):
            YoutubeRef = YoutubeModule.YoutubeUtil()
            YoutubeRef.TestFunction()
            print("Simulated")
            YoutubeRef.YoutubeSimulator(query)

        elif "lightsOff" or "lightsOn" in tag  :
            firebaseUtils = fm.FirebasUtils()
            firebaseUtils.DatabaseTasks(tag)
        
        elif any(y in query for y in Emotion_wordset):
            EmotionInstance = EM.EmotionInterface()
            EmotionInstance.ProcessEmotion(query)

        elif "goodbye" in tag :
            Amanda.speak(random.choice(responses))
            quit()
        else :
            Amanda.speak(random.choice(responses))

        
                
            
