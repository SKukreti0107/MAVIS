
import tflearn
#import random
from nlp import training , output , labels , words, data, np, nltk, stemmer



#model:

net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

#remove below # to train new model
try:
    #x
    model.load("model.tflearn")
 
except:
    model.fit(training , output , n_epoch=1000, batch_size=16, show_metric=True)
    model.save("model.tflearn")



def bag_of_words(s ,words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i,w in enumerate(words):
            if w == se:
                bag[i] = 1

    return np.array(bag)
