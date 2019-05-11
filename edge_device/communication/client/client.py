import requests 
import tarfile
import subprocess
import json
from flask import jsonify
import os

# Assemble File Paths
def sendClassifier(ip, RD=os.path.dirname(os.path.realpath(__file__))):
    try: 
        classifierF = open(RD+'/assets/classifier.pkl','r')
        namesF = open(RD+'/assets/names.txt','r')
        print classifierF
        print namesF
        try:
            files = {"classifier":classifierF,"names":namesF}
            r = requests.post('http://'+ip+':5000/update_classifier', files=files)
            print(ip, "sent successfully")
        except: 
            print(ip, "failed to send files")
        finally: 
            classifierF.close()
            namesF.close()
    except: 
        print("Files not found: " + RD + '/assets/names.txt or ' + RD+'/assets/classifier.pkl')

def sendToEdgeDevices(RD=os.path.dirname(os.path.realpath(__file__))):
    # Get the IP of edge device
    p = subprocess.Popen(RD+'/scripts/getIPs.sh', shell=True, stdout=subprocess.PIPE)
    IPaddr = str(p.communicate()[0]).split(',')
    print IPaddr
    for ip in IPaddr:
        sendClassifier(ip, RD)


if __name__ == "__main__":
    sendToEdgeDevices()