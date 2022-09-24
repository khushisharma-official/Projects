# OPERATIONS THIS CHAT BOT CAN PERFORM :- 
### hi / hello / hey / hello there...
### play music / please play music / start song / start music
### tell me date / date / what's the date
### show time
### tell me news
### wether report

from datetime import datetime as dt
import os, random
import bs4
import urllib.request as url
import json
import pandas as pd

greetIntent = ["hi", "hello", "hey", "hi there", "hello there", "hey there"]
dateIntent = ["date", "tell me date", "what's the date", "please tell me date"]
timeIntent = ["time", "tell me time", "what's the time", "please tell me time"]
musicIntent = ["play music", "please play music", "music", "start song", "song"]
weatherIntent = ["weather", "weather report", "tell me weather report"]
newsIntent = ["news", "tell me news", "news report"]

chat = True
while chat:
    msg = input("Enter your message : ")

    if msg in greetIntent:
        print("Hello User...")
        
    elif msg in dateIntent:
        currentDate = dt.now().date()
        print("Date is",currentDate.strftime("%d %b, %Y, %a"))

    elif msg in timeIntent:
        currentTime = dt.now().time()
        print("Current Time is",currentTime.strftime("%I:%M:%S,%p"))

    elif msg in musicIntent:
        path = r"C:\Users\DVS\Desktop\Desktop\KAY\1_MY_MUSIC"
        os.chdir(path)
        songs = os.listdir()
        song = random.choice(songs)
        os.startfile(song)

    elif msg in newsIntent:       
        api_key = "pub_7958eb37fb5e38fcbeee53f1ee007c949b06&q"
        path = f"https://newsdata.io/api/1/news?apikey={api_key}=india%20news&country=in&language=en"    
        response = url.urlopen(path)
        data = json.load(response)
        print("***** Top 10 News Headlines *****")
        for i in range(10):
            print(i+1, data["results"][i]["title"])

    elif msg in weatherIntent:
        key = "789b88eeaf7786700f2e3b3ecf0f63c0"
        lat = 28.644800         #For Delhi only
        lon = 77.216721         #For Delhi only
        path = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}"
        response = url.urlopen(path)
        data = json.load(response)
        weatherData = []
        weatherData.append(data["main"])
        df2 = pd.DataFrame(weatherData)
        print(df2.head())

    elif msg == "bye":
        print("Bye User...")
        chat = False
        break
    else:
        print("I don't Understand...")