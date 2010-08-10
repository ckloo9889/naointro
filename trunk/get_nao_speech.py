import os
import sys
import time
from PIL import Image
import cv
import imghdr
import os
import sys
import aiml
import pickle
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
	def __init__(self, host, port, voice):
		self.host         = host # "192.168.0.80"
		self.port         = port # 9559
		self.speechDevice = None
		self.recoDevice   = None
		self.memoryDevice = None
		self.aliceKernel  = None
		self.oldInput     = ""
		self.threshold    = 0.5
		self.voice        = voice #"Heather22Enhanced"
	
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
		try:
			self.speechDevice.setVoice(self.voice)	
		except Exception, e:
		    print "Error when setting the voice: "+str(e)

		#CONNECT TO A SPEECH RECOGNITION PROXY
		try:
		    self.recoDevice = ALProxy("ALSpeechRecognition", self.host, self.port)
		except Exception, e:
		    print "Error when creating speech recognition device proxy:"+str(e)
		
		#SET UP RECOGNITION DEVICE
		try:
			self.recoDevice.setLanguage("English")
			if(chat == False): 
				wordList = ["stand up","go nao"]
			else:	
				dictFile = open("dictionary.pkl", "rb")
				dictio   = pickle.load(dictFile)
				dictFile.close()
				wordList = dictio.keys()
			print wordList
			self.recoDevice.setWordListAsVocabulary(wordList)
			self.recoDevice.setParameter("EarUseFilter",1.0)	
			self.recoDevice.setParameter("EarSpeed",2.0)
			self.recoDevice.setVisualExpression(False)
			self.recoDevice.setAudioExpression(False)		
		except Exception, e:
		    print "Error when creating speech recognition device proxy:"+str(e)
			
		#INITIALISE ALICE
		if(chat == True):
			cwd = os.getcwd()
			os.chdir(alicePath)
			self.aliceKernel = aiml.Kernel()
			self.aliceKernel.learn("std-startup.xml")
			self.aliceKernel.respond("load aiml b")
			os.chdir(cwd)					

		#START WORDS DETECTION
		try:
			self.recoDevice.subscribe("MyModule")
		except Exception, e:
		    print "Error when starting the speech recognition: "+str(e)
			
	#CHAT WITH NAO__________________________________________________________________________________
	def naoChat(self,chat):
		try:
			inputSpeech = self.memoryDevice.getData("WordRecognized",0)
		except Exception, e:
		    print "Error when reading reacognized word: "+str(e)

		predictedWords = ""
		if(inputSpeech[1] >= self.threshold):
			predictedWord = inputSpeech[0]
		try:
			self.memoryDevice.insertData("WordRecognized",["",0])
		except Exception, e:
		    print "Error when overwriting the reacognized word: "+str(e)

		if(len(predictedWords)>0):
			print predictedWords
			if(predictedWords != self.oldInput):
				self.oldInput = predictedWords
				if(chat == True): #RESPOND TO THE INPUT
					aliceReply = self.aliceKernel.respond(predictedWords)
					aliceReply.lower().replace("alice", "nao")
					self.genSpeech(aliceReply)
		return predictedWords						

	#SAY A SENTENCE___________________________________________________________________________________
	def genSpeech(self,sentence):
		try:
			self.speechDevice.post.say(sentence)
		except Exception, e:
		    print "Error when saying a sentence: "+str(e)

	#STOP CHATTING___________________________________________________________________________________
	def stopSpeechReco(self):
		time.sleep(2)
		try:
			self.recoDevice.unsubscribe("MyModule") 
		except Exception, e:
		    print "Error when stopping the speech recognition: "+str(e)


