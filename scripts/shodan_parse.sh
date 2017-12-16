#!/usr/bin/env bash

echo 'IP$Hostname$Port$Product$Version$OS$Organization$Data' > OpenPorts.csv
for f in *.json.gz
do
    shodan parse --fields ip_str,hostnames,port,product,version,os,org,data --separator $ "$f" >> OpenPorts.csv
done
