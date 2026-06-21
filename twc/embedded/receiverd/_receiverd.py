import receivere
import sys
import traceback as tb

msgdesc = ""

def abortMsg(fd, msgId):
    print(f"Error in FD {fd}, msgId {msgId}:\n{tb.format_exc()}", file=sys.stderr)

def setTime(sec, millisec):
    print("Somebody is trying to set the time! Dark magic?")

def setMsgDesc(fd, msgId, desc):
    global msgdesc
    msgdesc = desc

def decrementInterest(fd, msgId):
    print("what is interest")