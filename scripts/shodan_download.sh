#!/usr/bin/env bash

while read line; do
	name=$(echo $line | sed -e 's/\//_/g')
	shodan download $name net:$line
done < internets.txt

