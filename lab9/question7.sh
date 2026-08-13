#!/bin/bash
mass=1
speed=3*10^8
energy=$(bc << EOF
$mass*$speed*$speed
EOF
)
echo "calculates energy is:$energy"


