#!/bin/bash

cd "$(dirname "$0")"

pkill python*

rm -r output_dir/*
rm -r ../classifiers

if [ ! $(ls static | grep current_face) ] ; then
	mkdir static/current_face
fi

rm -rf static/current_face/*

python interface.py &
python align_data.py
python classify.py

cd ../communication/server
python server.py &
cd ../client/
rm -rf assets/*
