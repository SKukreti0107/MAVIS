
import tkinter as tk
from tkinter import scrolledtext
from threading import Thread


from model import model , bag_of_words , words , labels , data, np , nltk
import random

from mic_input import listen
from speach import speak
from search import search
from calc import chatbot

from nltk.corpus import stopwords 
from search import search
from nltk.tokenize import word_tokenize, sent_tokenize

# initialize the Tkinter GUI
root = tk.Tk()
root.title("Chatbot")
root.geometry("600x500")

# add labels and entry box for user input
label = tk.Label(root, text="Enter your message:", font=("Helvetica", 16))
label.pack(pady=10)

input_box = tk.Entry(root, width=50, font=("Helvetica", 14))
input_box.pack(pady=10)

# add scrolled text widget to display chat history
output_box = scrolledtext.ScrolledText(root, width=60, height=20, font=("Helvetica", 14))
output_box.pack(pady=10)

# define the chatbot function
def chatbot(input):
    # your chatbot code here
    #predefined varaiable :
    j = 0
    
    #importing user input from mic getting response from data
   # while True:
        #chat.inp = listen()
    chatbot.inp = input
    results = model.predict([bag_of_words(chatbot.inp, words)])[0]
    results_index = np.argmax(results)
    tag = labels[results_index]
        
    if results[results_index] >= 0.8:
        for tg in data["intents"]:
            if tg["tag"]== tag:
                responses = tg["responses"]
                chatbot.response = (random.choice(responses))
                return(chatbot.response)
                #speak(chatbot.response)
    else:
        print("i didnt get that . please try again")
        speak('i didnt get that . please try again')
  

        #workflow for tasks:

    if tag == "goodbye":
        exit()

    if tag == "search":
        
        sentences = nltk.sent_tokenize(chatbot.inp)
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
            #print(a)
        search(chatbot.inp)
pass

# define a function to get user input and show chatbot response
def get_response():
    # get user input
    user_input = input_box.get()

    # clear input box
    input_box.delete(0, tk.END)

    # show user input in output box
    output_box.insert(tk.END, "You: " + user_input + "\n")

    # get chatbot response
    results = chatbot(user_input)

    # show chatbot response in output box
    output_box.insert(tk.END, "Bot: " + results + "\n")

# define a function to run the chatbot function in a separate thread
def run_chatbot_thread():
    Thread(target=chatbot).start()

# add button to submit user input
submit_button = tk.Button(root, text="Submit", font=("Helvetica", 14), command=get_response)
submit_button.pack(pady=10)

# add button to start chatbot
start_button = tk.Button(root, text="Start Chatbot", font=("Helvetica", 14), command=run_chatbot_thread)
start_button.pack(pady=10)

# start the Tkinter event loop
root.mainloop()






