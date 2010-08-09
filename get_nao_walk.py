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

#_________________________________________________________________________
#_________________________________________________________________________
class getNaoLegMoves:
	def __init__(self, host, port):
		self.host         = host # "192.168.0.80"
		self.port         = port # 9559
		self.motionDevice = None
		self.gvm          = None
		self.stiffness    = 1.0

	#INITIALIZE THE VIDEO DEVICE_____________________________________________
	def initDevice(self):
		#CONNECT TO A PROXY
		try:
		    self.motionDevice = ALProxy("ALMotion", self.host, self.port)
		except Exception, e:
		    print "Error when creating motion device proxy:"+str(e)
		    exit(1)

		#MAKE NAO STIFF (OTHERWISE IT WON'T MOVE)
		self.motionDevice.stiffnessInterpolation("Body",self.stiffness,1.0)

	#WALK IN A DIRECTION_______________________________________________________
	def walkDirection(self, targetX, targetY, targetTheta):
		#ENABLE ARMS MOVEMENT DURING WALKING
		self.motionDevice.setWalkArmsEnable(True,True)
		
		#ENABLE FOOT CONTACT PROTETCTION
		self.motionDevice.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION",True]])	

		frequency = 1.0 #MAXIMUM SPEED
		self.motionDevice.post.setWalkTargetVelocity(targetX, targetY, targetTheta, frequency)
		
		#WALK FOR 5 SECONDS (OTHERWISE IT WON'T STOP)
		time.sleep(5.0)
		self.motionDevice.setWalkTargetVelocity(0.0, 0.0, 0.0, 0.0)

	#WALK TO A TARGET___________________________________________________________
	def walkTo(self, targetX, targetY, targetTheta):
		#ENABLE ARMS MOVEMENT DURING WALKING
		self.motionDevice.setWalkArmsEnable(True,True)
		
		#ENABLE FOOT CONTACT PROTETCTION
		self.motionDevice.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION",True]])	

		self.motionDevice.post.walkTo(targetX, targetY, targetTheta)
		self.motionDevice.waitUntilWalkIsFinished()

	def kneelDown(self):	
		names  = "LHipPitch"
		angleLists  = [-55]
		timeLists   = [1.0]
		isAbsolute  = True
		angleLists = [x * (math.pi/180.0) for x in angleLists]
		self.motionDevice.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)

		names  = "LKneePitch"
		angleLists  = [112]
		timeLists   = [1.0]
		isAbsolute  = True
		angleLists = [x * (math.pi/180.0) for x in angleLists]
		self.motionDevice.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
		
		names  = "LAnklePitch"
		angleLists  = [-58.5]
		timeLists   = [1.0]
		isAbsolute  = True
		angleLists = [x * (math.pi/180.0) for x in angleLists]
		self.motionDevice.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)

		names  = "RHipPitch"
		angleLists  = [-55]
		timeLists   = [1.0]
		isAbsolute  = True
		angleLists = [x * (math.pi/180.0) for x in angleLists]
		self.motionDevice.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)

		names  = "RKneePitch"
		angleLists  = [112]
		timeLists   = [1.0]
		isAbsolute  = True
		angleLists = [x * (math.pi/180.0) for x in angleLists]
		self.motionDevice.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
		
		names  = "RAnklePitch"
		angleLists  = [-58.5]
		timeLists   = [1.0]
		isAbsolute  = True
		angleLists = [x * (math.pi/180.0) for x in angleLists]
		self.motionDevice.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
		
	def bendForward(self):
		names  = "LHipPitch"
		angleLists  = [-95.0]
		timeLists   = [1.0]
		isAbsolute  = True
		angleLists = [x * (math.pi/180.0) for x in angleLists]
		self.motionDevice.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
 	
		names  = "RHipPitch"
		angleLists  = [-95.0]
		timeLists   = [1.0]
		isAbsolute  = True
		angleLists = [x * (math.pi/180.0) for x in angleLists]
		self.motionDevice.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)

	def sitStraight(self):			
		names  = "LHipPitch"
		angleLists  = [-55.0]
		timeLists   = [1.0]
		isAbsolute  = True
		angleLists = [x * (math.pi/180.0) for x in angleLists]
		self.motionDevice.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
 	
		names  = "RHipPitch"
		angleLists  = [-55.0]
		timeLists   = [1.0]
		isAbsolute  = True
		angleLists = [x * (math.pi/180.0) for x in angleLists]
		self.motionDevice.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
					
	#REMOVE THE STIFFNESS________________________________________________________________
	def stiffnessOff(self):
		#NAO MIGHT FALL!
		if(not self.motionDevice.walkIsActive()):
			self.motionDevice.stiffnessInterpolation("Body",0.0,1.0)
		else:
			self.motionDevice.waitUntilWalkIsFinished()
			self.motionDevice.stiffnessInterpolation("Body",0.0,1.0)









