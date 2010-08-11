import os
import sys
import time
from PIL import Image
import cv
import imghdr
import os
import sys
import random
import math
#PATHS FOR NAO___________________________________________________________
#alPath = "/data/Documents/nao/lib"
alPath = "C:\Program Files\Aldebaran\Choregraphe 1.6.13\lib"
sys.path.append(alPath)
import naoqi
from naoqi import ALBroker
from naoqi import ALModule
from naoqi import ALProxy
from naoqi import ALBehavior		 
from naoqi import motion

#_________________________________________________________________________________________________
#_________________________________________________________________________________________________
class getNaoHeadMoves:
	def __init__(self, host, port):
		self.host		 = host # "192.168.0.80"
		self.port		 = port # 9559
		self.motionDevice = None
		self.memoryDevice = None
		self.speechDevice = None
		self.nrJoints	 = 0

	#INITIALIZE THE MOTION DEVICE__________________________________________________________________
	def initDevice(self):
		#CONNECT TO A PROXY
		try:
			self.motionDevice = ALProxy("ALMotion", self.host, self.port)
		except Exception, e:
			print "Error when creating motion device proxy:"+str(e)
			exit(1)

	#MOVE HEAD YAW_________________________________________________________________________________
	def moveHeadYawAbs(self, pTargetAngles, timeLists):
		names  = "HeadYaw"
		#CONVERT TO RADIANS
		pTargetAngles = [x * (math.pi/180.0) for x in pTargetAngles]
		isAbsolute  = True
		try:
			self.motionDevice.angleInterpolation(names, pTargetAngles, timeLists, isAbsolute)
		except Exception, e:
			print "Error when changing the head yaw: "+str(e)

	#MOVE HEAD PITCH________________________________________________________________________________
	def moveHeadPitchAbs(self, pTargetAngles, timeLists):
		names  = "HeadPitch"
		pTargetAngles = [x * (math.pi/180.0) for x in pTargetAngles]
		#CONVERT TO RADIANS
		pTargetAngles = [x * (math.pi/180.0) for x in pTargetAngles]
		isAbsolute  = True
		try:
			self.motionDevice.angleInterpolation(names, pTargetAngles, timeLists, isAbsolute)
		except Exception, e:
			print "Error when changing the head pitch: "+str(e)

		
