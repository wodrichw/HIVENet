#!/usr/bin/env python2
import os
import sys
from os.path import dirname
import subprocess
from flask import Flask, request, redirect, url_for, send_from_directory
sys.path.append(dirname(dirname(dirname(os.path.realpath(__file__))))+'/tracking')
from people import People


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'assets/'

# Assemble File Paths
RD = dirname(os.path.realpath(__file__))
ED = dirname(dirname(RD))   
FS = ED + "/facenet_src"
classifiersDir = ED+"/classifiers"

# /HIVENet/edge_device/tracking/pickles
namesDir = ED + '/tracking/pickles'

#run recognize.py
def runRecognize():
    recognizeProc = subprocess.Popen("cd " + FS + " ; python recognize.py", shell=True)

@app.route('/update_classifier', methods=['POST'])
def updateClassifier():
    ip = request.remote_addr
    nodedir = classifiersDir+'/node_'+ip
    if request.files['classifier']:
        # Make nodedir if does not exist
        cmd="""
        if test ! -d {0}
        then
            mkdir {0}
        fi""".format(nodedir)
        subprocess.call(cmd, shell=True)
        request.files['classifier'].save(nodedir+"/classifier.pkl")
        request.files['names'].save(nodedir+"/names.txt")
        return "classifier updated successfully"
    else: 
        return "return failed"

@app.route('/update_names', methods = ['POST'])
def updateNames():
    if request.method == 'POST':
        f = request.files['names']
        f.save(namesDir + '/temp.pkl')
        return "file uploaded successfully"
    # if request.files['names']:
    #     request.files['names'].save(namesDir + '/temp.pkl')

@app.route('/update_tracking', methods = ['POST'])
def updateTracking():
    key = request.data['people_key']
    location = request.data['location']
    recognizeProc.kill()
    people = People()
    people.add_location(key, location)
    del people
    runRecognize()



if __name__ == '__main__':
    os.chdir(RD)
    runRecognize()
    app.run(debug=True, host='0.0.0.0')
