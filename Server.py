import argparse
from sys import argv
import socket

# Q: Works perfect on localhost, but how to make it work with the diff server addresses that the client will give? or
#    will that not happen.. as in, the client will give the address that the server is on.. not sure

# EXAMPLE:
# python Server.py 5444
# python Client.py vi.cs.rutgers.edu 5444

# Parse the Port number to create server socket
parser=argparse.ArgumentParser(description="""Arg Parser for Server.py""")
parser.add_argument('portNum', type=int, help='This is the port to launch the server on',action='store')
args = parser.parse_args(argv[1:])


portNum = args.portNum
# print(str(portNum))

# Create Server socket 
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(('', portNum))
ss.listen(0)
sock, addr = ss.accept()

# Reverse func
def revString(string):
    return string[::-1]  

# Loop till Client response is '' meaning their socket is closed
active = True
clientString = ''
newString = ''

while active:
    clientString = sock.recv(256)
    clientString = clientString.decode('utf-8')

    if clientString != '':
        newString = revString(clientString)
        sock.sendall(newString.encode('utf-8'))
    
    else:
        active = False

# All done, close the server socket(ss) and the new socket(sock)
ss.close()
sock.close()
