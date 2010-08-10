import os
import sys
import time
from PIL import Image
import cv
import imghdr
import os
import sys
import random
#PATHS FOR NAO___________________________________________________________
alPath = "/data/Documents/nao/lib"
#alPath = "C:\Program Files\Aldebaran\Choregraphe 1.6.13\lib"
sys.path.append(alPath)
import naoqi
from naoqi import ALBroker
from naoqi import ALModule
from naoqi import ALProxy
from naoqi import ALBehavior         

#_________________________________________________________________________
#_________________________________________________________________________
class getNaoBehaviors:
	def __init__(self, host, port):
		self.host     = host # "192.168.0.80"
		self.port     = port # 9559
		self.frame    = None
		self.motion   = None
		#SET PATH TO BEHAVIORS IN NAO'S HEAD
		self.basePath = "/home/nao/behaviors/" #"/data/Documents/nao/projects/" 

	#INITIALIZE THE VIDEO DEVICE_____________________________________________
	def initDevice(self):
		try:
			self.frame  = ALProxy("ALFrameManager", self.host, self.port)
		except Exception, e:
		    print "Error when creating the frame manager device: "+str(e)
			exit(1)

		try:
			self.motion = ALProxy("ALMotion", self.host, self.port)
		except Exception, e:
		    print "Error when creating the motion device: "+str(e)
			exit(1)
		
	#CALL THE NEEDED BEHAVIOR________________________________________________
	def callBehavior(self,what):
		gesture_path = self.basePath + what
		try:
			gesture_id   = self.frame.newBehaviorFromFile(gesture_path, "")
		except Exception, e:
		    print "Error when reading the behavior from file: "+str(e)

		#THE BODY NEEDS TO BE STIFF BEFORE PLAYING THE BAHVIORS!
 		try:
			self.frame.playBehavior(gesture_id)
			self.frame.completeBehavior(gesture_id) # ... what does it do?
		except Exception, e:
		    print "Error when playing the behavior: "+str(e)
	
		

