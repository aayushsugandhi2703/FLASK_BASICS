import requests

Base = 'http://127.0.0.1:5000/'

data =[ {"name": 'movie1', "views": 10000},
        {"name": 'movie2', "views": 20000},
        {"name": 'movie3', "views": 30000}
    ]

for i in range(len(data)):
    response = requests.put(Base + 'video/' + str(i), json=data[i])
    print(response.json())
input()
response = requests.delete(Base + 'video/2')
print(response)
input()
response = requests.get(Base + 'video/1')   
print(response.json()) 
