import requests 
import tarfile
import subprocess
import json
from flask import jsonify
import os

URL = "http://127.0.0.1:5000"
ROOTDIR = os.path.dirname(os.path.realpath(__file__))

def addName(newName):
    with open(ROOTDIR+'assets/newNames.txt', 'a+') as nf:
        nf.writelines([newName])

def sendNewPhotos(url=URL):
    with open(ROOTDIR+'/assets/newNames.txt', 'r') as nf:
        names = [n.strip() for n in nf.readlines()]

    for n in names:
        tarCmd = ROOTDIR+'/scripts/compressPhotos.sh'
        subprocess.call([tarCmd, ROOTDIR, n])
        fin = open(ROOTDIR+'/assets/tarPhotos/'+n+'.tar.gz', 'rb')
        files = {'file': fin}
        try:
            r = requests.post(URL+'/training-data', files=files)
            print(r.text)
        finally:
            fin.close()

def sendNames(url=URL):
    fin = open(ROOTDIR+'/assets/newNames.txt', 'r')
    files = {'file': fin}
    try:
        r = requests.post(URL+'/names', files=files)
        print(r.text)
    finally:
        fin.close()

def sendClassifier(url=URL):
    fin = open(os.path.realpath('./classifier.pkl'))
    files = {'file': fin}
    try:
        r = requests.post(URL+'/classifier', files=files)
        print(r.text)
    finally:
        fin.close()
