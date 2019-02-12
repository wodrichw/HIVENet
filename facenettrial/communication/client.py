import requests 
import json


# api-endpoint 
URL = "http://127.0.0.1"
  
classifierF =  open('../classifier.pkl', 'r')
classifier = classifierF.read()
r = requests.post(url = URL + "/classifier", data = json.dumps(classifier))


namesF = open('./newNames.txt', 'r')
namesRaw = namesF.read()
names = namesF.readlines()

names = [n.strip() for n in names]
r = requests.post(url = URL + "/names", data = json.dumps(namesRaw))

  
  