
import CommunicationInterface as sti
import pywhatkit as kit
import requests




class YoutubeUtil():
    def __init__(self):
        self.a = 100
        self.b = 200
        self.YT_wordset = ['play on youtube','play','youtube','open youtube','play in youtube', 'youtube songs','on youtube',
        'play','play something','play a song','play anything']
    
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
        InputSearch.replace('play','')
        kit.playonyt(InputSearch)

