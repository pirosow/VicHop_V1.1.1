from findNightServerAlt import findNightServer
import socket
from fontTools.misc.textTools import tobytes
import time

hostName = socket.gethostname()
ipAdress = "192.168.0.172" #my local ip xd

tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 5555

tcpsocket.connect((ipAdress, port))

while True:
    try:
        url = findNightServer(claim=False)

        url = tobytes(url)

        tcpsocket.send(url)

    except:
        time.sleep(300)

        tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        port = 5555

        tcpsocket.connect((ipAdress, port))