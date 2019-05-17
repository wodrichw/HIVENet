#!/bin/bash

cd "$(dirname "$0")"

#Hello
pkill python*

# #im not sure why we have docker here 
# if [ $(ifconfig | grep docker0) ]
# then
# 	sudo ip link delete doker0
# fi

# # we want to automatically connect to TP-Link_CAFF
# if [ $(nmcli device wifi list | grep TP-Link_CAFF) ]
# then
# 	nmcli device wifi connect TP-Link_CAFF password 04870418
# fi

# clear all data from aligned_data/ 
rm -r facenet_src/aligned_data/*

# all classifiers from previious builds. 
rm -r classifiers

# create the classifiers file here. we did it this way because we cannot store empty directories in git Q: i wonder if this is the same for aligned_data?
mkdir classifiers

# initialize data
cp -r base_data/kamilla/ data/kamilla

# align our dataset 
python facenet_src/align_data.py

# classify our dataset
python facenet_src/classify.py

cd ../interface

rm -rf static/current_face/*

# starts the interface 
python interface.py &

# start server
cd ../edge_device/communication/server
python server.py &


# clean client folder
cd ../client/
rm -rf assets/*