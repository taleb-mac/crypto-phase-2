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
        regular_connection(client, msg)

    except:
        print(sys.exc_info()[0])

if __name__ == "__main__":
    main()
