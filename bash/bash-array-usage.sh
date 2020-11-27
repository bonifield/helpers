#!/bin/bash

# initialize the array
declare -a ray=()

#=============
# add all directory items to array
# wrap in parentheses = add new element, without parentheses = create one giant string
#=============

for i in `ls`; do
	ray+=("${i}")
done

#=============
# print number of elements in array, like python len()
# pound sign says count elements, at symbol says get all elements (aka count all elements)
#=============

echo "array length:"
echo ${#ray[@]}

#=============
# print whole array with printf
#=============

echo
echo "printf"
printf '%s\n' "${ray[@]}"

#=============
# print whole array with for loop
#=============

echo
echo "for loop - print whole array"
for i in "${ray[@]}"; do
	echo $i
	#or this:
	#echo ${ray[$i]}
done

#=============
# print whole array with for loop - only index keys
# bang means access keys
#=============

echo
echo "for loop - print key index list"
for i in "${!ray[@]}"; do
	echo $i
done

#=============
# print array and index number, note index starts at zero
# i = 0, loop over i and increment it for each item in the array
# index starts at 0, so add 1 to have the proper number
# based on https://stackoverflow.com/questions/38602587/bash-for-loop-output-index-number-and-element
#=============

echo
echo "key-index / value"
for ((i = 0; i < ${#ray[@]}; ++i)); do
    p=$(($i + 1))
    echo "$p,${ray[$i]}"
done

#=============
# access a specific index
# index numbers start at zero, meaning the third item is index 2
#=============
echo
echo "get item at 3rd index"
echo "${ray[2]}"
