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
class getNaoArmMoves:
	def __init__(self, host, port):
		self.host         = host # "192.168.0.80"
		self.port         = port # 9559
		self.motionDevice = None
		self.memoryDevice = None
		self.speechDevice = None
		self.nrJoints     = 0

	#INITIALIZE THE MOTION DEVICE__________________________________________________________________
	def initDevice(self):
		#CONNECT TO A PROXY
		try:
		    self.motionDevice = ALProxy("ALMotion", self.host, self.port)
		except Exception, e:
		    print "Error when creating motion device proxy: "+str(e)
			exit(1)

	#HOLDING BOTTLE POSITON_____________________________________________________________________
	def initPosHoldBottle(self):
		names  = "LShoulderPitch"
		angleLists  = [40]
		timeLists   = [1.0]
		isAbsolute  = True
		angleLists = [x * (math.pi/180.0) for x in angleLists]
		try:
			self.motionDevice.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
		except Exception, e:
    		print "Error when making nao hold the bottle(LShoulderPitch): "+str(e)

		names  = "RShoulderPitch"
		angleLists  = [40]
		timeLists   = [1.0]
		isAbsolute  = True
		angleLists = [x * (math.pi/180.0) for x in angleLists]
		try:
			self.motionDevice.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
		except Exception, e:
    		print "Error when making nao hold the bottle(RShoulderPitch): "+str(e)
                
		names  = "LShoulderRoll"
		angleLists  = [2.4]
		timeLists   = [1.0]
		isAbsolute  = True
		angleLists = [x * (math.pi/180.0) for x in angleLists]
		try:
			self.motionDevice.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
		except Exception, e:
    		print "Error when making nao hold the bottle(LShoulderRoll):"+str(e)

		names  = "RShoulderRoll"
		angleLists  = [-2.4]
		timeLists   = [1.0]
		isAbsolute  = True
		angleLists = [x * (math.pi/180.0) for x in angleLists]
		try:
			self.motionDevice.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
		except Exception, e:
    		print "Error when making nao hold the bottle(RShoulderRoll): "+str(e)

		names  = "LWristYaw"
		angleLists  = [-38.8]
		timeLists   = [1.0]
		isAbsolute  = True
		angleLists = [x * (math.pi/180.0) for x in angleLists]
		try:
			self.motionDevice.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
		except Exception, e:
    		print "Error when making nao hold the bottle(LWristYaw): "+str(e)

		names  = "RWristYaw"
		angleLists  = [38.8]
		timeLists   = [1.0]
		isAbsolute  = True
		angleLists = [x * (math.pi/180.0) for x in angleLists]
		try:
			self.motionDevice.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
		except Exception, e:
    		print "Error when making nao hold the bottle(RWristYaw): "+str(e)

		names  = "LHand"
		angleLists  = [49.9]
		timeLists   = [1.0]
		isAbsolute  = True
		angleLists = [x * (math.pi/180.0) for x in angleLists]
		try:
			self.motionDevice.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
		except Exception, e:
    		print "Error when making nao hold the bottle(LHand): "+str(e)

		names  = "RHand"
		angleLists  = [49.9]
		timeLists   = [1.0]
		isAbsolute  = True
		angleLists = [x * (math.pi/180.0) for x in angleLists]
		try:
			self.motionDevice.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
		except Exception, e:
    		print "Error when making nao hold the bottle(RHand): "+str(e)

	#RELEASE THE BOTTLE MOVEMENT___________________________________________________________________________
	def releaseBottle(self):
		names  = "LShoulderPitch"
		angleLists  = [103]
		timeLists   = [1.0]
		isAbsolute  = True
		angleLists = [x * (math.pi/180.0) for x in angleLists]
		try:
			self.motionDevice.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
		except Exception, e:
    		print "Error when making nao release the bottle(LShoulderPitch): "+str(e)

		names  = "RShoulderPitch"
		angleLists  = [103]
		timeLists   = [1.0]
		isAbsolute  = True
		angleLists = [x * (math.pi/180.0) for x in angleLists]
		try:
			self.motionDevice.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
		except Exception, e:
    		print "Error when making nao release the bottle(RShoulderPitch): "+str(e)
                
		names  = "LShoulderRoll"
		angleLists  = [35]
		timeLists   = [1.0]
		isAbsolute  = True
		angleLists = [x * (math.pi/180.0) for x in angleLists]
		try:
			self.motionDevice.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
		except Exception, e:
    		print "Error when making nao release the bottle(LShoulderRoll): "+str(e)

		names  = "RShoulderRoll"
		angleLists  = [-35]
		timeLists   = [1.0]
		isAbsolute  = True
		angleLists = [x * (math.pi/180.0) for x in angleLists]
		try:
			self.motionDevice.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
		except Exception, e:
    		print "Error when making nao release the bottle(RShoulderRoll): "+str(e)

		names  = "LWristYaw"
		angleLists  = [-38.8]
		timeLists   = [1.0]
		isAbsolute  = True
		angleLists = [x * (math.pi/180.0) for x in angleLists]
		try:
			self.motionDevice.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
		except Exception, e:
    		print "Error when making nao release the bottle(LWristYaw): "+str(e)
		
		names  = "RWristYaw"
		angleLists  = [38.8]
		timeLists   = [1.0]
		isAbsolute  = True
		angleLists = [x * (math.pi/180.0) for x in angleLists]
		try:
			self.motionDevice.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
		except Exception, e:
    		print "Error when making nao release the bottle(RWristYaw): "+str(e)
		
		names  = "LHand"
		angleLists  = [23]
		timeLists   = [1.0]
		isAbsolute  = True
		angleLists = [x * (math.pi/180.0) for x in angleLists]
		try:
			self.motionDevice.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
		except Exception, e:
    		print "Error when making nao release the bottle(LHand): "+str(e)

		names  = "RHand"
		angleLists  = [23]
		timeLists   = [1.0]
		isAbsolute  = True
		angleLists = [x * (math.pi/180.0) for x in angleLists]
		try:
			self.motionDevice.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
		except Exception, e:
    		print "Error when making nao release the bottle(RHand): "+str(e)

	#MOVE ARMS IN FRONT OF THE BODY__________________________________________________________________________________
	def moveArmsInFront(self):
		names  = "LShoulderPitch"
		angleLists  = [52.0]
		timeLists   = [1.0]
		isAbsolute  = True
		angleLists = [x * (math.pi/180.0) for x in angleLists]
		try:
			self.motionDevice.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
		except Exception, e:
    		print "Error when moving arms in front(LShoulderPitch): "+str(e)
		
		names  = "RShoulderPitch"
		angleLists  = [52.0]
		timeLists   = [1.0]
		isAbsolute  = True
		angleLists = [x * (math.pi/180.0) for x in angleLists]
		try:
			self.motionDevice.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
		except Exception, e:
    		print "Error when moving arms in front(RShoulderPitch): "+str(e)
		                
		names  = "LShoulderRoll"
		angleLists  = [2.4]
		timeLists   = [1.0]
		isAbsolute  = True
		angleLists = [x * (math.pi/180.0) for x in angleLists]
		try:
			self.motionDevice.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
		except Exception, e:
    		print "Error when moving arms in front(LShoulderRoll): "+str(e)
		
		names  = "RShoulderRoll"
		angleLists  = [-2.4]
		timeLists   = [1.0]
		isAbsolute  = True
		angleLists = [x * (math.pi/180.0) for x in angleLists]
		try:
			self.motionDevice.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
		except Exception, e:
    		print "Error when moving arms in front(RShoulderRoll): "+str(e)
		
		names  = "LWristYaw"
		angleLists  = [36.6]
		timeLists   = [1.0]
		isAbsolute  = True
		angleLists = [x * (math.pi/180.0) for x in angleLists]
		try:
			self.motionDevice.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
		except Exception, e:
    		print "Error when moving arms in front(LWristYaw): "+str(e)
		
		names  = "RWristYaw"
		angleLists  = [-36.6]
		timeLists   = [1.0]
		isAbsolute  = True
		angleLists = [x * (math.pi/180.0) for x in angleLists]
		try:
			self.motionDevice.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
		except Exception, e:
    		print "Error when moving arms in front(RWristYaw): "+str(e)
		
		names  = "LElbowRoll"
		angleLists  = [-65.0]
		timeLists   = [1.0]
		isAbsolute  = True
		angleLists = [x * (math.pi/180.0) for x in angleLists]
		try:
			self.motionDevice.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
		except Exception, e:
    		print "Error when moving arms in front(LElbowRoll): "+str(e)
		
		names  = "RElbowRoll"
		angleLists  = [65.0]
		timeLists   = [1.0]
		isAbsolute  = True
		angleLists = [x * (math.pi/180.0) for x in angleLists]
		try:
			self.motionDevice.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
		except Exception, e:
    		print "Error when moving arms in front(RElbowRoll): "+str(e)

		names  = "LHand"
		angleLists  = [12.0]
		timeLists   = [1.0]
		isAbsolute  = True
		angleLists = [x * (math.pi/180.0) for x in angleLists]
		try:
			self.motionDevice.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
		except Exception, e:
    		print "Error when moving arms in front(LHand): "+str(e)
		
		names  = "RHand"
		angleLists  = [12.0]
		timeLists   = [1.0]
		isAbsolute  = True
		angleLists = [x * (math.pi/180.0) for x in angleLists]
		try:
			self.motionDevice.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
		except Exception, e:
    		print "Error when moving arms in front(RHand): "+str(e)
						
	#MOVE LEFT ARM BETWEEN 2 POSITIONS__________________________________________________________________
	def moveArm(self, dx, dy, dz, dwx, dwy, dwz, closeOpen):
		#DO NOT FORGET TO INITIALIZE NAO'S POSITION!		
		try:
			if(closeOpen == "close"):
				self.motionDevice.post.closeHand('LHand')
			else:
				self.motionDevice.post.openHand('LHand')
		except Exception, e:
    		print "Error when closing/opening the hand: "+str(e)

		effector   = "LArm"
		space      = motion.SPACE_NAO
		axisMask   = 39 #CONTROL EVERYTHING
		isAbsolute = False

		#SINCE THE SYSTEM IS RELATIVE TO NAO:
		currentPos = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

		#DEFINE CHANGES RELATIVE TO CURRENT POSITION
		#dx  -- translation axis X (meters)
		#dy  -- translation axis Y (meters)
		#dz  -- translation axis Z (meters)
		#dwx -- rotation axis X (radians)
		#dwy -- rotation axis Y (radians)
		#dwz -- rotation axis Z (radians)
		targetPos  = [dx, dy, dz, dwx, dwy, dwz]
		
		#GO TO THE TARGET POSITION ANF BACK AGAIN
		path  = targetPos #[targetPos, currentPos]
		times = 10.0 #TIME IN SECONDS
		try:
			self.motionDevice.post.positionInterpolation(effector, space, path, axisMask, times, isAbsolute)
		except Exception, e:
    		print "Error when moving the left arm between 2positions: "+str(e)

	#CHECK IF THERE IS SOMETHING IN THE HAND AND IF SO CLOSE IT______________________________________________
	def grabObject(self):
		#WAIT TO BE HANDED IN THE OBJECT
		self.moveArm(0.2, -0.2, 0.5, 0.5, 0.9, 0.2, "open")
		
		#CONNECT TO A MEMORY PROXY
		try:
			self.memoryDevice = ALProxy("ALMemory", self.host, self.port)
		except Exception, e:
		    print "Error when creating memory device proxy:"+str(e)
		    exit(1)
	
		try:
			handBefore = self.memoryDevice.getData("FrontTactilTouched")
			handAfter  = self.memoryDevice.getData("FrontTactilTouched")
		except Exception, e:
    		print "Error when reading tactile data from memory: "+str(e)

		#CONNECT TO A SPEECH PROXY
		try:
			self.speechDevice = ALProxy("ALTextToSpeech", self.host, self.port)
		except Exception, e:
		    print "Error when creating speech device proxy:"+str(e)
		    exit(1)
		
		while(handAfter == handBefore):
			time.sleep(2)
			try:
				handAfter = self.memoryDevice.getData("FrontTactilTouched")
			except Exception, e:
    			print "Error when reading tactile data from memory: "+str(e)
			try:
				self.speechDevice.post.say("Hand in that microphone, will you?!")
			except Exception, e:
    			print "Error saying something: "+str(e)
			break
		self.moveArm(-1.3, 0.2, -0.7, 1.8, -0.2, -0.4, "close")
			
 	#MOVE ARM IN AN ELLIPSOIDAL MANNER__________________________________________________
	def moveArmEllipse(self):
		#DO NOT FORGET TO INITIALIZE NAO'S POSITION
		self.initPos()

		effector = "LArm"
		space    = motion.SPACE_NAO
		path     = [
					 [0.0, -0.02, +0.00, 0.0, 0.0, 0.0], #POINT 1
					 [0.0, +0.00, +0.01, 0.0, 0.0, 0.0], #POINT 2
					 [0.0, +0.08, +0.00, 0.0, 0.0, 0.0], #POINT 3
					 [0.0, +0.00, -0.04, 0.0, 0.0, 0.0], #POINT 4
					 [0.0, -0.02, +0.00, 0.0, 0.0, 0.0], #POINT 5
					 [0.0, +0.00, +0.00, 0.0, 0.0, 0.0]] #POINT 6
		axisMask   = 7 #JUST CONTROL POSITION
		times      = [0.5, 1.0, 2.0, 3.0, 4.0, 4.5] #SECONDS
		isAbsolute = False
		try:
			self.motionDevice.positionInterpolation(effector, space, path, axisMask, times, isAbsolute)
		except Exception, e:
    		print "Error when moving arm in an ellipsoidal way: "+str(e)







