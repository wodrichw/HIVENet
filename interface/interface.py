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

app = Flask(__name__)

# Disable Caching making development easier
@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/training_form', methods = ['POST'])
def get_training_form():
    submitted_name = request.get_json()['name']
    #Save state of name
    print(submitted_name)
    it.setName(submitted_name)

    return 'success'

@app.route('/take_face_photos', methods = ['GET'])
def get_take_photos_page():
    return  render_template('take_face_photos.html')

@app.route('/take_face_photo', methods = ['GET'])
def take_photo():
    it.take_save_image()
    return "submitted"

@app.route('/your_photos', methods = ['GET'])
def your_photos():
    if it.name == "": return "no name"
    
    # align photos , update current_face photos, get the name of the photo files in current_face
    cmd = """
    if test ! -d {0}
    then
        mkdir {0}
    fi
    for i in $(ls {0})
    do
        rm -r {0}/$i
    done
    cp {1}/* {0}/
    ls {0}
    """
    cmd = cmd.format(currentFaceDir, alignedDataDir+"/"+it.name)

    align_data(facenetDir)
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    picFiles = p.communicate()[0].split('\n')[:-1]

    return render_template('your_photos.html', name=it.name, picFiles = picFiles)

@app.route('/retake_photos', methods = ['GET'])
def retake_photos():
    if it.name == "": return render_template('take_face_photos.html')
    subprocess.Popen("rm -r "+alignedDataDir+"/"+it.name+" "+dataDir+"/"+it.name+"/*", shell=True)
    return render_template('take_face_photos.html')

@app.route('/submit_photos', methods = ['GET'])
def submit_photos():
    # get name of node directory for device 
    # TODO: get nodedir from classify.py

    # classify, move data to client assets and sync from
    # to all other edge devices on the network
    cmd = """
    if test ! -d {0}
    then
        mkdir {0}
    fi
    for i in $(ls {0})
    do
        rm -r {0}/$i
    done
    cp -r {1}/* {0}/
    """.format(clientAssetsDir, nodedir)

    classify(facenetDir)
    subprocess.call(cmd, shell=True)
    sendToEdgeDevices()

    return render_template('index.html')

if __name__== '__main__':
    os.chdir(RD)
    it = Imagetaker()
    app.run(port=5052)