#!/bin/bash
divide () {
local a=$1
local b=$2
if [ $b -eq 0 ]
then
	echo " Error :Division by zero"
fi
	
quotient=$(echo "scale=2;$a/$b" | bc)
remainder=$((a % b))

echo "Quotient $quotient , Remainder $remainder "

}
result=$( divide 10 3 )
echo "$result"

