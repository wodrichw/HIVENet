from flask import Flask, request, url_for, redirect, render_template, flash
#from celery import app as celery_app
from celery import Celery
import os
import time

#https://stackoverflow.com/questions/27539309/how-do-i-create-a-link-to-another-html-page

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

#----- This is the functionality for the training form
@app.route('/training_form', methods = ['GET', 'POST'])
def get_training_form():
    if request.method == 'POST':
        if request.form['submit'] == 'submit_name':
            submitted_name = request.form.get('textbox')
            print(submitted_name)
            if submitted_name == "":
                return render_template('training_form.html')
            else:
                #make correct directory
                path = mkdir_path(submitted_name)
                if path is not False:
                    os.mkdir(path)
                    #open up webcam -- beta release only
                    #final release will open up webcam and take pictures automatically
                    web_cmd = "cheese"
                    os.system(web_cmd)
                    mv_pics(path)
                    #configure data
                    align = "python ../Make_aligndata_git.py"
                    classifier = "python ../Make_classifier_git.py"
                    os.system(align)
                    os.system(classifier)
                    return redirect(url_for('index'))
                else:
                    error = "directory already named"
        else:
            return redirect(url_for('index'))    
    return render_template('training_form.html')

def mkdir_path(name):
    if not os.path.exists(name):
        path = "../output_dir/"
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
            strtrec = 'python ../realtime_facenet_git.py'
            os.system(strtrec)
            return redirect(url_for('index'))
        else:
            return render_template('recognition_form.html')
    return render_template('recognition_form.html')


if __name__== '__main__':
    app.run()