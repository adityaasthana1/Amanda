
from utility import CommunicationInterface as sti
import pywhatkit as kit
import requests




class YoutubeUtil():
    def __init__(self):
        self.a = 100
        self.b = 200
        self.YT_wordset = ['play','youtube','open youtube','play in youtube', 'youtube songs','on youtube',
        'play','play something','play a song','play anything']
        self.remove_wordset = ['play','on youtube']
    
    def TestFunction(self):
        print('Hello!')
    
    def YoutubeSimulator(self,query):
        #for simulating flow on YouTube
    
        Amanda = sti.AmandaComm()
        '''
        for x in self.YT_wordset:
            query.replace(x,'')
        if len(query) == 0:
            CommunicationInterface.AmandaComm().speak('What would you like me to play?')
            query = CommunicationInterface.AmandaComm().takeInput()
                
        StringArg = 'playing' + query + 'on youtube'
        Amanda.speak(StringArg)
        '''
        Amanda.speak('What would you like me to play on YouTube?')
        InputSearch = Amanda.takeInput()
        InputSearch = self.removeShit(InputSearch)
        speech = "playing" + InputSearch + "on youtube"
        Amanda.speak(speech)
        kit.playonyt(InputSearch)

    def Play(self,query):
        query = self.removeShit(query)
        speech = "playing" + query + "On youtube"
        Amanda = sti.AmandaComm()
        Amanda.speak(speech)
        kit.playonyt(query)

    def removeShit(self,query):
        remove_wordset = ['play','on youtube']
        for word in remove_wordset:
            print(word)
            query = query.replace(word," ")
            print(query)
        return query
        