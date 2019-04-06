import requests 
import tarfile
import subprocess
import json
from flask import jsonify
import os

URL = "http://10.248.170.135:5000"
ROOTDIR = os.path.dirname(os.path.realpath(__file__))


def sendClassifier(ip):
    try: 
        classifierF = open(ROOTDIR+'/assets/classifier.pkl','r')
        namesF = open(ROOTDIR+'/assets/names.txt','r')
        try:
            files = {"classifier":classifierF,"names":namesF}
            r = requests.post('http://'+ip+':5000/update_classifier', files=files)
        except: 
            print("failed to send files")
        finally: 
            classifierF.close()
            namesF.close()
    except: 
        print("Files not found: " + ROOTDIR + '/assets/names.txt or ' + ROOTDIR+'/assets/classifier.pkl')

def sendToEdgeDevices():
    # Get the IP of edge device
    p = subprocess.Popen(ROOTDIR+'/scripts/getIPs.sh', shell=True, stdout=subprocess.PIPE)
    IPaddr = p.communicate()#.strip()
    for ip in IPaddr:
        if ip is not None and ip != '': 
            ip.rstrip()
            if ip[-1] == '\n': ip = ip[:-1]
            print(ip)
            sendClassifier(ip)

    print (IPaddr)

sendToEdgeDevices()
