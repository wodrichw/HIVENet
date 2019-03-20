import sys
import numpy as np
import cv2
import subprocess
import os

class Imagetaker:
    def __init__(self):
        self.name = ""
        self.numImage = 0
        self.relevant_path=os.path.dirname(os.path.abspath(__file__)) 
        p = subprocess.Popen('cd '+self.relevant_path+'; cd ../../datasets/data ; echo $PWD', shell=True, stdout= subprocess.PIPE)
        self.dataset_dir = p.communicate()[0][:-1]

    def setName(self, name):
        self.numImage = 0
        self.name = name
        self.make_directory()

    def make_directory(self):
        # Make nodedir if does not exist
        subprocess.call("if [ -z $(ls "+self.dataset_dir+"| grep "+self.name+") ] ; then mkdir "+self.dataset_dir+"/"+self.name+" ; fi", shell=True) 

    def take_save_image(self):
        if self.name == "": return
        video_capture = cv2.VideoCapture(0)
        path = os.path.join(self.dataset_dir,self.name)    

        ret, frame = video_capture.read()
        cv2.imwrite(os.path.join(path,self.name+"_"+str(self.numImage)+".jpg"),frame)
        self.numImage += 1
        video_capture.release()
        cv2.destroyAllWindows()