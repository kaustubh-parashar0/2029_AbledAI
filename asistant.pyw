import speech_recognition as sr
import time
import datetime
import os
import webbrowser
import openai
from apicode import apikey
import datetime
import pyttsx3
import random
import numpy as np
import pyjokes
import sys
from pynput.keyboard import Key, Controller
keyboard = Controller()

chatStr = ""
def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"User: {query}\n Abled: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]


def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    # print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold =  0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Abled"

if __name__ == '__main__':
    print('Welcome to Abled A.I')
    print("Listening...")
    say("Welcome to Abled A,I, How may i help you ")

    while True:

        query = takeCommand()

        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"],["gmail","https://mail.google.com/mail"],["spotify", "https://open.spotify.com/"],["discord","https://discord.com/"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
        # todo: Add a feature to play a specific song
        if  "open music".lower() in query.lower():
            os.system(f"Music")

        elif "type".lower() in query.lower():
            query2 = query.replace("type","")
            time.sleep(3)
            keyboard.type(query2)

        elif "Using chat g p t".lower() in query.lower():
            ai(prompt=query)

        elif "tell me a joke ".lower() in query.lower():
            say(pyjokes.get_joke())

        elif "What is your name".lower() in query.lower():
            say("I am Abled A,I , I am here to help you , what can i do for you today ?")

        elif "Who made you".lower() in query.lower():
            say("I am Abled A,I , I was programmed by Kaustubh Parashar and Mehar Garg for the S,F,H,S code hack 2023 ")

        elif " Exit".lower() in query.lower():
            say("exiting program , Bye bye!")
            os.system("taskkill /f /im asistant.exe")

        elif "What is your favourite anime".lower() in query.lower():
            say("Being a programed AI i don't really have any mental or emotional opinions about anime. But, my creators really like Naruto.")

        elif "I am bored".lower() in query.lower():
            say("I do have my some tricks up sleeve , try asking me tell a joke or ask what is my favourite anime")
        #easter egggg !!!!!!!
        elif "shasakiy is better than Naruto".lower() in query.lower():
            say("Try saying that when you are hit with the raasingun !")
        elif "time".lower() in query.lower():
            x=datetime.datetime.now()
            say(x)


        elif "reset chat".lower() in query.lower():
            chatStr = ""

        else:
            print("Chatting...")
            chat(query)





