import argparse
from sys import argv
import socket

# EXAMPLE:
# python Server.py 5444
# python Client.py vi.cs.rutgers.edu 5444

# Parse the Port number to create server socket
parser=argparse.ArgumentParser(description="""Arg Parser for Server.py""")
parser.add_argument('portNum', type=int, help='This is the port to launch the server on',action='store')
args = parser.parse_args(argv[1:])

portNum = args.portNum

# Create The Server socket 
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind((socket.gethostname(), portNum))
ss.listen(0)
sock, addr = ss.accept()

# Reverse func
def revString(string):
    return string[::-1]  

# Communication Loop
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

# Exit Gracefully
ss.close()
sock.close()
