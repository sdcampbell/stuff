#!/bin/bash

gobuster -k -w /opt/SecLists/Discovery/Web_Content/raft-large-directories.txt -t $1 -u $2

