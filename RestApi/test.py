import requests

Base = 'http://127.0.0.1:5000/'

'''
# this was for basic example class
response = requests.get(Base + 'example')
print(response.json())
'''
response = requests.put(Base + 'movie/1', json={'likes':10})
print(response.json())