#!/bin/bash

cd "$(dirname "$0")"

pkill python*

if [ $(ifconfig | grep docker0) ]
then
	sudo ip link delete doker0
fi

if [ $(nmcli device wifi list | grep TP-Link_CAFF) ]
then
	nmcli device wifi connect TP-Link_CAFF password 04870418
fi

rm -r facenet_src/aligned_data/*
rm -r classifiers

python facenet_src/align_data.py

cd ../interface

rm -rf static/current_face/*

python interface.py &

cd ../edge_device/communication/server
python server.py &
cd ../client/
rm -rf assets/*
