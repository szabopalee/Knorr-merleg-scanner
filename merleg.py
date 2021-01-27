import socket
import sys

# parameterben kell megadni az IP és port cimeket
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

# visual:

from Tkinter import *

class Application(Frame):
    def weigh(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        bytes_sent = s.send(MESSAGE)
        print("Message sent", bytes_sent)
        data = s.recv(BUFFER_SIZE)
        print("Received:", data)
        s.close()
        self.textvar.set(data[3:17])
        self.result.pack()

    def createWidgets(self):
        self.textvar = StringVar()
        self.result = Label(self, textvariable=self.textvar)
        self.result.pack()

        self.weigh_button = Button(self)
        self.weigh_button["text"] = "Meres"
        self.weigh_button["command"] = self.weigh
        self.weigh_button.pack({"side": "left"})

        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()