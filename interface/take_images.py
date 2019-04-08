import sys
import cv2
import subprocess
import os
from datetime import datetime

# Assemble directory paths
RD = os.path.dirname(os.path.abspath(__file__)) 
dataDir = os.path.dirname(RD)+"/edge_device/data"

class Imagetaker:
    def __init__(self):
        self.name = ""

    def setName(self, name):
        self.numImage = 0
        self.name = name
        self.make_directory()

    def make_directory(self):
        # Make nodedir if does not exist
        subprocess.call("if [ -z $(ls "+dataDir+"| grep "+self.name+") ] ; then mkdir "+dataDir+"/"+self.name+" ; fi", shell=True) 

    def take_save_image(self):
        if self.name == "": return
        video_capture = cv2.VideoCapture(0)
        path = os.path.join(dataDir,self.name)    

        ret, frame = video_capture.read()
        cv2.imwrite(os.path.join(path,self.name+"_"+str(datetime.now().time())+".jpg"),frame)
        video_capture.release()
        cv2.destroyAllWindows()