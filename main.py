#!/usr/bin/env python3

import speech_recognition as sr
from termcolor import colored as color
import apiai
import json
import threading
from forecast import weather_current
from play import play_song
from add_to_do import make_todo
from add_to_do import list_todo
from subprocess import call
from web_query import google,wiki_search
#from web_query import wiki_search
from cap_man import abuse
from database import log,get_log
from myemailc import mail_send

BOLD = "\033[1m"   #use to bold the text
END = "\033[0m"    #use to close the bold text
CLIENT_ACCESS_TOKEN = '__key__'
ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)


try:
    r = sr.Recognizer()
#    r.energy_threshold = 3500
    with sr.Microphone() as source:
        call(['clear'])
        print(color(f'🤖 {BOLD}Hola!\n🤖 Ask me anything.{END}',"green"))
        while True:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

#	while True:	
            try:
                query = r.recognize_google(audio)
    			
                print(color(f'                                 {BOLD}{query}{END}\n','red'))
                if '*' in query:
                    abuse(query)
                
                log(query)
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
                    print(color(f'🤖 {BOLD}{wiki_say}{END}\n','green'))
                elif search[0] == "log":
                    logs = get_log()
                    for i,logg in enumerate(logs):
                        print(color(f'{BOLD}{i+1}. {logg[0]}{END}','green'))
                elif search[0] == "Youtube":
                    thread = threading._start_new_thread(play_song,(search[1],))
                    print("")
                elif search[0] == "temp":
                    weather_current()
                elif search[0] == "send email":
                    mail_send(search[1])
                elif search[0] == "todolist and todolist" or search[0] == "todolist and todo":
                    todo_list = list_todo()
                    print(color(f'🤖 {BOLD}{todo_list}{END}','green'))
                elif search[0] == "addtodo":
                    make_todo(query)
                    print(color(f'🤖 {BOLD}Added successfully{END}','green'))
                elif search[0]=="todo" or search[0]=="todo and todo":
                    print(color(f'🤖 {BOLD}start saying your to do list{END}\nAnd say "add" at starting','green'))
                else :
                    print (color(f'🤖 {BOLD}{speech}{END}\n','green'))
				
            except sr.UnknownValueError:
                print (color("Listening","blue"))
except KeyboardInterrupt:
    print (color(f'🤖 {BOLD} Bye!{END}', "cyan"))

try:
    while True:
        pass


except KeyboardInterrupt:
    print() 
