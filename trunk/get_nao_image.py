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
class getNaoImage:
	def __init__(self, host, port):
		self.host        = host #"192.168.0.80"
		self.port        = port #9559
		self.videoDevice = None
		self.gvm         = None

	#INITIALIZE THE VIDEO DEVICE_____________________________________________
	def initDevice():
		#CONNECT TO A PROXY
		try:
		    self.videoDevice = ALProxy("ALVideoDevice", self.host, self.port)
		except Exception, e:
		    print "Error when creating video device proxy:"+str(e)
		    exit(1)

		#SUBSCRIBE GVM TO VIM
		self.gvm = self.videoDevice.subscribe("GVM", 0, 13, 1) # ... parameters?

	#RETRIEVE IMAGES__________________________________________________________
	def getImage():
		#GET THE IMAGE BYTES
	    result = self.videoDevice.getImageRemote(self.gvm)
		
		#PROCESS RESULT TO GET THE IMAGE
    	imString = result[6]
    	columns  = result[0]
    	rows     = result[1]

    	#TRANSFORM THE STRING IN IMAGE
    	im     = Image.fromstring("RGB", (columns, rows), imString)
    	cv_img = cv.CreateImageHeader(im.size, cv.IPL_DEPTH_8U, 3)
    	cv.SetData(cv_img, im.tostring(), im.size[0]*3)
    	return cv_img

 	#CLOSE VIDEO DEVICE_________________________________________________________
	def closeDevice():
    	#UNSUBSCRIBE THE IMAGE DEVICE - UNSUBSCRIBE SVM TO VIM
		self.videoDevice.unsubscribe(self.gvm)







