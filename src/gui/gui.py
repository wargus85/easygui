#!/usr/bin/env python3

from guizero import App, Text, PushButton

def say_hello():
    text.value = "hello world"

app = App()
text = Text(app)
button = PushButton(app, command=say_hello)
app.display()