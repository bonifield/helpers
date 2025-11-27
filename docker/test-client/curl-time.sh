#!/bin/bash

while true; do
	# set using environment variables in docker-compose.yml
	curl $API_HOST:$API_PORT >> $OUTPUT_FILE
	# this sleep occurs before a graceful container shutdown
	sleep 5
done
