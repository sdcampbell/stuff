#!/bin/bash

# Steve Campbell @lpha3ch0

if [ $# -eq 0 ]; then
    echo "Usage: Login to https://connect.data.com. Perform your search and copy and paste the table of results into a text file. Provide the path to the text file as the command line argument."
    exit 1
fi

cat $1 | gsed -e 's/^[ \t]*//' | tr -s '\t' | gsed 's/Direct Dial Available\s*//' | gsed 's/I Own This\s*//' | sed 's/,//' | awk '{print $2,$1}'

# Convert First Last name to usernames:
# Convert First Last to first initial last name : awk '{print tolower(substr($1,1,3) $2)}’
# Convert First Last to first.last : awk '{print tolower($1 “." $2)}
# Convert First Last to firstlast : awk '{print tolower($1 $2)}’