#!/bin/bash

#(1)
var1="Testing"
var2="testing"

#(2)

if [ "$var1" \> "$var2" ]
then
	echo "$var1 is greater than $var2"
	
else
	echo "$var1 is lesser than $var2"
fi

#(3)
# The output is "Testing is greater than testing"

#(4)
echo -e "$var1\n$var2" > teststringfiles 

#(5)
sort "teststringfile"



The shell if comparision treats uppercase letters as greater than lowecase ,so it prints:
Testing is greater than testing 

The sort command uses a different order 
testing
Testing

the results are not same 



