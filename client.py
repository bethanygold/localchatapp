import socket
import sys
import time

# end import

# Init
s = socket.socket()
host = input(str("Please enter the hostname server: ")) # request the host name of the server
port = 9090
# connections
s.connect((host,port)) # this connects the socket to the host and port
print("Connected to chat server") # this print out when its connects
# message
while 1:
        incoming_message = s.recv(1024)
        incoming_message = incoming_message.decode()
        print("Server: ", incoming_message)
        message = input(str(">>"))
        message = message.encode()
        s.send(message)
        print("message sent...")
        print("")
