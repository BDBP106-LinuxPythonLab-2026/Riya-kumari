#!/bin/bash

#diffrence between -e,-s,-f use of if-block


# -e checks if the file/directory exists.

if [ -e "$filename" ]
read filename
then
	echo "file is exists"
else
	echo "file doesnot exists"
fi

# -s check file exists and is not empty
 if [ -s "$filename" ]
read filename
then
    echo "file is not empty"
else
	echo "file is  empty"

fi


# -f check if it is a regular file 
 
if [ -f "$filename" ]
read filename
then 
	echo "it is a regular file"
else 
	echo "it is not a regular file"
fi

