#!/bin/bash

check_dir(){
	local dir=$1
	if [ -d "$dir"]
	then
		echo " Directory exists"
		ls "$dir"
	else
		
		mkdir "$dir"
		echo "Directory created"

	fi
}
check_dir "test"

