import requests
from bs4 import BeautifulSoup as bs
from speach import speak

import pywhatkit as kit




def search(query):

    try:
        kit.info(query)
        
    except:
        '''
        url = "https://www.google.com/search?q="+ query

        result = requests.get(url)
        doc = bs(result.text, 'html.parser')
        #print(doc.prettify())

        res = doc.find( "div" , class_='BNeawe s3v9rd AP7Wnd' ).text
        print(res)
        speak(res)'''
        kit.search(query)

