import numpy
import nltk
from nltk.stem.lancaster import LancasterStemmer
import tflearn
import tensorflow
import random
import json
import pickle
import CommunicationInterface as ci
import Amanda_PROCESSOR as ap
import pyrebase
import FirebaseModule as fm



stemmer = LancasterStemmer()
with open("intents.json") as file:
    data = json.load(file)

try:
    #sdasdgahsdas
    with open("./model_data/data.pickle", "rb") as f:
        words, labels, training, output = pickle.load(f)
except:
    words = []
    labels = []
    docs_x = []
    docs_y = []

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            wrds = nltk.word_tokenize(pattern)
            words.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(intent["tag"])

        if intent["tag"] not in labels:
            labels.append(intent["tag"])

    words = [stemmer.stem(w.lower()) for w in words if w != "?"]
    words = sorted(list(set(words)))

    labels = sorted(labels)

    training = []
    output = []

    out_empty = [0 for _ in range(len(labels))]

    for x, doc in enumerate(docs_x):
        bag = []

        wrds = [stemmer.stem(w.lower()) for w in doc]

        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)

        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1

        training.append(bag)
        output.append(output_row)


    training = numpy.array(training)
    output = numpy.array(output)

    with open("./model_data/data.pickle", "wb") as f:
        pickle.dump((words, labels, training, output), f)

tensorflow.compat.v1.reset_default_graph()
net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 12)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

try:
    #xxxdddasda
    model.load("./model_data/model.tflearn")
except:
    model.fit(training, output, n_epoch=500, batch_size=8, show_metric=True)
    model.save("./model_data/model.tflearn")

def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
            
    return numpy.array(bag)


def chat():
    while True:
        #inp = input("You: ")
        Amanda = ci.AmandaComm()
        query = Amanda.takeInput().lower()
        #if inp.lower() == "quit":
            #break

        results = model.predict([bag_of_words(query, words)])
        results_index = numpy.argmax(results)
        print(results)
        print(numpy.argmax(results))
        print(results_index)
        if(numpy.argmax(results) < 0.50) :
            print("LOW QUAL")
        else :
            tag = labels[results_index]
            print(tag)
            if query == "say again please":
                pass
            else :
                AmandaProcessor = ap.ProcessorAmanda()
                AmandaProcessor.ExecuteTask(query,tag)
        

while True:
    try :
        with open("UserData.pickle",'rb') as file :
            userData = pickle.load(file)
            if bool(userData) :
                print(userData.useremail)
                break
                

    except Exception as e:
        Amanda = ci.AmandaComm()
        Amanda.speak("Please Enter your Email and password in the console.")
        email = input("Enter your Email :\n")
        password = input("Enter your Password :\n")
        FirebaseInstance = fm.FirebasUtils()
        LoginResult = FirebaseInstance.LoginUser(email,password)
        print("DONE")
        if LoginResult == "LOGIN_SUCCESS" :
            Amanda = ci.AmandaComm()
            Amanda.speak("Logged In")
            break
    

chat()

