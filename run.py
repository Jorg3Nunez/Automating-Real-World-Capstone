#!c:/Python/python.exe

import os
import requests

# Variable declaration
path = '/data/feedback/'
myLink = 'http://<External-IP-address>/feedback/'
myFiles = os.listdir(path)

for file in myFiles:
    myData = open(path + file)
    iData = myData.read().split('\n')

    myDictionary = {"title";iData[0], "name";iData[1], "date";iData[2], "feedback";iData[3]}

    response = requests.post(myLink, json=myDictionary)

    myData.close()

print(response.status_code) 