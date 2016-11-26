from socket import socket, AF_INET, SOCK_STREAM
import time

sock = socket(family=AF_INET, type=SOCK_STREAM)
sock.connect(('localhost', 25000))

while True:
  start = time.time()
  sock.send(b'32')
  response = sock.recv(100)
  end = time.time()
  print(str(end - start))
