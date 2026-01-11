#!/bin/bash

USERNAME=$USER
OUTPUT_PATH="/home/$USER/Downloads/GeoLite2"

read -s -p "Enter your MaxMind API License Key (will not display on screen when entered): " YOUR_LICENSE_KEY

mkdir -p $OUTPUT_PATH

for FILE_TYPE in {"ASN","City","Country"}; do
	URL="https://download.maxmind.com/app/geoip_download?edition_id=GeoLite2-$FILE_TYPE&license_key=$YOUR_LICENSE_KEY&suffix=tar.gz"
	FILE_NAME="$FILE_TYPE.tar.gz"
	wget $URL -O "$OUTPUT_PATH/$FILE_NAME"
	tar xzf "$OUTPUT_PATH/$FILE_NAME" --strip=1 -C "$OUTPUT_PATH"
done
ls $OUTPUT_PATH
