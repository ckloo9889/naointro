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

		self.stiffness    = 1.0
		self.nrJoints     = 0

	#INITIALIZE THE MOTION DEVICE__________________________________________________________________
	def initDevice(self):
		#CONNECT TO A PROXY
		try:
		    self.motionDevice = ALProxy("ALMotion", self.host, self.port)
		except Exception, e:
		    print "Error when creating motion device proxy:"+str(e)
		    exit(1)

		#MAKE NAO STIFF (OTHERWISE IT WON'T MOVE)
		self.motionDevice.stiffnessInterpolation("Body",self.stiffness,1.0)

	#PUT NAO IN AN INITIAL POSITON (REQUIRED FOR ANY MOVEMENT)______________________________________
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

	def initPosHoldBottle(self):

		names  = "LShoulderPitch"
		angleLists  = [40]
		timeLists   = [1.0]
		isAbsolute  = True
		angleLists = [x * (math.pi/180.0) for x in angleLists]
		self.motionDevice.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)

		names  = "RShoulderPitch"
		angleLists  = [40]
		timeLists   = [1.0]
		isAbsolute  = True
		angleLists = [x * (math.pi/180.0) for x in angleLists]
		self.motionDevice.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
				
		names  = "LShoulderRoll"
		angleLists  = [6.3]
		timeLists   = [1.0]
		isAbsolute  = True
		angleLists = [x * (math.pi/180.0) for x in angleLists]
		self.motionDevice.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
		
		names  = "RShoulderRoll"
		angleLists  = [-6.3]
		timeLists   = [1.0]
		isAbsolute  = True
		angleLists = [x * (math.pi/180.0) for x in angleLists]
		self.motionDevice.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)

		names  = "LWristYaw"
		angleLists  = [-38.8]
		timeLists   = [1.0]
		isAbsolute  = True
		angleLists = [x * (math.pi/180.0) for x in angleLists]
		self.motionDevice.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)

		names  = "RWristYaw"
		angleLists  = [38.8]
		timeLists   = [1.0]
		isAbsolute  = True
		angleLists = [x * (math.pi/180.0) for x in angleLists]
		self.motionDevice.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
		
		names  = "LHand"
		angleLists  = [49.9]
		timeLists   = [1.0]
		isAbsolute  = True
		angleLists = [x * (math.pi/180.0) for x in angleLists]
		self.motionDevice.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)

		names  = "RHand"
		angleLists  = [49.9]
		timeLists   = [1.0]
		isAbsolute  = True
		angleLists = [x * (math.pi/180.0) for x in angleLists]
		self.motionDevice.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
				
	#MOVE ARM BETWEEN 2 POSITIONS__________________________________________________________________
	def moveArm(self, dx, dy, dz, dwx, dwy, dwz, closeOpen):
		print self.motionDevice.getJointNames("LArm")
		#DO NOT FORGET TO INITIALIZE NAO'S POSITION!		
		if(closeOpen == "close"):
			self.motionDevice.post.closeHand('LHand')
		else:
			self.motionDevice.post.openHand('LHand')

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

		self.motionDevice.post.positionInterpolation(effector, space, path, axisMask, times, isAbsolute)
		
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
		handBefore = self.memoryDevice.getData("FrontTactilTouched")
		handAfter  = self.memoryDevice.getData("FrontTactilTouched")

		#CONNECT TO A SPEECH PROXY
		try:
			self.speechDevice = ALProxy("ALTextToSpeech", self.host, self.port)
		except Exception, e:
		    print "Error when creating speech device proxy:"+str(e)
		    exit(1)
		
		while (handAfter == handBefore):
			time.sleep(2)
			handAfter = self.memoryDevice.getData("FrontTactilTouched")
			self.speechDevice.post.say("Hand in that microphone, will you?!")
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
		self.motionDevice.positionInterpolation(effector, space, path, axisMask, times, isAbsolute)

	#REMOVE THE STIFFNESS________________________________________________________________
	def stiffnessOff(self):
		#NAO MIGHT FALL!
		self.motionDevice.stiffnessInterpolation("Body",0.0,1.0)






