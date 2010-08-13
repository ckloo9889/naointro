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
		self.host		 = host # "192.168.0.80"
		self.port		 = port # 9559
		self.motionDevice = None
		self.gvm		  = None

	#INITIALIZE THE VIDEO DEVICE_____________________________________________
	def initDevice(self):
		#CONNECT TO A PROXY
		try:
			self.motionDevice = ALProxy("ALMotion", self.host, self.port)
		except Exception, e:
			print "Error when creating motion device proxy:"+str(e)
			exit(1)

	#WALK IN A DIRECTION_______________________________________________________
	def walkDirection(self, targetX, targetY, targetTheta):
		#ENABLE ARMS MOVEMENT DURING WALKING
		try:
			self.motionDevice.setWalkArmsEnable(True,True)
		except Exception, e:
			print "Error when enabling the hands during the walk: "+str(e)

		#ENABLE FOOT CONTACT PROTETCTION
		try:
			self.motionDevice.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION",True]])	
		except Exception, e:
			print "Error when enabling the foot protection: "+str(e)

		frequency = 1.0 #MAXIMUM SPEED
		try:
			self.motionDevice.post.setWalkTargetVelocity(targetX, targetY, targetTheta, frequency)
		except Exception, e:
			print "Error when generating the walking on a direction: "+str(e)
	
		#WALK FOR 5 SECONDS (OTHERWISE IT WON'T STOP)
		time.sleep(5.0)
		try:
			self.motionDevice.setWalkTargetVelocity(0.0, 0.0, 0.0, 0.0)
		except Exception, e:
			print "Error when stopping the walking on a direction: "+str(e)

	#WALK TO A TARGET___________________________________________________________
	def walkTo(self, targetX, targetY, targetTheta):
		#ENABLE ARMS MOVEMENT DURING WALKING
		try:
			self.motionDevice.setWalkArmsEnable(True,True)
		except Exception, e:
			print "Error when enabling the hands during the walk: "+str(e)
		
		'''	
		#ENABLE FOOT CONTACT PROTETCTION
		try:
			self.motionDevice.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION",True]])	
		except Exception, e:
			print "Error when enabling the foot protection: "+str(e)
		'''
		
		try:
			self.motionDevice.post.walkTo(targetX, targetY, targetTheta)
		except Exception, e:
			print "Error when walking to a target: "+str(e)

		try:
			self.motionDevice.waitUntilWalkIsFinished()
		except Exception, e:
			print "Error when waiting for the walk to finish: "+str(e)

	#KNEEL DOWN MOTION_____________________________________________________________________________
	def kneelDown(self):	
		names	  = "LHipPitch"
		angleLists = [-55]
		timeLists  = [1.0]
		isAbsolute = True
		angleLists = [x * (math.pi/180.0) for x in angleLists]
		try:	
			self.motionDevice.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
		except Exception, e:
			print "Error in kneelDown (LHipPitch): "+str(e)

		names	  = "LKneePitch"
		angleLists = [112]
		timeLists  = [1.0]
		isAbsolute = True
		angleLists = [x * (math.pi/180.0) for x in angleLists]
		try:
			self.motionDevice.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
		except Exception, e:
			print "Error in kneelDown (LKneePitch): "+str(e)

		names	  = "LAnklePitch"
		angleLists = [-58.5]
		timeLists  = [1.0]
		isAbsolute = True
		angleLists = [x * (math.pi/180.0) for x in angleLists]
		try:
			self.motionDevice.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
		except Exception, e:
			print "Error in kneelDown (LAnklePitch): "+str(e)

		names	  = "RHipPitch"
		angleLists = [-55]
		timeLists  = [1.0]
		isAbsolute = True
		angleLists = [x * (math.pi/180.0) for x in angleLists]
		try:
			self.motionDevice.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
		except Exception, e:
			print "Error in kneelDown (RHipPitch): "+str(e)
		
		names	  = "RKneePitch"
		angleLists = [112]
		timeLists  = [1.0]
		isAbsolute = True
		angleLists = [x * (math.pi/180.0) for x in angleLists]
		try:
			self.motionDevice.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
		except Exception, e:
			print "Error in kneelDown (RKneePitch): "+str(e)		

		names	  = "RAnklePitch"
		angleLists = [-58.5]
		timeLists  = [1.0]
		isAbsolute = True
		angleLists = [x * (math.pi/180.0) for x in angleLists]
		try:
			self.motionDevice.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
		except Exception, e:
			print "Error in kneelDown (RAnklePitch): "+str(e)
	
	#BEND FORWARD MOTION______________________________________________________________________________	
	def bendForward(self):
		names	  = "LHipPitch"
		angleLists = [-95.0]
		timeLists  = [1.0]
		isAbsolute = True
		angleLists = [x * (math.pi/180.0) for x in angleLists]
		try:
			self.motionDevice.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
		except Exception, e:
			print "Error in bendForward (LHipPitch): "+str(e)
 	
		names  = "RHipPitch"
		angleLists  = [-95.0]
		timeLists   = [1.0]
		isAbsolute  = True
		angleLists = [x * (math.pi/180.0) for x in angleLists]
		try:
			self.motionDevice.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
		except Exception, e:
			print "Error in bendForward (RHipPitch): "+str(e)

	#SIT STRAIGHT______________________________________________________________________________________ 
	def sitStraight(self):			
		names	  = "LHipPitch"
		angleLists = [-55.0]
		timeLists  = [1.0]
		isAbsolute = True
		angleLists = [x * (math.pi/180.0) for x in angleLists]
		try:
			self.motionDevice.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
		except Exception, e:
			print "Error in sitStraight (LHipPitch): "+str(e)
 	
		names	  = "RHipPitch"
		angleLists = [-55.0]
		timeLists  = [1.0]
		isAbsolute = True
		angleLists = [x * (math.pi/180.0) for x in angleLists]
		try:
			self.motionDevice.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
		except Exception, e:
			print "Error in sitStraight (RHipPitch): "+str(e)
					







