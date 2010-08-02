import os
import sys
import time
from PIL import Image
import cv
import imghdr
import os
import sys
import aiml
alicePath = "/usr/lib/python2.6/dist-packages/aiml/standard-aiml/"
#PATHS FOR NAO___________________________________________________________
alPath = "/data/Documents/nao/lib"
#alPath = "C:\Program Files\Aldebaran\Choregraphe 1.6.13\lib"
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
		self.speechDevice = None
		self.recoDevice   = None
		self.memoryDevice = None
		self.aliceKernel  = None
	
	#INITIALIZE THE MOTION DEVICE__________________________________________________________________
	def initDevice(self):
		#CONNECT TO A MEMORY PROXY
		try:
			self.memoryDevice = ALProxy("ALMemory", self.host, self.port)
		except Exception, e:
		    print "Error when creating memory device proxy:"+str(e)
		    exit(1)

		#CONNECT TO A SPEECH PROXY
		try:
		    self.speechDevice = ALProxy("ALTextToSpeech", self.host, self.port)
		except Exception, e:
		    print "Error when creating speech device proxy:"+str(e)
		    exit(1)

		#CONNECT TO A SPEECH RECOGNITION PROXY
		try:
		    self.recoDevice = ALProxy("ALSpeechRecognition", self.host, self.port)
		except Exception, e:
		    print "Error when creating speech recognition device proxy:"+str(e)
		    exit(1)

		#SET UP RECOGNITION DEVICE
		self.recoDevice.setLanguage("English") 
		wordList = ["yes","no","hello Nao","goodbye Nao","stupid robot"]
        self.recoDevice.setWordListAsVocabulary(wordList)
 
		#INITIALISE ALICE
		cwd = os.getcwd()
		os.chdir(alicePath)
		self.aliceKernel = aiml.Kernel()
		self.aliceKernel.learn("std-startup.xml")
		self.aliceKernel.respond("load aiml b")
		
		#START WORDS DETECTION
		self.recoDevice.subscribe("MyModule")
	
	#CHAT WITH NAO__________________________________________________________________________________
	def naoChat(self):
		inputSpeech = self.memoryDevice.post.getDataOnChange("WordRecognized",0)
		 
		#RESPOND TO THE INPUT
		aliceReply = self.aliceKernel.respond(inputSpeech)
		self.speechDevice.post.say(aliceReply)

	#STOP CHATTING___________________________________________________________________________________
	def stopSpeechReco(self):
		time.sleep(2)
		self.recoDevice.unsubscribe("MyModule") 


