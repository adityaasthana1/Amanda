import pyttsx3
import os
import sys
import webbrowser
import wikipedia
import json
import random
from utility import YoutubeModule
from utility import CommunicationInterface
from utility import EmotionModule as EM
from utility import FirebaseModule as fm
from utility import SearchModule as sm

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

class ProcessorAmanda() :
    def __init__(self): 
        with open('./data/intents.json') as file:
            self.data = json.load(file) 

    def speak(self,AudioInput):
        engine.say(AudioInput)
        engine.runAndWait()
    
    def ExecuteTask(self,query,tag):
        Emotion_wordset = EM.EmotionInterface().key_wordset
        Amanda = CommunicationInterface.AmandaComm()
        YoutubeRef = YoutubeModule.YoutubeUtil()
            
        for tg in self.data["intents"]:
            if tg['tag'] == tag:
                responses = tg['responses']

        if 'WikipediaInstruct' in tag:
            SearchInstance = sm.SearchInterface()
            SearchInstance.SearchWiki(query,tag)

        if 'WikiSearch' in tag:
            SearchInstance = sm.SearchInterface()
            SearchInstance.SearchWiki(query,tag)

        elif "Introduction" in tag:
            Amanda.speak(responses[0])

        elif "YoutubeSearch" in tag : #  any(x in query for x in Youtube_wordset):
            YoutubeRef.TestFunction()
            #print("Simulated")
            YoutubeRef.YoutubeSimulator(query)

        elif "YoutubePlay" in tag:
            YoutubeRef.Play(query)


        elif "lightsOff" in tag  :
            Amanda.speak(random.choice(responses))
            firebaseUtils = fm.FirebasUtils()
            firebaseUtils.DatabaseTasks(tag)

        elif "lightsOn" in tag  :
            Amanda.speak(random.choice(responses))
            firebaseUtils = fm.FirebasUtils()
            firebaseUtils.DatabaseTasks(tag)
        
        elif any(y in query for y in Emotion_wordset):
            EmotionInstance = EM.EmotionInterface()
            EmotionInstance.ProcessEmotion(query)

        elif "goodbye" in tag :
            Amanda.speak(random.choice(responses))
            quit()
        else :
            print("we are here")
            Amanda.speak(random.choice(responses))

        
                
            
