#!/bin/bash

if [[ $# -le 1 ]] || [[ $# -ge 3 ]]
then
	printf "USAGE: ./decompressPhotos.sh <path> <fileName>
		Note: <path> is the absolute path to the client or server directory"
	exit 1
fi

cd $1
tarDir=$(realpath assets/tarPhotos)
dev=$(realpath assets)
cd ../../datasets/data
mv $tarDir/$2 .
tar -xzf $2
rm $2
