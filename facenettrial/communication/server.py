import os
from flask import Flask, request, redirect, url_for, send_from_directory

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'dev/'

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file: 
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            return url_for('uploaded_file', filename=file.filename)
    return "file upload not successful"

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

if __name__ == '__main__':
	app.run(debug=True)