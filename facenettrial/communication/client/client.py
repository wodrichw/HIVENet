import requests 
import tarfile
import subprocess
import json
from flask import jsonify
import os


# api-endpoint 
URL = "http://127.0.0.1:5000/training-data"


with open('assets/newNames.txt', 'r') as nf:
    names = [n.strip() for n in nf.readlines()]

for n in names:
    rootDir = os.path.dirname(os.path.realpath(__file__))
    tarCmd = rootDir+'/scripts/compressPhotos.sh'
    subprocess.call([tarCmd, rootDir, n])
    fin = open('assets/tarPhotos/'+n+'.tar.gz', 'rb')
    files = {'file': fin}
    try:
        r = requests.post(URL, files=files)
        print(r.text)
    finally:
        fin.close()
