#!/usr/bin/env python2

import os
import subprocess
from flask import Flask, request, redirect, url_for, send_from_directory

## Must be run from server directory in order to work properly


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'assets/'
rootDir = os.path.dirname(os.path.realpath(__file__))

######################################################
# API Handleing for Beta version
####################################################@#

@app.route('/beta/update_classifier', methods=['POST'])
def updateClassifier():
    ip = request.remote_addr
    if request.files['classifier']:
        # Make nodedir if does not exist
        subprocess.call("if [ -z $(ls ../../classifiers | grep "+ip+") ] ; then mkdir ../../classifiers/node_"+ip+" ; fi", shell=True)
        request.files['classifier'].save('../../classifiers/node_'+ip+ "/classifier.pkl")
        request.files['names'].save('../../classifiers/node_'+ip+ "/names.txt")
        return "classifier updated successfully"
    else: 
        return "return failed"
def run():
    app.run(debug=True, port="2000")

if __name__ == '__main__':
    os.chdir(rootDir)
    app.run(debug=True, host='0.0.0.0')
