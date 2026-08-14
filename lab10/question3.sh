#!/bin/bash

echo "Enter a file name"
read filename

if [-f "$filename"]; then
	if [ -x "$filename"];then
		echo "File exists and is executable"
	else
		echo "File exists but is not executable"
	fi
 	echo "the file exists"
	exit 200
	echo $?

else	
	echo "file does not exist"
	exit 201
	echo$?

fi
 
echo 'outside the if-block'
exit 0




