#!/bin/bash

if [[ $# -ne 0 ]]
then
	printf "USAGE: \n./compressPhotos.sh"
	exit 1
fi

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

cd $DIR; cd ..
rm -rf assets/tarPhotos/newNamesData > /dev/null 2>&1
mkdir assets/tarPhotos/newNamesData

tarDir=$(realpath assets/tarPhotos)
for name in $(cat assets/newNames.txt)
do
	cp -r ../../real-time-deep-face-recognition/output_dir/$name assets/tarPhotos/newNamesData
done

cd assets/tarPhotos
tar -czf newNamesData.tar.gz newNamesData
