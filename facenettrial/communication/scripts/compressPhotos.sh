#!/bin/bash

cd ../../datasets/data
tar -czf $1.tar.gz $1
mv $1.tar.gz ../../communication
