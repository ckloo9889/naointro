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
class getNaoSpeech:
	def __init__(self, host, port, voice):
		self.host         = host # "192.168.0.80"
		self.port         = port # 9559
		self.speechDevice = None
		self.recoDevice   = None
		self.memoryDevice = None
		self.aliceKernel  = None
		self.oldInput     = ""
		self.threshold    = 0.01
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
		self.speechDevice.setVoice(self.voice)		

		#CONNECT TO A SPEECH RECOGNITION PROXY
		try:
		    self.recoDevice = ALProxy("ALSpeechRecognition", self.host, self.port)
		except Exception, e:
		    print "Error when creating speech recognition device proxy:"+str(e)
		
		#SET UP RECOGNITION DEVICE    
		try:
			self.recoDevice.setLanguage("English")
			if(chat == False): 
				wordList = ["nao stand up","start up","go"]
			else:	
				"""
				dictFile = open("dictionary.pkl", "rb")
				dictio   = pickle.load(dictFile)
				dictFile.close()
				wordList = dictio.keys()
				"""	
				wordList = ["poor", "picture", "star", "monday", "good", "surprise"]
			self.recoDevice.setWordListAsVocabulary(wordList)	
			self.recoDevice.setParameter("EarUseFilter",1.0)	
			self.recoDevice.setParameter("EarUseSpeechDetector",2.0)
			self.recoDevice.setParameter("EarSpeed",2.0)
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
		    print "Error when creating speech recognition device proxy:"+str(e)
		
	#SORT DICTINARY_____________________________________________________________________________
	def getPredictedWords(self,predict,chat):
		if(chat == False):
			maxWord   = ""
			maxProbab = 0
			for(word,probab) in predict.items():
				if(maxProbab<probab):
					maxProbab = probab
					maxWord   = word	
			return maxWord
		else:
			predictedSent = ""
			for(word,probab) in predict.items():
				if(probab>self.threshold):
					predictedSent += word+" "
			predictedSent = predictedSent.strip()
	    	return predictedSent

	#CHAT WITH NAO__________________________________________________________________________________
	def naoChat(self,chat):
		inputSpeech = self.memoryDevice.getData("WordRecognized",0)

		print inputSpeech

		predict     = {}
		if(len(inputSpeech)>0):
			for i in range(0,len(inputSpeech)):
				if(i%2==1): #IF IT IS A PROBABILITY
					predict[inputSpeech[i-1]] = inputSpeech[i]
			predictedWords = self.getPredictedWords(predict,chat)

			print predict
			print predictedWords		

			if(predictedWords != self.oldInput):	 
				#RESPOND TO THE INPUT
				self.oldInput = predictedWords
				if(chat == True):
					aliceReply = self.aliceKernel.respond(predictedWords)
					aliceReply.lower().replace("alice", "nao")
					self.speechDevice.post.say(aliceReply)
				else:
					return predictedWords						

	#STOP CHATTING___________________________________________________________________________________
	def genSpeech(self, sentence):
		self.speechDevice.post.say(sentence)

	#STOP CHATTING___________________________________________________________________________________
	def stopSpeechReco(self):
		time.sleep(2)
		self.recoDevice.unsubscribe("MyModule") 


