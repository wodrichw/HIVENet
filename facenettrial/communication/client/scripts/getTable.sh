#!/bin/bash
 
if [ $(ls ipTable) ]
then
	rm ipTable
fi

if [ ! $1 ]
then
	broadcast=$(echo 10.0.0.*)
else
	broadcast=$1
fi

tmpTable=ipTable

exec $(nmap -sP $broadcast | grep $(echo ${braodcast::-1})) & > tmpTable

