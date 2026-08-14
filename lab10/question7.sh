#!/bin/bash

# Getting the username of the logged-in user
logged_in_user=$(whoami)

#checking if the user is logged in
if [ -n "$logged_in_user" ]
then
	echo "The logged -in user is: $logged_in_user"
else
	echo "user is not logged in"
fi

#corrected the ")" into "]" and removed the semicolon in line5
#corrected the variable name in line 7

