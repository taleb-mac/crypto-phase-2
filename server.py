# -----------------------------------------------------------
# Echo server: a server that accepts a connection, prints
# client message, then echo back (send) client message
# Usage: python3 server.python
# Seerver port is hardcoded to 9999
#
# 2023 Dr. Fatma Alali
# -----------------------------------------------------------

import socket
import ssl

HOST = "localhost"
BUF_SIZE = 4096*1000
PORT = 9999

def regular_connection(s):
    client, addr = s.accept()
    print("Client accepted")
    # read and print the msg from the client
    data = client.recv(BUF_SIZE)
    print("Client sent", data.decode())
    # send back the same message to the client
    client.sendall(data)


def main():
  #create tcp socket
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.bind((HOST, PORT))
  #listen to incomming connections
  s.listen(1)
  regular_connection(s)

if __name__ == "__main__":
  main()

