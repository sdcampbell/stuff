#!/bin/bash

cat creds.csv | cut -d ',' -f 4 | cut -d '\' -f 2 | sed 's/.$//'
