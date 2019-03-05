import os
import subprocess
from flask import Flask, request, redirect, url_for, send_from_directory

## Must be run from server directory in order to work properly

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'assets/'
rootDir = os.path.dirname(os.path.realpath(__file__))

@app.route('/training-data', methods=['POST'])
def uploadTrainingData():
    handleTrainingData(request.files['file'])

def handleTrainingData(file):
    if file: 
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'tarPhotos/', file.filename))
        tarCmd = rootDir+'/scripts/decompressPhotos.sh'
        subprocess.call([tarCmd])
        return file.filename+' upload successful'
    return file.filename+" upload not successful"

@app.route('/classifier', methods=['POST'])
def uploadClassifier():
    handleClassifier(request.files['file'])

def handleClassifier(file):
    if file: 
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        return file.filename+'upload successful'
    return file.filename+" upload not successful"


@app.route('/names', methods=['POST'])
def uploadNames():
    handleNames(request.files['file'])

def handleNames(file):
    if file: 
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        appendNamesCmd = rootDir + '/scripts/'
        subprocess.call([])
        return file.filename+'upload successful'
    return "file upload not successful"



@app.route('/sync-all', methods=['POST'])
def syncAll():
    handleTrainingData(request.files['trainingData'])
    handleClassifier(request.files['classifier'])
    handleNames(request.files['names'])

    
def run():
    app.run(debug=True, port="2000")

if __name__ == '__main__':
	app.run(debug=True)
