#!/usr/bin/env python2
import os
from os.path import dirname
import subprocess
from flask import Flask, request, redirect, url_for, send_from_directory


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'assets/'
# Assemble File Paths
RD = dirname(os.path.realpath(__file__))
cmdON=RD+"""/scripts/turnOnRecognition.sh"""
cmdOFF=RD+"""/scripts/turnOffRecognition.sh"""
ED = dirname(dirname(RD))
classifiersDir = ED+"/classifiers"

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
        #restart classifier
        subprocess.call(cmdOFF, shell=True)
        subprocess.call(cmdON, shell=True)

        return "classifier updated successfully"
    else: 
        return "return failed"

if __name__ == '__main__':
    os.chdir(RD)
    app.run(debug=True, host='0.0.0.0')
    
