#!/usr/bin/env bash


if [ "$#" -ne 2 ]; then
	echo “Author: Steve Campbell @lpha3ch0”
	echo “Purpose: Takes crackmapexec --ntds output and mashes it together with hashcat output to match usernames with plaintext passwords.”
	echo “Usage: cme-hashsmash.sh \<cme ndtds.dit file\> \<hashcat output file\>”
	exit 1
fi

# Remove color codes from crackmapexec output.
gsed -r "s/\x1B\[(([0-9]{1,2})?(;)?([0-9]{1,2})?)?[m,K,H,f,J]//g" $1 > $1.nocolor

while read -r line; do
	read -r user < <(echo $line | cut -d ':' -f 1)
	hash=$(echo $line | cut -d ':' -f 4)
	plaintext=$(cat $2 | grep $hash)
	if [ "$plaintext" ]
	  then
	    echo -e "$user:$plaintext"
	fi
done<$1.nocolor
