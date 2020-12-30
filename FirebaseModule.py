import pickle
import pyrebase
import CommunicationInterface as ci
import requests

class UserInformationFirebase :
    def __init__(self, email,password,uid):
        self.useremail = email
        self.userpassword = password
        self.uid = uid
    
    

class FirebasUtils:
    def __init__(self):
        with open("firebaseDataConfig.pickle",'rb') as file:
            self.firebaseConfig = pickle.load(file)
            file.close()
        self.firebase = pyrebase.initialize_app(self.firebaseConfig)
        self.firebaseAuth = self.firebase.auth()
        self.firebaseDatabase = self.firebase.database()

    def LoginUser(self):
        Amanda = ci.AmandaComm()
        Amanda.speak("Please Enter your Email and password in the console.")
        email = input("Enter your Email :\n")
        password = input("Enter your Password :\n")
        
        try :
            self.firebaseAuth.sign_in_with_email_and_password(email,password)
            self.firebaseAuth = self.firebase.auth()
            userInstance = UserInformationFirebase(email,password,self.firebaseAuth)
            with open("UserData.pickle",'wb') as file:
        
        except Exception as e :
            print(e)

print(firebaseConfig)
