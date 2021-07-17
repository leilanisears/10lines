# JULY 16TH

import smtplib, ssl
import socket, sys, argparse

def send_alert(ip_address, port):
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
