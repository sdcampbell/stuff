#!/bin/bash

while :
do
	if grep -qF "SUCCESSFUL" /root/msfspool.txt
	then
		sendEmail -f steven.d.campbell68@gmail.com    -t steven_campbell@rapid7.com -u "owa_login SUCCESSFUL!" -m "Check your msfspool.txt log" -s smtp.gmail.com:587 -o tls=yes -xu steven.d.campbell68@gmail.com -xp $1
		sleep 15m
	fi
done

