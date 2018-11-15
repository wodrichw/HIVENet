#!/bin/bash

sudo pip3 install -U virtualenv

virtualenv --system-site-packages -p python3 ./tensorflow

#
#simulate virtual env 
#
source ./tensorflow/bin/activate

pip install --upgrade pip 
pip install --upgrade tensorflow
