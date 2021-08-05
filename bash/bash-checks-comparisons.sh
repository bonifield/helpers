#!/bin/bash


echo "\$0 (name of current script): $0"
#echo "\$1-\$9 (first nine script arguments): $1 $2 $3 $4 $5 $6 $7 $8 $9"
echo "\$# (count of arguments): $#"
echo "\$@ (all arguments): $@"
echo "\$? (exit status of most recent process): $?"
echo "\$$ (process ID of running script): $$"
echo "\$USER (current username): $USER"
echo "\$HOSTNAME (machine hostname): $HOSTNAME"
echo "\$RANDOM (random number): $RANDOM"
echo "\$LINENO (current line number): $LINENO"

one=1
two=2
empty=""

#
# -eq
#
if [ ! $one -eq $two ]; then
	echo "(-eq) 1 does not equal 2"
elif [ $one -eq $two ]; then
	echo "(-eq) 1 does equal 2 in some other universe"
else
	echo "try again"
fi

#
# -ne
#
if [ $one -ne $two ]; then
	echo "(-ne) 1 does not equal 2"
elif [ $one -eq $two ]; then
	echo "(-eq) 1 does equal 2 in some other universe"
else
	echo "try again"
fi

#
# == and !=
#
if [ $one != $two ]; then
	echo "(!=) 1 does not equal 2"
elif [ $one == $two ]; then
	echo "(==) 1 does equal 2 in some other universe"
else
	echo "try again"
fi

#
# double brackets for multiple checks in one statement (but [[]] is not POSIX-safe)
#
if [[ ! $one -eq $two && ! $two -eq $one ]]; then
	echo "(-eq) 1 does not equal 2"
elif [ $one -eq $two ]; then
	echo "(-eq) 1 does equal 2 in some other universe"
else
	echo "try again"
fi

#
# -n (length check)
#
if [ -n "testword" ]; then
	echo "(-n) length of testword is greater than 0"
fi

#
# -z (zero-length check)
#
if [ -z "" ]; then
	echo "(-z) an empty string has a length of zero"
fi

#
# -gt (greater than) and -lt (less than)
#
if [ $two -gt $one ]; then
	echo "(-gt) two is greater than one"
elif [ $two -lt $one ]; then
	echo "(-lt) two is less than one in some other universe"
else
	echo "try again"
fi

#
# -ge (greater than or equal to) and -le (less than or equal to)
#
if [ $two -ge $one ]; then
	echo "(-ge) two is greater than or equal to one"
elif [ $two -lt $one ]; then
	echo "(-le) two is less than or equal to one in some other universe"
else
	echo "try again"
fi

#
# -e (file exists) (note directories are still files)
#
if [ -e /etc/passwd ]; then
	#echo "(-e) the file /home exists"
	echo "(-e) the file /etc/passwd exists"
fi

#
# -h (file exists and is a symbolic link)
#
if [ -e /sbin ]; then
	s=`readlink -f /sbin`
	echo "(-h) /sbin exists and is a symbolic link to $s"
fi

#
# -d (file exists and is a directory)
#
if [ -d /home/$USER ]; then
	echo "(-d) /home/$USER exists and is a directory"
fi

#
# -r (file exists and has read permissions)
#
if [ -r /home/$USER ]; then
	echo "(-r) /home/$USER exists and has read permissions"
fi

#
# -s (file exists and is not empty)
#
if [ -s /etc/passwd ]; then
	echo "(-s) /etc/passwd exists and is not empty"
fi

#
# -w (file exists and has write permissions)
#
if [ -w /home/$USER ]; then
	echo "(-w) /home/$USER exists and has write permissions"
fi

#
# -x (file exists and has execute permissions)
#
if [ -x /bin/ls ]; then
	echo "(-x) /bin/ls exists and has execute permissions"
fi
