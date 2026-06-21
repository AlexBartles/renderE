import socket
import struct
import threading as th
import sys

dgramtimeout = 20
recvsize = 3640*1024
tmpdir = "temp"

def receive(sock):
    #actual stuff goes here eventually
    try:
        sock.recv(recvsize)
        return 1
    except TimeoutError:
        return 0

def portListener(desc, devIP, port):
    print(f"adding receiverE portlistener: {desc}", file=sys.stderr)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((devIP, port))
    sock.settimeout(dgramtimeout)
    while True:
        if not receive(sock):
            break
    print(f"terminating receiverE portlistener: {desc}", file=sys.stderr)

def multicastPortListener(desc, groupIP, port, devIP):
    print(f"adding receiverE mcast portlistener: {desc}", file=sys.stderr)
    #thank the lord for https://gist.github.com/dksmiffs/96ddbfd11ad7349ab4889b2e79dc2b22
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((groupIP, port))
    mreq = struct.pack('4sl', socket.inet_aton(groupIP), socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
    sock.settimeout(dgramtimeout)
    while True:
        if not receive(sock):
            break
    print(f"terminating receiverE mcast portlistener: {desc}", file=sys.stderr)

def addPortListener(desc, devIP, port):
    th.Thread(target=portListener, args=(desc, devIP, port), daemon=True).start()

def addMulticastPortListener(desc, groupIP, port, devIP=''):
    th.Thread(target=multicastPortListener, args=(desc, groupIP, port, devIP)).start()

def setUDPDatagramTimeout(timeout):
    global dgramtimeout
    dgramtimeout = timeout

def setRecvSize(rs):
    global recvsize
    recvsize = rs

def setTimeDriftThreshold(val):
    pass #dont care

def setTmpDir(dirName):
    global tmpDir
    tmpDir = dirName

#more work is being done! not here though, that would be too hard to test