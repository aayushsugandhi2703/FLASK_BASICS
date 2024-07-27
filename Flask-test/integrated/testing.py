import requests
import json

Base = "http://127.0.0.1:5000/"

data = [{"name": "video1"},
        {"name": "video2"},
        {"name": "video3"}]

for i in range (len(data)):
    response = requests.put(Base + "video/" + str(i), json=data[i])
    print(response.json())
input()
response = requests.get(Base + "video/1")
print(response.json())