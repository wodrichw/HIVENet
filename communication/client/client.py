import requests 
import tarfile
import subprocess
import json
from flask import jsonify
import os

RD = os.path.dirname(os.path.realpath(__file__))

def sendClassifier(ip):
    try: 
        classifierF = open(RD+'/assets/classifier.pkl','r')
        namesF = open(RD+'/assets/names.txt','r')
        try:
            files = {"classifier":classifierF,"names":namesF}
            r = requests.post('http://'+ip+':5000/beta/update_classifier', files=files)
        except: 
            print("failed to send files")
        finally: 
            classifierF.close()
            namesF.close()
    except: 
        print("Files not found: " + RD + '/assets/names.txt or ' + RD+'/assets/classifier.pkl')
def sendToEdgeDevices():
    # Get the IP of edge device
    p = subprocess.Popen(RD+'/scripts/getIPs.sh', shell=True, stdout=subprocess.PIPE)
    IPaddr = p.communicate()#.strip()
    for ip in IPaddr:
        if ip is not None and ip != '': 
            ip.rstrip()
            print(ip)
            sendClassifier(ip)

    print (IPaddr)

sendToEdgeDevices()
