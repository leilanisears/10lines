#a continuous script being run on RPI
#run setup.sh to have running as daemon

# ---- JULY 11TH ---------------------------------------------

import socket
import sys
import pickle
import subprocess

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = ('localhost', '4444')
print("SERVER STARTING ON %s PORT %s'" % server_addr)

sock.bind(server_addr)
sock.listen(1)

while True:
    print('WAITING FOR CONNECTION....')
    connection, client_addr = sock.accept()

# --- JULY 12TH ----------------------------------------------

    sock.send(pickle.dumps("Hi! Please send command! Send HELP for more info"))
    cmd = connection.recv(4096)
    cmd_data = pickle.loads(cmd)

    if cmd == "HELP":
        #more commands to be added as functionality is implemented
        help_cmd = """
        PRINT - prints connection info of serevr for reference
        LIST - lists log sources
        TRANSFER <log file> - transfers log files over using scp
            NOTE: will be prompted for appropriate credentials as this is not a headless operation
        EXIT - exits server
        """

        sock.send(pickle.dumps(help_cmd))

    #litrallu LMAO probsa bad practice
    #helpful for debugging
    if cmd == "PRINT":
        msg = pickle.dumps(server_addr)
        sock.send(msg)

        print("PRINTING SERVER INFO...")

# --- JULY 13TH ---------------------------------------------

    if cmd == "LIST":
        conf_file = open("/home/server/logging.conf")
        list_srcs = ""

        for line in conf_file:
            list_srcs = list_srcs + " " + line

        msg = pickle.dumps(list_srcs)
        sock.send(msg)

        print("LISTING SOURCES...")

# --- JULY 14TH ---------------------------------------------

    cmd_spl = cmd.split()
    if cmd_spl[0] == 'TRANSFER':
        sock.send(pickle.dumps("Username: "))

        username_raw = connection.recv(4096)
        username = pickle.loads(username_raw)
        sys_call = username + "@" + client_addr = '.'

        subprocess.run(['scp', cmd_spl[1], sys_call])

    else:
        sock.close()
        print("QUERY COMPLETED OR UNKNOWN ......")
