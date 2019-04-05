from flask import Flask, request, url_for, redirect, render_template, flash
import os
import time
import json
import subprocess
from app.take_images import Imagetaker

RD  = os.path.dirname(os.path.realpath(__file__))

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

#----- This is the functionality for the training form
@app.route('/training_form', methods = ['GET', 'POST'])
def get_training_form():
    if request.method == 'POST':
        submitted_name = request.get_json()['name']
        
        #Save state of name
        print(submitted_name)
        it.setName(submitted_name)

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
    return str(it.numImage)

@app.route('/your_photos', methods = ['GET'])
def your_photos():
    os.chdir(RD)
    if it.name == "": return "no name"
    
    p = subprocess.Popen("python align_data.py > /dev/null 2>&1 ; cp output_dir/"+it.name+"/* static/current_face/ ; ls static/current_face", shell=True, stdout=subprocess.PIPE)
    picFiles = p.communicate()[0].split('\n')[:-1]

    return render_template('your_photos.html', name=it.name, picFiles = picFiles)

if __name__== '__main__':
    it = Imagetaker()
    app.run(port=5052)