#setup script for deploying server on raspberry pi
#!/bin/bash

cd /home/server
git clone https://github.com/leilanisears/10lines
chmod +x server.py
./server.py&
