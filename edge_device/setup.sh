#!/bin/bash

cd "$(dirname "$0")"

pkill python*

if [[ $(ifconfig | grep docker0) ]] ; then
	sudo ip link delete doker0
fi

nmcli device wifi connect TP-Link_CAFF password 04870418

rm -r facenet/align_data/*
rm -r classifiers

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
