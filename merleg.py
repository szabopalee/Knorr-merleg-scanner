#import os
#cmd = "echo S | netcat 172.27.51.35 4305"
#os.system(cmd)


import socket

TCP_IP = '172.27.51.35' # this IP of my pc. When I want raspberry pi 2`s as a client, I replace it with its IP '169.254.54.195'
TCP_PORT = 4305
BUFFER_SIZE = 1024
MESSAGE = "S"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
print("Message sent")
response, addr = s.recvfrom(TCP_PORT)
response_id = struct.unpack('!H', response[4:6])
print(response_id)
#data = s.recv(BUFFER_SIZE)
s.close()

print ("received data:", data)