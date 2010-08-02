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
		self.basePath = "/home/nao/behaviors/" #PATH TO BEHAVIORS IN NAO'S HEAD

	#INITIALIZE THE VIDEO DEVICE_____________________________________________
	def initDevice(self):
		self.frame  = ALProxy("ALFrameManager", host, port)
		self.motion = ALProxy("ALMotion", host, port)

	#CALL THE NEEDED BEHAVIOR________________________________________________
	def callBehavior(self,what):
		gesture_path = self.basePath + what
		gesture_id   = self.frame.newBehaviorFromFile(gesture_path, "")

		self.motion.stiffnessInterpolation("Body", 1.0, 1.0) 
		self.frame.playBehavior(gesture_id)
		self.frame.completeBehavior(gesture_id) # ... what does it do?
		

