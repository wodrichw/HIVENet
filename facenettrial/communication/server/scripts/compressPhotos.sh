#!/bin/bash

if [[ $# -le 1 ]] || [[ $# -ge 3 ]]
then
	printf "USAGE: \n./compressPhotos.sh <rootDir> <name>\n"
	exit 1
fi

cd $1
tarDir=$(realpath assets/tarPhotos)
cd ../datasets/data
tar -czf $2.tar.gz $2
mv $2.tar.gz $tarDir
