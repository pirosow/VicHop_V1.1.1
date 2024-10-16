from findNightServerAlt import findNightServer
import socket
from fontTools.misc.textTools import tobytes
import time
from functions import sendMessage

hostName = socket.gethostname()
ipAdress = "local ip adress here"

port = 5555

def connectToMain(port):
    tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tcpsocket.connect((ipAdress, port))

    return tcpsocket

tcpsocket = connectToMain(port)

while True:
    try:
        url = findNightServer(claim=False)

        url = tobytes(url)

        tcpsocket.send(url)

    except:
        print("Connection lost to main. Reconnecting...")

        sendMessage("Connection lost to main. Reconnecting... [alt]")

        time.sleep(10)

        tcpsocket = connectToMain(port)
