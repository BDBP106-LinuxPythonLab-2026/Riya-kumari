#!/bin/bash

echo 'Enter your age: '
read age


if [ "$age" -ge 18 ] 
 then

	echo "You are an adult"
else
	echo "you are a minor"
fi



