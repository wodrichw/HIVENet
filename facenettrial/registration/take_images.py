import sys
import numpy as np
import cv2
import subprocess
import os
def make_directory(name,dataset_dir):
    # Make nodedir if does not exist
    subprocess.call("if [ -z $(ls "+dataset_dir+"| grep "+name+") ] ; then mkdir "+dataset_dir+"/"+name+" ; fi", shell=True) 

def take_save_images(name,dataset_dir):
    
    video_capture = cv2.VideoCapture(0)
    path = os.path.join(dataset_dir,name)    

    num_images = 0 
    while num_images < 30:
        ret, frame = video_capture.read()
        #cv2.imshow('frame', frame)
        cv2.imwrite(os.path.join(path,name+"_"+str(num_images)+".jpg"),frame)
        num_images += 1
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    name = sys.argv[1]
    relevant_path=os.path.dirname(os.path.abspath(__file__)) 
    dataset_dir = relevant_path + '/../datasets/data'
    make_directory(name,dataset_dir)
    take_save_images(name,dataset_dir)