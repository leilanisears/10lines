# JULY 15TH ---------------------

import argparse
import socket
import pickle

parser = argparse.ArgumentParser(description='Long story, I will explain later')
parser.add_argument('-port', '--p', type=int, default=3333)

#MAKE SURE VALUES ARE ADDED
server_addr = (ip, port)

commands="""
PRINT - prints server details
TRANSFER <FILE> - transfer file over using SCP
LIST - lists log sources
EXIT - closes connection to server
"""

command = ""
args = parser.parse_args()

print("Client session open on port %d" % args[0])
sock = sock.bind((localhost, args[0]))

while command != "EXIT":
    print(commands)
    cmd = input("> ")

# JULY 16TH -------------------------------------------------------------------

    sock.connect(server_addr)
    sock.send(pickle.dumps(cmd))
