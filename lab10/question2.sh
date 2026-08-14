#!/bin/bash

echo enter filename:

read file
if [ -f "$file" ]; then
       echo "file exists"	

	if [ -x "$file" ]; then
	echo "the file exits and is executable"
else
		
	echo "the file is not executable"
	fi
else
	echo "the file does not exists"
fi








