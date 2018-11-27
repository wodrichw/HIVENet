#!/bin/bash 


#
#we are using python 2.7 
#
virtualenv --system-site-packages -p python2 ./virtualfacenet

source ./virtualfacenet/bin/activate

git clone https://github.com/davidsandberg/facenet.git

cd facenet/

pip install --no-binary numpy --upgrade numpy
pip install -r requirements.txt
export PYTHONPATH=./src:./src/models:./src/align
