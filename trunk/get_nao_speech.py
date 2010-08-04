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
class getNaoSpeech:
	def __init__(self, host, port):
		self.host         = host # "192.168.0.80"
		self.port         = port # 9559
		self.speechDevice = None
		self.recoDevice   = None
		self.memoryDevice = None
		self.aliceKernel  = None
		self.oldInput     = ""
	
	#INITIALIZE THE MOTION DEVICE__________________________________________________________________
	def initDevice(self,chat):
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
		if(chat == False): 
			wordList = ["nao get up","get up","go"]
		else:	
			wordList = ["hello", "bye", "goodbye", "how are you"]
		self.recoDevice.setWordListAsVocabulary(wordList)	
		self.recoDevice.setParameter("EarUseFilter",1.0)	

		#INITIALISE ALICE
		if(chat == True):
			cwd = os.getcwd()
			os.chdir(alicePath)
			self.aliceKernel = aiml.Kernel()
			self.aliceKernel.learn("std-startup.xml")
			self.aliceKernel.respond("load aiml b")
			os.chdir(cwd)					

		#START WORDS DETECTION
		self.recoDevice.subscribe("MyModule")

	#CHAT WITH NAO__________________________________________________________________________________
	def naoChat(self,chat):
		maxSpeech = "";
		maxProbab = 0;	
		inputSpeech = self.memoryDevice.getData("WordRecognized")
		
		if(len(inputSpeech)>0):
			for i in range(0,len(inputSpeech)):
				if(i%2==1 and maxProbab>inputSpeech[i]):
					maxSpeech = inputSpeech[i-1];
					maxProbab = inputSpeech[i];	
				
			if(maxSpeech != self.oldInput):	 
				#RESPOND TO THE INPUT
				self.oldInput = maxSpeech
				if(chat == True):
					aliceReply = self.aliceKernel.respond(str(maxSpeech))
					aliceReply.lower().replace("alice", "nao")
					self.speechDevice.post.say(aliceReply)
				else:
					return maxSpeech						

	#STOP CHATTING___________________________________________________________________________________
	def stopSpeechReco(self):
		time.sleep(2)
		self.recoDevice.unsubscribe("MyModule") 


