#!/bin/bash

read -e -p "yes or no? (y/n) " yesno
if [[ $yesno =~ [Yy] ]]; then
	echo "yes"
elif [[ $yesno =~ [Nn] ]]; then
	echo "no"
else
	echo "neither"
fi
