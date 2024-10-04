import requests     # for call api
import json
import os
from gtts import gTTS
language='en'

city=str(input("Enter the name of city "))

url = f"http://api.weatherapi.com/v1/current.json?key=781886868e114cb3a4c55406232008&q={city}&aqi=no"

r = requests.get(url)

# print(r.text)

data = json.loads(r.text)

# print(data)

print(data["current"]["temp_c"],'C')

v = str(data["current"]["temp_c"])

voice_data = gTTS(text= city+" wether is "+ v +' celsius ',lang=language,slow=False)
voice_data.save("wether.mp3")
os.system("wether.mp3")

