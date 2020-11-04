import socket
import sys

#TCP_IP = '172.27.51.35'
#TCP_PORT = 4305

TCP_IP = sys.argv[1]
TCP_PORT = int(sys.argv[2])

BUFFER_SIZE = 1024
MESSAGE = "S" + "\r\n"

'''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
bytes_sent = s.send(bytes(MESSAGE, 'ASCII'))

#s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.IPPROTO_RAW)   # csak raspberry-n
#s.bind(("172.27.51.35", 0))
#bytes_sent = s.sendto(MESSAGE, (TCP_IP, TCP_PORT))

print("Message sent", bytes_sent)
bytes_recv = s.recv(BUFFER_SIZE)
data = bytes_recv.decode("ASCII")

print("Received:", data)
s.close()
'''
from Tkinter import *

class Application(Frame):
    def weigh(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        bytes_sent = s.send(bytes(MESSAGE, 'ASCII'))
        print("Message sent", bytes_sent)
        bytes_recv = s.recv(BUFFER_SIZE)
        data = bytes_recv.decode("ASCII")
        print("Received:", data)
        s.close()

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.weigh_button = Button(self)
        self.weigh_button["text"] = "Meres",
        self.weigh_button["command"] = self.weigh

        self.weigh_button.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()


# pi python2
'''
import time
import serial

ser = serial.Serial(
        port='/dev/ttyS0',
        baudrate = 115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

while 1:
        x = ser.readline()
        print(x)
'''


'''
# pc python3
import time
from serial import Serial
import serial

ser = Serial(
        port='COM16',
        baudrate = 115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

while 1:
        x = ser.readline()
        print(x)
'''


