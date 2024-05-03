# -----------------------------------------------------------
# a client that connects to a server and send a message,
# then wait to receive a message from the server
# Usage: python3 server.python
# the port and server IP address are hardcoded
# 2023 Dr. Fatma Alali
# -----------------------------------------------------------


import socket
import sys
import ssl

BUF_SIZE = 4096*1000
HOST = "localhost"
PORT = 9999

CERT_FILE = "cert.crt"
KEY_FILE = "key.pem"

def tls_connection(client, msg):
    try:
        ssl_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH, cafile=CERT_FILE)
        ssl_context.load_cert_chain(certfile=CERT_FILE, keyfile=KEY_FILE)

        with ssl_context.wrap_socket(client, server_hostname=HOST) as ssl_client:
            ssl_client.connect((HOST, PORT))
            ssl_client.sendall(msg.encode())
            print("Message was sent")

            data = ssl_client.recv(BUF_SIZE)
            print("Client received", data.decode())

    except Exception as e:
        print("Error:", e)


def regular_connection(client, msg):
    #connect to server
    client.connect((HOST, PORT))
    #send message
    client.sendall(msg.encode())
    print("Message was sent")

    #receive dat from server
    data = client.recv(BUF_SIZE)
    print("Client received", data.decode())
    client.close()

def main():
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # read data from user
        msg = input("Enter your message: ")
        #connect to server
        tls_connection(client, msg)

    except:
        print(sys.exc_info()[0])

if __name__ == "__main__":
    main()
