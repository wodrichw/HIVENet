import os
import subprocess
from flask import Flask, request, redirect, url_for, send_from_directory

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'assets/'

@app.route('/training-data', methods=['POST'])
def uploadTrainingData():
    file = request.files['file']
    if file: 
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'tarPhotos/', file.filename))
        rootDir = os.path.dirname(os.path.realpath(__file__))
        tarCmd = rootDir+'/scripts/decompressPhotos.sh'
        subprocess.call([tarCmd, rootDir, file.filename])
        return file.filename+' upload successful'
    return file.filename+" upload not successful"

@app.route('/classifier', methods=['POST'])
def uploadClassifier():
    file = request.files['file']
    if file: 
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        return file.filename+'upload successful'
    return file.filename+" upload not successful"

@app.route('/names', methods=['POST'])
def uploadNames():
    file = request.files['file']
    if file: 
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        return url_for('uploaded_file', filename=file.filename)
    return "file upload not successful"
    
if __name__ == '__main__':
	app.run(debug=True)