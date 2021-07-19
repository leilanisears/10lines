# JULY 16TH

import smtplib, ssl
import socket, sys, argparse

message_log = open("/home/server/honey.log", '+a')

def send_alert(ip_address):
    sender_email = "leilani.sears@gmail.com"
    receiver_email = "leilani.sears@gmail.com"

    port = 465
    password = input("Input password > ")

    context = ssl.create_default_context()
    message = """\
        Subject: Connection Alert
        Honeypot has been connected to by %s on port %s""" % (ip_address, port)

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

# JULY 17TH
# ------------------------------------------------------------------

def stand_server(self, port):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(('localhost', port))
    sock.listen()

    while True:
        connection, addr = sock.accept()
        print("Connection by %s" % addr)
        send_alert(addr)

        msg = ""

        while msg != "EXIT"
            connection.send("Send message. To exit, send EXIT")
            msg = connection.recv(4096)
            msg_log.write(msg)

        connection.send("Exiting server. Thank you.")
        sock.close()
        break

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Honeypot Server & Message Logging')
    parser.add_argument('--port', '-p', help='port to run server from', action='store', required=True)
    args = parser.parse_args()

    stand_server(args.port)
