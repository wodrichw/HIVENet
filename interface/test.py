import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))+'/edge_device')
from flask import Flask, request, url_for, redirect, render_template, flash
import time
import json
import subprocess
from take_images import Imagetaker
from communication.client.client import sendToEdgeDevices
from facenet_src.classify import classify
from facenet_src.align_data import align as align_data
# from facenet_src.recognize import recognize

# Assemble Directory paths
RD = os.path.dirname(os.path.realpath(__file__))
ED  = os.path.dirname(RD)+"/edge_device"
dataDir = ED + "/data"
facenetDir = ED + "/facenet_src"
alignedDataDir = facenetDir+"/aligned_data"
classifierDir = ED+"/classifiers"
communicationDir = ED+"/communication"
clientDir = communicationDir+"/client"
clientAssetsDir = clientDir+"/assets"
staticDir = RD+"/static"
currentFaceDir = staticDir+"/current_face"

p = subprocess.Popen("ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1'", shell=True, stdout=subprocess.PIPE)
IPaddr = p.communicate()[0].strip()
nodedir = classifierDir+"/node_"+IPaddr 

align_data(facenetDir)
classify(facenetDir)