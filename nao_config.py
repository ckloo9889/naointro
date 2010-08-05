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

class NaoConfig:
	def __init__(self, host, port):
		self.ip = host
		self.port = port

		self.host         = host # "192.168.0.80"
		self.port         = port # 9559
		self.motionDevice = None
		self.memoryDevice = None
		self.speechDevice = None

		self.stiffness    = 1.0
		self.nrJoints     = 0
		

	def initDevice(self):
		#CONNECT TO A PROXY
		try:
		    self.motionDevice = ALProxy("ALMotion", self.host, self.port)
		except Exception, e:
		    print "Error when creating motion device proxy:"+str(e)
		    exit(1)

		#MAKE NAO STIFF (OTHERWISE IT WON'T MOVE)
		self.motionDevice.stiffnessInterpolation("Body",self.stiffness,1.0)

	def initPos(self):
		self.nrJoints = len(self.motionDevice.getJointNames("Body"))
		#DEFINE THE INITIAL POSITION
		head     = [0, 0]
		leftArm  = [90, 30, -45, -45]
		leftLeg  = [0, 0, -10, 20, -10, 0]
		rightLeg = [0, 0, -10, 20, -10, 0]
		rightArm = [90, -30, 45, 45]

		#ADD ANGLES FOR WRIST AND HAND
		if(self.nrJoints == 26):
			leftArm  += [-90, 10]
 			rightArm += [90, 10]
		pTargetAngles = head + leftArm + leftLeg + rightLeg + rightArm  

		#CONVERT TO RADIANS
		pTargetAngles = [x * (math.pi/180.0) for x in pTargetAngles]
		
		#INITIALIZE POSITION
		pName     = "Body"
		pMaxSpeed = 0.2
		self.motionDevice.angleInterpolationWithSpeed(pName, pTargetAngles, pMaxSpeed)	
		time.sleep(1)

	#REMOVE THE STIFFNESS
	def stiffnessOff(self):
		#NAO MIGHT FALL!
		self.motionDevice.stiffnessInterpolation("Body",0.0,1.0)
				