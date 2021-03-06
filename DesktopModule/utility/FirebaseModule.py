import pickle
import pyrebase
from utility import CommunicationInterface as ci
import requests
import json

class UserInformationFirebase :
    def __init__(self, email,password,uid):
        self.useremail = email
        self.userpassword = password
        self.uid = uid

class FirebasUtils:
    def __init__(self):
        with open("./data/firebaseDataConfig.pickle",'rb') as file:
            self.firebaseConfig = pickle.load(file)
            file.close()
        self.firebase = pyrebase.initialize_app(self.firebaseConfig)
        self.firebaseAuth = self.firebase.auth()
        self.firebaseDatabase = self.firebase.database()
        

    def LoginUser(self,email,password):
               
        try :
            login = self.firebaseAuth.sign_in_with_email_and_password(email,password)
            self.firebaseAuth = self.firebase.auth()
            userInstance = UserInformationFirebase(email,password,login['localId'])
            with open("./data/UserData.pickle",'wb') as file:
                pickle.dump(userInstance,file)
                file.close()
            print("logged in ")
            print(login['localId'])
            return "LOGIN_SUCCESS"
        except requests.HTTPError as e:
            error_json = e.args[1]
            error = json.loads(error_json)['error']['message']
            print(error)
            if error == "ENAIL_NOT_FOUND":
                print("Email not available!")
            
    def DatabaseTasks(self,tag):
        with open("./data/UserData.pickle",'rb') as file:
            userData = pickle.load(file)

        if "lightsOff" in tag:
            self.firebaseDatabase.child(userData.uid).child("D1").set("OFF")
        if "lightsOn" in tag:
            self.firebaseDatabase.child(userData.uid).child("D1").set("ON")
    
