#!/usr/bin/env bash

if [ -z "$1" ]
  then
    echo "Usage: scan.sh <hostname>"
    exit 1
fi

mkdir $1

IP=$(ping -c 1 $1 | grep 'PING' | cut -d '(' -f 2 | cut -d ')' -f 1)
masscan --open -sS -p 0-65535 $IP --rate=10000 -oG $1/$1-masscan.gnmap
cat $1/$1-masscan.gnmap | tr -s " " | cut -d ' ' -f 2 | awk '!/Masscan/ && !/Ports/' | sort -u > $1/hosts.txt
cat $1/$1-masscan.gnmap | tr -s " " | cut -d ' ' -f 4 | cut -d '/' -f 1 | grep '^[1-9]' | sort -u > $1/ports.txt
ports=$(awk -vORS=, '{ print $1 }' $1/ports.txt | sed 's/,$/\n/')
nmap --open -sS -Pn -p $ports -sV -oA $1/$1-TCP -iL $1/hosts.txt
nmap --open -sU --top-ports 10 -oA $1/$1-UDP -iL $1/hosts.txt
./gnmapper.sh *.gnmap > $1/openports.csv

