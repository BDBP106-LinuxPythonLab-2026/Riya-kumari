#!/bin/bash

#To check if a string is empty or not

string1="string"

if [ -z "string" ]
then
	echo "string is empty"
else
	echo "string is not empty"
fi


string2="string"
if [ -n "string" ]
then
	echo "string is empty"
else 	
        echo "string is not empty"
fi

	


