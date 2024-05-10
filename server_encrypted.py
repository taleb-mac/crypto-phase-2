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

CERT_FILE = "cert.crt"
KEY_FILE = "key.pem"

def tls_connection(s):
  client, addr = s.accept()
  print("Client accepted")

  ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
  ssl_context.load_cert_chain(certfile=CERT_FILE, keyfile=KEY_FILE)

  with ssl_context.wrap_socket(client, server_side=True) as ssl_client:
    data = ssl_client.recv(BUF_SIZE)
    print("Client sent", data.decode())

    ssl_client.sendall(data)

def main():
  #create tcp socket
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.bind((HOST, PORT))
  #listen to incomming connections
  s.listen(1)
  tls_connection(s)

if __name__ == "__main__":
  main()

