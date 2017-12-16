#!/usr/bin/env bash

while read line; do
	name=$(echo $line | sed -e 's/\//_/g')
	shodan download $name net:$line
done < internets.txt

echo 'IP$Hostname$Port$Product$Version$OS$Organization$Data' > OpenPorts.csv
for f in *.json.gz
do
    shodan parse --fields ip_str,hostnames,port,product,version,os,org,data --separator $ "$f" >> OpenPorts.csv
done

rm *.json.gz

