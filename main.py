#!/usr/bin/env python3

import speech_recognition as sr
from termcolor import colored as color
import apiai
import json
import threading
from subprocess import call
from web_query import google
from web_query import wiki_search
from cap_man import abuse

BOLD = "\033[1m"   #use to bold the text
END = "\033[0m"    #use to close the bold text
CLIENT_ACCESS_TOKEN = '30cb9f273f4246239ee6b8c215673336'
ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)


try:
    r = sr.Recognizer()
    r.energy_threshold = 3500
    with sr.Microphone() as source:
        call(['clear'])
        print(color(f'{BOLD}Hola!\nAsk me anything.{END}',"green"))
        while True:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

#	while True:	
            try:
                query = r.recognize_google(audio)
    			
                print(color("                               "+BOLD+query+END+"\n","red"))
                if '*' in query:
                    abuse(query)
                request = ai.text_request()
                request.query = query  
                response = request.getresponse()
                json_data = (response.read())
                say =  json.loads(json_data)
#                print(say)
                speech = say['result']['fulfillment']['speech']
                search = speech.split(":")
                if search[0] == "Google" or search[0] == "Google and Google":
#                    thread = threading._start_new_thread(google,(search[1],)) #',' this after search[1] is user to make it a tuple
                    google(search[1])
                    print()
                elif search[0] == "Wiki" :
                    wiki_say = wiki_search(search[1])
                    print(color(f'{BOLD}{wiki_say}{END}\n','green'))
                elif search[0] == "Youtube":
                    print("")
                else :
                    print (color(f'{BOLD}{speech}{END}\n','green'))
				
            except sr.UnknownValueError:
                print (color("Listening","blue"))
except KeyboardInterrupt:
    print (color(f'{BOLD} Bye!{END}', "cyan"))

while True:
    pass
