import wikipedia
from utility import CommunicationInterface as ci

class SearchInterface():
    def __init__(self):
        self.remove_wordset = ["seach for","on wikipedia","look for","what is", "Who is", "find me" , "tell me something about", "something about"]
    

    def SearchWiki(self,query,tag):
        Amanda = ci.AmandaComm()
        if 'WikipediaInstrusct' in tag:
            Amanda.speak("What would you like me to search")
            query = Amanda.takeInput()
        query = self.removeShit(query)
        try:
            result = wikipedia.summary(query,sentences=1)
            Amanda.speak(result)
        except Exception as e:
            print("Could not find result  : ", e)
        


    def removeShit(self,query):
        for word in self.remove_wordset:
            print(word)
            query = query.replace(word," ")
            print(query)
        return query
