#!/bin/bash

# =~ is a softmatch, == is equality

funcName () {
	read -e -p "Enter your first name: " name
	if [[ $name =~ ^[A-Z]{1}[a-z]{1,99}+$ ]]; then
		echo "Your first name is $name."
	elif [[ $name =~ ^[a-z]{1,99}+$ ]]; then
		echo "Your name starts with a capital letter!  Try again!"
		funcName
	else
		echo "Names only have letters!  Try again!"
		funcName
	fi
}

funcNum () {
	read -e -p "Enter a single-digit number 0-9: " num
	if [[ $num =~ ^[0-9]{1}$ ]]; then
		echo "You input $num."
		while [[ $num -lt 10 ]]; do
			echo "Incrementing $num until equal to 10."
			num=$((num+1))
			echo -e "\tCurrent value after loop: $num"
		done
	else
		echo "Only input a single-digit number!"
		funcNum
	fi
}

funcName
funcNum

echo
echo "Single For loop 1-5:"
for i in {1..5}; do echo $i; done
echo "Single For loop for accessing items in a directory:"
for i in `ls ~`; do echo $i; done
echo "Nested For loop:"
for x in {1..2}; do for z in {3..4}; do echo "$x$z"; done; done
echo "Looping Substitution"
echo {1..2}{3..4}
echo "Looping with Variable Substitution"
echo "$USER"{01..05}
