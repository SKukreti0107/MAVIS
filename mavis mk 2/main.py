
from model import model , bag_of_words , words , labels , data, np , nltk
import random

from mic_input import listen
from speach import speak
from search import search
from calc import chatbot

from nltk.corpus import stopwords 
from search import search
from nltk.tokenize import word_tokenize, sent_tokenize






def chat():

    #predefined varaiable :
    j = 0
    
    #importing user input from mic getting response from data
    while True:
        chat.inp = listen()
        #chat.inp = input("you:")
        results = model.predict([bag_of_words(chat.inp, words)])[0]
        results_index = np.argmax(results)
        tag = labels[results_index]
        
        if results[results_index] >= 0.8:
            for tg in data["intents"]:
                if tg["tag"]== tag:
                    responses = tg["responses"]
                    chat.response = (random.choice(responses))
                    print(chat.response)
                    speak(chat.response)
                    return(chat.response)
        else:
            print("i didnt get that . please try again")
            speak('i didnt get that . please try again')
  

        #workflow for tasks:

        if tag == "goodbye":
            exit()

        if tag == "search":
            '''
            sentences = nltk.sent_tokenize(chat.inp)
            for sentence in sentences:
                wd = nltk.word_tokenize(sentence)
                wd = [word for word in wd if word not in set(stopwords.words('english'))]
                tagged = nltk.pos_tag(wd)
                x = []
                str1 = " "
                for (wd, tag) in tagged:
                    if tag =='NN'or 'NNP'or'NNS'or'NNPS': # If the word is a proper noun
                        x.append(wd)       
                #print(x)
                a=str1.join(x)
                #print(a)'''
            search(chat.inp)


        if tag == "calc":
            chatbot(chat.inp)





        

        if tag == 'jokes':
            j = 1 

        if tag =="jokes_response_+":
            if j == 0:
                resp = 'did i tell a joke , i guess i forgot','i dont remember telling a joke'
                resp = random.choice(resp)
                print(resp)
            if j == 1 :
                resp = "thankyou","ah good to know","glad i could make you laugh"
                resp = random.choice(resp)
                print(resp)
                j = 2 
            if j == 2 :
                resp = 'you still on that joke. move on.','wow it what that good huh.'
             
           
chat()