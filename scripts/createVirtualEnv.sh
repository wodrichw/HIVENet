#!/bin/bash

sudo apt -y install python3

sudo apt -y update

sudo apt -y install python3-pip

curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
python3 get-pip.py --user

rm get-pip.py

sudo pip3 install -U virtualenv

virtualenv --system-site-packages -p python3 ./tensorflow

#
#simulate virtual env 
#
source ./tensorflow/bin/activate

pip install --upgrade pip 
pip install --upgrade tensorflow
