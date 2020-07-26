#!/bin/bash

# create test arrays with overlapping values
declare -a array1=(a b c d e f g)
declare -a array2=(e f g h i j k)

#create intersection array
array3=($(comm -12 <(printf '%s\n' "${array1[@]}" | LC_ALL=C sort) <(printf '%s\n' "${array2[@]}" | LC_ALL=C sort)))

echo
echo "Array 1"
printf '%s\n' "${array1[@]}"
echo

echo "Array 2"
printf '%s\n' "${array2[@]}"
echo

echo "Array 3 - Intersection"
printf '%s\n' "${array3[@]}"
echo
