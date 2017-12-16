#!/usr/bin/env bash

sudo hping3 -c 2 -S $1 -p $2 --tcp-timestamp
