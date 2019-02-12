import requests 
import json


# api-endpoint 
URL = "http://127.0.0.1"
  
classifierF =  open('../classifier.pkl', 'r')
classifier = classifierF.read()
r = requests.post(url = URL + "/classifier", data = json.dumps(classifier))


newNamesF = open('./newNames.txt', 'r')
newNames = newNamesF.read()
r = requests.post(url = URL + "/names", data = json.dumps(newNames))

  
  