#!/usr/bin/python
import os
import time
import datetime

phoneIP = "192.168.0.2"
timeList=["0800", "2230", "0600", "2230", "0600", "2230", "0845", "2330", "0845", "2358", "0900", "2358", "0900", "2300"] #Two entries for each day, first is "start" second is "end"
var = 1
failCount = 0
global mirrorOn
mirrorOn = False


def toggle(): #Calling toggles the GPIO, and thus the mirror on/off
    print "entered toggle function"
    global mirrorOn
    os.system("gpio write 0 1")
    time.sleep(0.8)
    os.system("gpio write 0 0")
    mirrorOn = not mirrorOn
    print "Mirror status", mirrorOn
    return

def pingMirror(): #Calling pings the mirror and return if successful or not.
    print "entered pingMirror function"
    global failCount
    response = os.system("ping -c1 -w1 " + phoneIP + " > /dev/null") #Pings mirror -c1 (once), -w1 (wait for 1 second) and send any responses to /dev/null
    if response == 0: #Response == 0 when ping successful.
        if failCount >=6:
            print "Waking mirror from previous WiFi disabled state"
            toggle()
            failCount = 0
	if mirrorOn == False:
	    toggle()
        return()
    else:
	print "failCount +1"
        failCount += 1
    if failCount == 6:
	print "failCount = 6, toggling mirror state"
        toggle()
    return()

os.system("gpio mode 0 out") #Runs first to declare GPIO pin 0 as output mode
print "running"

while var == 1:
    time.sleep(5)
    day = datetime.datetime.today().weekday() #gets weekday where Monday = 0 and Sunday = 6
    currentTime = time.strftime("%H%M") #gets time as HHMM
    if day == 0:  # monday
	print "monday"
        if currentTime==timeList[0] and mirrorOn==False:
            toggle()
        if currentTime>=timeList[0] and currentTime<=timeList[1]:
            pingMirror()
        elif currentTime==timeList[1]+1 and mirrorOn==True: #If the time exceeds the "late" time and the mirror has not been toggled off due to ping...
            toggle()
    elif day == 1:  # tuesday
	print "tuesday"
        if currentTime==timeList[2] and mirrorOn==False:
            toggle()
        if currentTime>=timeList[2] and currentTime<=timeList[3]:
            pingMirror()
        elif currentTime==timeList[3]+1 and mirrorOn==True:
            toggle()
    elif day == 2:  # wednesday
	print "wednesday"
        if currentTime==timeList[4] and mirrorOn==False:
            toggle()
        if currentTime>=timeList[4] and currentTime<=timeList[5]:
            pingMirror()
        elif currentTime==timeList[5]+1 and mirrorOn==True:
            toggle()
    elif day == 3:  # thursday
	print "thursday"
        if currentTime==timeList[6] and mirrorOn==False:
            toggle()
        if currentTime>=timeList[6] and currentTime<=timeList[7]:
            pingMirror()
        elif currentTime==timeList[7]+1 and mirrorOn==True:
            toggle()
    elif day == 4:  # friday
	print "friday"
        if currentTime==timeList[8] and mirrorOn==False:
            toggle()
        if currentTime>=timeList[8] and currentTime<=timeList[9]:
            pingMirror()
        elif currentTime==timeList[9]+1 and mirrorOn==True:
            toggle()
    elif day == 5:  # saturday
	print "saturday"
        if currentTime==timeList[10] and mirrorOn==False:
            toggle()
        if currentTime>=timeList[10] and currentTime<=timeList[11]:
            pingMirror()
        elif currentTime==timeList[11]+1 and mirrorOn==True:
            toggle()
    elif day == 6:  # sunday
	print "sunday"
        if currentTime==timeList[12] and mirrorOn==False:
            toggle()
        if currentTime>=timeList[12] and currentTime<=timeList[13]:
            pingMirror()
        elif currentTime==timeList[11]+1 and mirrorOn==True:
            toggle()
    else:
        print "Error with day detection."
