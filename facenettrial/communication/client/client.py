import requests 
import tarfile
import subprocess
import json
from flask import jsonify
import os

URL = "http://10.248.170.135:5000"
ROOTDIR = os.path.dirname(os.path.realpath(__file__))

def addName(newName):
    with open(ROOTDIR+'assets/newNames.txt', 'a+') as nf:
        nf.writelines([newName])

def sendNewPhotos(url=URL):
    tarCmd = ROOTDIR+'/scripts/compressPhotos.sh'
    subprocess.call([tarCmd])
    fin = open(ROOTDIR+'/assets/tarPhotos/newNamesData.tar.gz', 'rb')
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

def sendAll(url=URL):
    classifierF = open(ROOTDIR+'/assets/newNames.txt', 'r')

    namesF = open(ROOTDIR+'/assets/newNames.txt', 'r')

    tarCmd = ROOTDIR+'/scripts/compressPhotos.sh'
    subprocess.call([tarCmd])
    trainingDataF = open(ROOTDIR+'/assets/tarPhotos/newNamesData.tar.gz', 'rb')

    files = {'classifier': classifierF, 'names': namesF, 'trainingData': trainingDataF}

    try:
        r = requests.post(URL+'/sync-all', files=files)
        print(r.text)
    finally:
        classifierF.close()
        namesF.close()
        trainingDataF.close()
