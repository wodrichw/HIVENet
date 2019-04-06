#!/bin/bash

routerIP=$(ip route | grep default | awk '{print $3}')
myIP=$( ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1' )
subNet=$(echo $myIP | grep -Eo '^([0-9]*\.){3}')
connectedDevs=$(nmap -sP $subNet* | grep -Eo $subNet[0-9]* | grep -v $myIP | grep -vw $routerIP)

# if no connected device just run it twice
if [ ! $connectedDevs ] ; then
    nmap -sP $subNet* | grep -Eo $subNet[0-9]* | grep -v $myIP | grep -vw $routerIP
fi

echo $connectedDevs
