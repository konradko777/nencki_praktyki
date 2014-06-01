#!/bin/bash

for file in *.tgz
do
	mkdir ${file:0:-4}
	tar -xf $file -C ${file:0:-4}
done
