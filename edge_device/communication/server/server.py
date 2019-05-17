#!/usr/bin/env python2
import os
import sys
from os.path import dirname
import subprocess
from flask import Flask, request, redirect, url_for, send_from_directory
sys.path.append(dirname(dirname(dirname(os.path.realpath(__file__)))) + "/tracking" ) 
from merge_names import *

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'assets/'

# Assemble File Paths
RD = dirname(os.path.realpath(__file__))
ED = dirname(dirname(RD))   
FS = ED + "/facenet_src"
CD = ED+"/classifiers"

# /HIVENet/edge_device/tracking/pickles
TD = ED + '/tracking'

#run recognize.py
def runRecognize():
    recognizeProc = subprocess.Popen("cd " + FS + " ; python recognize.py", shell=True)

@app.route('/update_classifier', methods=['POST'])
def updateClassifier():
    ip = request.remote_addr
    nodedir = CD+'/node_'+ip
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

@app.route('/update_tracking', methods = ['POST'])
def updateNames():
    MTD = TD + "/merge_these.pkl"
    LND = TD + "/local_names.pkl"
    request.files['names'].save(MTD)
    merge(MTD, LND)
    # Call function to do stuff from here? Is that ok?

    return "classifier updated successfully"

if __name__ == '__main__':
    os.chdir(RD)
    app.run(debug=True, host='0.0.0.0')
