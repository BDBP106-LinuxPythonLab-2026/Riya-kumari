#!/bin/bash
read -ra numbers < nums.txt
echo "the numbers are:"
for i in "${numbers[@]}"
do 
	echo $i
done
echo "Double numbers:"
for i in "${numbers[@]}"
do
	echo $((i*2))
done	

