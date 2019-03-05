#!/bin/bash

if [[ $# -ne 0 ]]
then
	printf "USAGE: \n./compressPhotos.sh"
	exit 1
fi

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

cd $DIR; cd ../assets/tarPhotos

outputDir=$( cd ../../../../real-time-deep-face-recognition/output_dir ; pwd )

tar -xzf newNamesData.tar.gz
for name in $(ls newNamesData); do
	if [[ ! -z $(ls $outputDir  | grep $name) ]]; then
		for i in $(seq 100); do
			if [[ -z $(ls $outputDir | grep $name'_'$i) ]]; then
				mv newNamesData/$name newNamesData/$name'_'$i
				break
			fi
		done
	fi
done
mv newNamesData/* $outputDir

# rm -rf newNamesData*
