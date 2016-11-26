# a simple server using processes for tests

import datetime
from multiprocessing import Process
from socket import socket, SOL_SOCKET, SO_REUSEADDR, AF_INET, SOCK_STREAM
from fib import fib

def fib_server(address):
  sock = socket(family=AF_INET, type=SOCK_STREAM)
  sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
  sock.bind(address)
  sock.listen(5)
  while True:
    client, addr = sock.accept()
    print(datetime.datetime.utcnow(), "Connection", addr)
    Process(target=fib_handler, args=(client, addr,)).start()

def fib_handler(client, addr):
  while True:
    req = client.recv(100)
    if not req:
      break
    n = int(req)
    fibN = fib(n)
    response = "Reponse = " + str(fibN).encode(encoding='ascii') + b'\n'
    client.send(response)
  print(datetime.datetime.utcnow(), addr, "Closed")


fib_server(('', 25000))
