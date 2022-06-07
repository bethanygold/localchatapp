import socket
import sys
import time

# end of import

# init
s = socket.socket()
host = socket.gethostname() # this variable gets the local host name of your device
print("server will start on:",host)
port = 9090 # this variable is for the port
# Connections
s.bind((host,port)) # this binds the socket with the host and port
print("")
print("Server has been successfully binded with the host and port")
print("")
print("Server is waiting for incoming connections")
print("")
s.listen(1) # to listen to incoming connections and i set it to be one
conn,addr = s.accept() # the 'conn' is assigned to the socket coming from the client while the 'addr' is assigned to the ip address of the client connecting
print(addr, " has been connected to the server and is now online") # this will print out the ip address of the client that will be connecting
print("")
# message
while 1: # loop
        message = input(str(">>")) # to input your message
        message = message.encode() 
        conn.send(message)
        print("message sent...")
        print("")
        incoming_message = conn.recv(1024)
        incoming_message = incoming_message.decode()
        print("Client: ", incoming_message)
        
