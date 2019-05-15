#!/bin/bash

mypathtorec=$(pwd)"/../../facenet_src/recognize.py"
python "$mypathtorec"
export RECOG_PROC_ID=$!