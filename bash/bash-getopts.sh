#!/bin/bash

while getopts ":a:b:c:d:e:f:" opt; do
        case $opt in
                a)
                        alpha=${OPTARG}
                        echo "-a set to ${alpha}"
                        ;;
                b)
                        bravo=${OPTARG}
                        echo "-b set to ${bravo}"
                        ;;
                c)
                        charlie=${OPTARG}
                        echo "-c set to ${charlie}"
                        ;;
                d)
                        delta=${OPTARG}
                        echo "-d set to ${delta}, and falls through to -e"
                        ;&
                e)
                        echoo=${OPTARG}
                        echo "-e on the first loop will inherit -d OPTARG and -e on the second loop"
                        echo "-e set to ${echoo}, and falls through to -f"
                        echo "each loop through -e triggers -f"
                        ;&
                f)
                        echo "1) -f triggered by -e"
                        echo "2) -f does not need an argument"
                        ;;
                \?)
                        echo "Invalid option -${OPTARG}" >&2
                        ;;
        esac
done

#  ./getoptsExample.sh -a ALPHA -b BRAVO -c CHARLIE -d DELTA -e ECHO -z
#  -a set to ALPHA
#  -b set to BRAVO
#  -c set to CHARLIE
#  -d set to DELTA, and falls through to -e
#  -e on the first loop will inherit -d OPTARG and -e on the second loop
#  -e set to DELTA, and falls through to -f
#  each loop through -e triggers -f
#  1) -f triggered by -e
#  2) -f does not need an argument
#  -e on the first loop will inherit -d OPTARG and -e on the second loop
#  -e set to ECHO, and falls through to -f
#  each loop through -e triggers -f
#  1) -f triggered by -e
#  2) -f does not need an argument
###### NOTE next two lines are solely because of using -f
#  1) -f triggered by -e
#  2) -f does not need an argument
#  Invalid option -z

