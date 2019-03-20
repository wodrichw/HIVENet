from flask import Flask, request, url_for, redirect, render_template, flash
import os
import time
import json
import subprocess
from app.take_images import Imagetaker

RD  = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

#----- This is the functionality for the training form
@app.route('/training_form', methods = ['GET', 'POST'])
def get_training_form():
    if request.method == 'POST':
        submitted_name = request.get_json()['name']
        
        #Save state of name
        print(submitted_name)
        it.setName(submitted_name)

        #make correct directory
        # path = mkdir_path(submitted_name)
        # mkdirCall = subprocess.Popen('mkdir '+path, shell=True)
        # mkdirCall.wait()

        # if mkdirCall.returncode == 1:
        #     return json.dumps('ERROR ADDING DIRECTORY')
        return 'success';

def mkdir_path(name):
    if not os.path.exists(name):
        path = RD + "/output_dir/"
        path = path + name
        return path
    else:
        return False

def mv_pics(directory_one):
    directory_two = "~/Pictures/Webcam/*"
    cmd = "mv " + directory_two + " " + directory_one
    os.system(cmd) 

#----- This is the functionality for the recognition form
@app.route('/recognition_form', methods = ['GET', 'POST'])
def get_recognition_form():
    if request.method == 'POST':
        if request.form['submit'] == 'return_home':
            return redirect(url_for('index'))
        elif request.form['submit'] == 'start_recognition':
            strtrec = 'python realtime_facenet_git.py'
            os.system(strtrec)
            return redirect(url_for('index'))
        else:
            return render_template('recognition_form.html')
    return render_template('recognition_form.html')

@app.route('/take_face_photos', methods = ['GET'])
def get_take_photos_page():
    return  render_template('take_face_photos.html')

@app.route('/take_face_photo', methods = ['GET'])
def take_photo():
    it.take_save_image()
    return it.numImage


if __name__== '__main__':
    it = Imagetaker()
    app.run()