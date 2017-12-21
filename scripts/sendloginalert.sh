#!/bin/bash

while :
do
	if grep -qF "SUCCESSFUL" /root/msfspool.txt
	then
		sendEmail -f $1 -t $3 -u "owa_login SUCCESSFUL!" -m "Check your msfspool.txt log" -s smtp.gmail.com:587 -o tls=yes -xu $1 -xp $2
		sleep 15m
	fi
done

