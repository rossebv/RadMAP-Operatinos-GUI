import zmq
import subprocess
import glob
from datetime import datetime, date, time
import shlex
import string
from Tkinter import Tk
import time

context = zmq.Context()

#  Sockets to talk to servers
port = "5555"
dbSocket = context.socket(zmq.PAIR)
dbSocket.bind("tcp://192.168.100.42:%s" % port)

#booleans
velodynePortStarted = False
velodyneStarboardStarted = False
ladybugPortStarted = False
ladybugStarboardStarted = False
arduinoStarted = False
GpsStarted = False


processes = [] #list of all the processes running
iterations = 0 #number of iterations through loop. used to index list of processes for verification

#States
createDirs_state = 0 #0 if directories to be saved into not set up, 1 if set. if 1, ladybugs, lidar and arduino can be started
system_state = 0 #0 if sta command not received
#1 if sta command received and Lidar/Ladybug/Arduino collecting data


while True:
    
	if dbSocket.poll(100) != 0: #potentially add a timeout to the socket poll
		dbCommand = dbSocket.recv()
		
		
		if dbCommand == "startCapture":
			print "Command Received - %s" % dbCommand
			dbSocket.send("startCapture Command Received")
			startCapture = subprocess.Popen("startCapture.bat", cwd=r'E:', creationflags=subprocess.CREATE_NEW_CONSOLE)
			time.sleep(1)
			startArduino = subprocess.Popen("C:\\Users\\misti\\Desktop\\RadMAP-Operatinos-GUI\\Operations GUI\\Server Code\\startArduino.exe")
		if dbCommand == "startGPS":
			print "Command Received - %s" % dbCommand
			dbSocket.send("startGPS Command Received")
			date = datetime.now()
			#filename = date.strftime("Run_%Y%m%d_%H" + "%M%S")
			#logfile_path = filename + '\gps\logfile.gps' #set the path for the logfile to be saved with gps data collection
			logfile_path = date.strftime("\gps_%Y%m%d_%H%M%S_logfile.gps")
			x = Tk()
			x.withdraw()
			x.clipboard_clear()
			x.clipboard_append(logfile_path)
			x.destroy()
			startGps = subprocess.Popen("C:\\Users\\misti\\Desktop\\RadMAP-Operatinos-GUI\\Operations GUI\\AutoHotKey Scripts\\GPS_Start_Script.exe")

		if dbCommand == "stopCapture":
			print "Command Received - %s" % dbCommand
			dbSocket.send("stopCapture Command Received")
			stopCapture = subprocess.Popen("C:\\Users\\misti\\Desktop\\RadMAP-Operatinos-GUI\\Operations Gui\\Server Code\\StopCaptureScript.exe")

		if dbCommand == "stopGPS":
			print "Command Received - %s" % dbCommand
			dbSocket.send("stopGPS Command Received")
			startGps = subprocess.Popen("C:\\Users\\misti\\Desktop\\RadMAP-Operatinos-GUI\\Operations GUI\\AutoHotKey Scripts\\GPS_Stop_Script.exe")



