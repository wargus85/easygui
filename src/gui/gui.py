#!/usr/bin/env python3

""" from guizero import App, Text, PushButton

def say_hello():
    text.value = "hello world"

app = App()
text = Text(app)
button = PushButton(app, command=say_hello)
app.display() """

from googlesearch import search
from random import choice
import webbrowser
import easygui as eg

eg.msgbox(msg="Tell me what you would like in a project and I shall serach Google for you. This will trigger 3 pop up windows",title='InPIration',ok_button="inspire me!")

things = []
suggestions = []

for i in range(3):
    things.append(eg.enterbox(msg="'READY>>>"))

inspiration = str(things[0]+" "+things[1]+" "+things[2])
print(inspiration) #Debug

for item in search(inspiration,tld="com.au",num=3,stop=1,pause=2):
    print(item)
    suggestions.append(item)

for i in range(len(suggestions)):
    links="\n".join(suggestions[0:])

eg.textbox(msg="Hey I found these that might be of interest, I'll open one at random after you close this message",text=links)

webbrowser.open(choice(suggestions))