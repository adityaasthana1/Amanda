from utility import CommunicationInterface as CI
from utility import YoutubeModule as YM
import random 
from utility import Favorite
import pywhatkit as kit


class EmotionInterface():
    def __init__(self):
        self.key_wordset = ['feeling','feels','feel','felt']
        self.positive_wordset = {
            'patterns':['happy','good','really cool','great','fine','perfect'],
            'responses' : ['thats good!','really good to know that','That is amazing','That is good for you','hope, happiness stays','thats sexy']
        }
        self.negative_wordset ={
            'patterns' : ['sad','sed','bad','not good','not great','really bad','sick'],
            'responses' : ['It is sad to hear that','Well, Everything will be fine','Its about time','time shall pass']
        }
        self.neutral_wordset = ['ok','okay','nothing','dont know']
    
    def ProcessEmotion(self,query):
        Amanda = CI.AmandaComm()

        if any(x in query for x in self.positive_wordset['patterns']):
            Amanda.speak(random.choice(self.positive_wordset['responses']))
            Amanda.speak('What would you like me to do for you?')
            return 
        if any(x in query for x in self.negative_wordset['patterns']):
            Amanda.speak(random.choice(self.negative_wordset['responses']))
            Amanda.speak('Would you like me to play any of your favorite songs?')
            response = Amanda.takeInput()
            confirm = ['sure','why not','yes','great','yeah','yea','ya']
            if any(x in response for x in confirm):
                songname = random.choice(Favorite.FavoriteItems().favorit_songs)
                Amanda.speak('playing ' + songname)
                kit.playonyt(songname)
            else : 
                Amanda.speak('Sure, What would you like me to do for you?')


