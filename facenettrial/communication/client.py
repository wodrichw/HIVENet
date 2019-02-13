import requests 
import tarfile
import subprocess
import json
from os import listdir


# api-endpoint 
URL = "http://127.0.0.1"
  
# classifierF =  open('../classifier.pkl', 'r')
# classifier = classifierF.read()
# r = requests.post(url = URL + "/classifier", data = json.dumps(classifier))


# with open('./newNames.txt', 'r') as nf:
#     namesRaw = nf.read()
# r = requests.post(url = URL + "/names", data = json.dumps(namesRaw))

with open('./newNames.txt', 'r') as nf:
    names = nf.readlines()
    names = [n.strip() for n in names]
  
for name in names:
    # tar = tarfile.open(name + ".tar.gz", 'w:gz')
    # nDir = "../datasets/data/" + name + '/'
    # for pic in listdir(nDir):
    #     tar.add(nDir + pic)
    # tar.close()
    with open(name + ".tar.gz", "rb") as f:
        data = f.read()
        r = requests.post(url = URL + '/training-data', data = {'name': name, 'file': data})
    
