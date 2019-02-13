import requests 
import tarfile
import subprocess
import json
from flask import jsonify
from os import listdir


# api-endpoint 
URL = "http://127.0.0.1"

fin = open('dev/cesilia.tar.gz', 'rb')
files = {'file': fin}
try:
  r = requests.post(URL, files=files)
  print(r.text)
finally:
    fin.close()
  