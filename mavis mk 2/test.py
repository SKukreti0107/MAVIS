#removing text from input
'''
text = "what is a computer"
ignore = ['what', 'is','a',' ']

qwords = text.split()
resultwords  = [word for word in qwords if word.lower() not in ignore]
result = ' '.join(resultwords)
print(result)

'''


#alarm
'''
import datetime
def alarm():
    while True:

        alarm_time = "08:21"
        current_time= datetime.datetime.now().strftime("%H:%M")
        if current_time == alarm_time:
            print("ring")
            break

alarm()'''


'''

import pyttsx3
engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[5].id)
engine.setProperty('rate',170)

def speak(Text):
    engine.say(text=Text)
    engine.runAndWait()

speak("good morning sir ")

'''


#play and search info
'''

from unicodedata import name
import pywhatkit as kit
import requests
from bs4 import BeautifulSoup as bs

#kit.playonyt("Most Extreme Collections! by Beasts Reacts")
#kit.info("what is the maximum height of blackbird")
#kit.search("how high can f 35 fly")

'''

'''

url = "https://www.google.com/search?q=where am i?"

result = requests.get(url)
doc = bs(result.text, 'html.parser')
#print(doc.prettify())

res = doc.find( "div" , class_='BNeawe s3v9rd AP7Wnd' ).text
print(res)
'''
'''





import nltk
from nltk.corpus import stopwords 
from search import search
from nltk.tokenize import word_tokenize, sent_tokenize

# Function to extract the proper nouns 


def ProperNounExtractor(text):
    
    #print('PROPER NOUNS EXTRACTED :')
    
    sentences = nltk.sent_tokenize(text)
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        words = [word for word in words if word not in set(stopwords.words('english'))]
        tagged = nltk.pos_tag(words)
        x = []
        str1 = " "
        for (word, tag) in tagged:
            if tag =='NN': # If the word is a proper noun
                x.append(word)       
        #print(x)
        a=str1.join(x)
        print(a)

    
text =  "when is spiderman no way home releasing "

ProperNounExtractor(text)

'''
'''
import pyjokes
print(pyjokes.get_joke())

str = f'hello{name} 
'''

'''
import wolframalpha
#app_id = "EUA7EU-73QT69E7E5"



# Define the chatbot function
def chatbot(app_id):
    # Initialize the Wolfram Alpha client
    client = wolframalpha.Client(app_id)
    
    print("Hello! I'm a math chatbot. How can I help you today?")

    while True:
        # Get user input
        user_input = input().lower()

        # Check for exit command
        if user_input in ['quit', 'exit', 'bye']:
            print("Goodbye!")
            break

        # Query the Wolfram Alpha API
        res = client.query(user_input)

        # Print the result
        try:
            result = next(res.results).text
            print("The answer is:", result)

        # Handle errors
        except StopIteration:
            print("I'm sorry, I didn't understand your question.")

chatbot('EUA7EU-73QT69E7E5')'''






'''


import requests

# Set up authentication
api_key = '<your-api-key>'
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

# Define task parameters
task_name = 'Buy groceries'
task_due_date = '2023-03-05T00:00:00Z'
task_list_id = '<your-task-list-id>'

# Create task payload
task_payload = {
    'title': task_name,
    'dueDateTime': {
        'dateTime': task_due_date,
        'timeZone': 'UTC'
    },
    'listId': task_list_id
}

# Make API request to create task
response = requests.post('https://graph.microsoft.com/v1.0/me/tasks', headers=headers, json=task_payload)

# Check if task was created successfully
if response.status_code == 201:
    print('Task created successfully!')
else:
    print('Error creating task:', response.text)
'''

'''

import spacy
from spacy.tokens import Doc
from spacy.language import Language

# Define the entities
entities = {
    "PERSON": ["John", "Jane", "Michael", "Sarah"],
    "DATE": ["today", "tomorrow", "next week", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
    "TIME": ["morning", "afternoon", "evening", "night", "AM", "PM"]
}

# Define the custom pipeline component
@Language.component("extract_entities")
def extract_entities(doc):
    for ent in doc.ents:
        if ent.label_ in entities:
            continue
        elif ent.text in entities[ent.label_]:
            ent_kb = doc.vocab.strings.add(ent.text)
            Doc.set_extension(f"{ent.label_}_lemma", getter=lambda ent: ent.text.lower(), force=True)
            doc.ents = list(doc.ents) + [(ent_kb, ent.start_char, ent.end_char, ent.label_)]
    return doc

# Load the spaCy model and add the entities and custom pipeline component
nlp = spacy.load("en_core_web_sm")
for ent, values in entities.items():
    patterns = [{"LOWER": val.lower()} for val in values]
    nlp.vocab.add_label(ent)
    nlp.vocab.add_flag(lambda s: s.lower() in values, spacy.attrs.IS_ENT)
    nlp.vocab.add_patterns([{"label": ent, "pattern": patterns}])
nlp.add_pipe("extract_entities", after="ner")

# Example string
example_string = "John and Jane are meeting tomorrow morning at 10 AM."

# Extract entities from the string
doc = nlp(example_string)
for ent in doc.ents:
    print(ent.label_, ent.text, ent._.get(f"{ent.label_}_lemma"))
'''



import spacy
from spacy.tokens import Span
from spacy.matcher import PhraseMatcher
from spacy.language import Language

nlp = spacy.load("en_core_web_sm")
matcher = PhraseMatcher(nlp.vocab)

# Define entities and patterns
entities = [
    {"label": "sad", "value": "unhappy", "sorrowful" },
    {"label": "GPE", "value": "San Francisco"},
    {"label": "PERSON", "value": "Steve Jobs"},
    {"label": "ANY", "value": " "},
    {"label": "query", "value": "solve                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             "},
]

patterns = [nlp(entity["value"]) for entity in entities]
matcher.add("Entities", None, *patterns)

# Define custom component for entity extraction
@Language.component("extract_entities")
def extract_entities(doc):
    matches = matcher(doc)
    spans = [Span(doc, start, end, label=match_id) for match_id, start, end in matches]
    doc.ents = spans
    return doc

nlp.add_pipe("extract_entities", after="ner")

# Test the entity extraction
text = "Steve Jobs founded Apple in San Francisco"
doc = nlp(text)

for ent in doc.ents:
    print(ent.label_, ent.text)



'''
import spacy

# Load the Spacy model
nlp = spacy.load("en_core_web_sm")

# Define the text to be analyzed
text = "I live in New York, but I'm flying to Paris next week."

# Analyze the text with Spacy
doc = nlp(text)

# Extract the location entities
locations = []
for entity in doc.ents:
    if entity.label_ == "GPE":  # GPE stands for "geo-political entity"
        locations.append(entity.text)

# Print the extracted locations
print(locations)

a = locations[0]
print(a)
'''