#!/bin/bash

mkdir ~/server
cd server

wget https://raw.githubusercontent.com/leilanisears/main/honeypot.py
chmod +x honeypot.py

echo "Starting server on port 4444"

#process will run infinitely
#when running script, bg the process
#eventually, move to daemon service

while true; do ./honeypot.py --port 4444; done



