import subprocess
import os
import communication.client.client as client
from datetime import datetime

#get root dir
RD  = os.path.dirname(os.path.realpath(__file__))
os.chdir(RD)

def insertLogStart():
    with open('hivenet.log', 'a') as f:
        f.write("\n###############################################################\n########"+datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"\n")
        
def startServer():
    insertLogStart()
    subprocess.Popen("python communication/server/server.py >> hivenet.log 2>&1", shell=True)

def trainLocalFaces():
    insertLogStart()
    subprocess.Popen(('python real-time-deep-face-recognition/Make_aligndata_git.py >> hivenet.log 2>&1;'
                      'python real-time-deep-face-recognition/Make_classifier_git.py >> hivenet.log 2>&1' ), shell=True)


def syncDevicesToClassifier():
#     client.sendNewPhotos()
    client.sendClassifier()
     

trainLocalFaces()
# syncDevicesToClassifier()
