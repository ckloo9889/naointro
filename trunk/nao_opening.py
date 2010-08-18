import sys
from threading import Thread
import threading
import math
import time
from nao_config import *
from get_nao_arm_moves import *
from get_nao_head_moves import *
from get_nao_walk import *
from get_nao_speech import *
from get_nao_behaviors import *
#__________________________________________________________________________________________
#__________________________________________________________________________________________
class NaoOpening:
	def __init__(self):
		self.nao1       = NaoConfig("192.168.0.90", 9559) #local: 127.0.0.1, 9559, wired: 192.168.0.87, wireless: 192.168.0.90
		self.nao1Speech = getNaoSpeech(self.nao1.ip, self.nao1.port, "Kenny22Enhanced")
		self.nao1Speech.initDevice(False)
		self.nao1Arm    = getNaoArmMoves(self.nao1.ip, self.nao1.port)
		self.nao1Arm.initDevice()
		self.nao1Head   = getNaoHeadMoves(self.nao1.ip, self.nao1.port)
		self.nao1Head.initDevice()
		self.nao1Legs   = getNaoLegMoves(self.nao1.ip, self.nao1.port)
		self.nao1Legs.initDevice()

		self.nao2         = NaoConfig("192.168.0.91", 9559) #local: 127.0.0.1, 9559, wired: 192.168.0.87, wireless: 192.168.0.91
		self.nao2Speech   = getNaoSpeech(self.nao2.ip, self.nao2.port, "Heather22Enhanced")
		self.nao2Speech.initDevice(False)
		self.nao2Legs     = getNaoLegMoves(self.nao2.ip, self.nao2.port)
		self.nao2Legs.initDevice()
		self.nao2Head   = getNaoHeadMoves(self.nao2.ip, self.nao2.port)
		self.nao2Head.initDevice()
		self.nao2Behavior = getNaoBehaviors(self.nao2.ip, self.nao2.port)
		self.nao2Behavior.initDevice()
                
		#GET INITIAL ROBOT POSITIONS
		self.initialPosNao1 = self.nao1Legs.motionDevice.getRobotPosition(True)	
		self.initialPosNao2 = self.nao2Legs.motionDevice.getRobotPosition(True)
                
	#SEND NAOS TO THE INITIAL POSITIONS IN THE SPACE_____________________________________________	
	def initDemo(self):
		self.nao1.initDevice()
		self.nao1.initPos()
		self.nao2.initDevice()
		self.nao2.initPos()
		
		lockNao2Legs = threading.Lock()
		lockNao1Legs = threading.Lock()
		#WALK TO INITIAL POSITION NAO2
		lockNao2Legs.acquire(1)
		try:
			nao2T1 = Thread(target=self.nao2Legs.walkTo, args = (0.0,-0.4,0))
			nao2T1.start()
		except Exception,e:
			print "error in threading while walking to initial position: "+str(e)
			lockNao2Legs.release()	
		lockNao2Legs.release()	

		#WALK TO INITIAL POSITION NAO1
		'''
		lockNao1Legs.acquire(1)
		try:
			nao1T1 = Thread(target=self.nao1Legs.walkTo, args=(0.3,0.3,0))
			nao1T1.start()
		except Exception,e:
			print "error in threading while walking to initial position: "+str(e)
			lockNao1Legs.release()	
		lockNao1Legs.release()
		nao1T1.join()
                '''	
		nao2T1.join()

		#INITALIZING POSITIONS NAO2
		lockNao2Legs.acquire(1)
		try:
			nao2T2 = Thread(target=self.nao2Behavior.callBehavior, args = ("sitdown",))
			nao2T2.start()
		except Exception,e:	
			print "error in threading while taking the initial positions: "+str(e)	
			lockNao2Legs.release()
		lockNao2Legs.release()

		#INITALIZING POSITIONS NAO1
		lockNao1Legs.acquire(1)
		try:
			nao1T2 = Thread(target=self.nao1Arm.initPosHoldBottle, args=())
			nao1T2.start()
		except Exception,e:	
			print "error in threading while taking the initial positions: "+str(e)	
			lockNao1Legs.release()
		lockNao1Legs.release()

		nao1T2.join()
		nao2T2.join()
		
	#MAKE NAO2(RED) WALK TO NAO1(BLUE)_______________________________________________________________________________					
	def nao2Walk2Nao1(self):
		posNao1 = self.nao1Legs.motionDevice.getRobotPosition(True)	
		posNao2 = self.nao2Legs.motionDevice.getRobotPosition(True)
		
		## SUBTRACT ACCUMULATED POSITION 
		posNao1[0] -= self.initialPosNao1[0]
		posNao1[1] -= self.initialPosNao1[1]
		posNao1[2] -= self.initialPosNao1[2]
		
		posNao2[0] -= self.initialPosNao2[0]
		posNao2[1] -= self.initialPosNao2[1]
		posNao2[2] -= self.initialPosNao2[2]

		print "BLUE NAO >> "+str(posNao1)
		print "RED NAO >> "+str(posNao2)
		
		self.nao2Legs.walkTo(math.fabs(posNao1[0]-posNao2[0])-0.4,
						math.fabs(posNao1[1]-posNao2[1]),
						math.fabs(posNao1[2]-posNao2[2]))

	#DEMO1: RELEASE BOTTLE__________________________________________________________________________________										
	def startDemo1(self):
		time.sleep(5)
		#NAO1 CALLS FOR NAO2
		self.nao1Head.moveHeadYawAbs([-60],[2.0])
		time.sleep(2)
		self.nao1Speech.genSpeech("Hey Nao stand up")
		time.sleep(2)
		self.nao1Speech.genSpeech("Holiday is over stand up")
		time.sleep(3)
		self.nao1Head.moveHeadYawAbs([0],[2.0])
		time.sleep(2)
		self.nao1Speech.genSpeech("Nao wont stand up, can you all together ask him to stand up on my count of three?")
		time.sleep(4)
		self.nao1Speech.genSpeech("1 2 3")
		#NAO2 TRIES TO RECOGNIZE THE AUDIENCE SAYING: "STAND UP"
		self.nao2Speech.startSpeechReco()
		#RESET THE MEMORY VARIABLE BEFORE RECOGNIZING AGAIN
		self.nao2Speech.resetRecoVariable()
		try:
			speechResult = self.nao2Speech.naoChat(False)
		except Exception,e:	
			print "error while executing the demo: "+str(e)	
			#STOP SPEECH RECO
			self.nao2Speech.stopSpeechReco()
		initial_time = time.time()				
		while(speechResult.find("stand up")==-1 and (time.time()-initial_time)<=5): #20 SECONDS HAVE PASSED OR NAO HAS RECOGNIZED "STAND UP"
			try:
				speechResult = self.nao2Speech.naoChat(False)
				if(speechResult.find("stand up")!=-1):
					print "recognized <<stand up>> ..."+str(time.time()-initial_time)

			except Exception,e:	
				print "error while executing the demo: "+str(e)	
				#STOP SPEECH RECO
				self.nao2Speech.stopSpeechReco()				
		self.nao2Speech.stopSpeechReco()

		#NOW NAO2 STANDUP	
		self.nao2Behavior.callBehavior('standup')
		time.sleep(5)		
		#NOW NAO2 WALKS TO NAO1	
		self.nao2Walk2Nao1()

		#NAO2 RECOGNIZES IF THE CROWD SAID "GO" & NAO1 RELEASES THE BOTTLE		
		time.sleep(2)
		#self.nao2Head.moveHeadYawAbs([40],[2.0])
		time.sleep(2)
		self.nao2Speech.genSpeech("what's up? What are you holding that bottle for?")
		time.sleep(3)

		self.nao1Head.moveHeadYawAbs([-40],[2.0])
		time.sleep(2)
		self.nao1Speech.genSpeech("We have to open the new Informatics institute today!")
		time.sleep(3)
		self.nao2Speech.genSpeech("How do we do that?")
		time.sleep(2)
		
		#NAO1 POINTS TOWARS AIBO ?!?!?!?!?!!?!?!?!?!?!?!?!!?
	
		self.nao1Speech.genSpeech("All we have to do is hit that button over there")
		time.sleep(4)
		self.nao2Speech.genSpeech("OK then go!")
		time.sleep(3)
		self.nao1Speech.genSpeech("I can not hear you!")
		time.sleep(3)
		self.nao2Head.moveHeadYawAbs([0],[2.0])
		self.nao1Head.moveHeadYawAbs([0],[2.0])
		self.nao2Speech.genSpeech("we need to say")
		time.sleep(1)
		self.nao2Speech.genSpeech("GO NAO") 
		time.sleep(1)
		self.nao2Speech.genSpeech("all together after 3")
		time.sleep(2)
		self.nao2Speech.genSpeech("1 2 3")

		#NAO2 TRIES TO RECOGNIZE THE AUDIENCE SAYING: "GO NAO"
		self.nao2Speech.startSpeechReco()
		#RESET THE MEMORY VARIABLE BEFORE RECOGNIZING AGAIN
		self.nao2Speech.resetRecoVariable()
		try:
			speechResult = self.nao2Speech.naoChat(False)
		except Exception,e:	
			print "error while executing the demo: "+str(e)	
			#STOP SPEECH RECO
			self.nao2Speech.stopSpeechReco()
		initial_time = time.time()
		while(speechResult.find("go nao")==-1 and (time.time()-initial_time)<=5): #20 SECONDS HAVE PASSED OR NAO HAS RECOGNIZED "GO NAO"
			try:
				speechResult = self.nao2Speech.naoChat(False)
				if(speechResult.find("go nao")!=-1):
					print "recognized <<go nao>>..."+str(time.time()-initial_time)
			except Exception,e:	
				print "error while executing the demo: "+str(e)	
				#STOP SPEECH RECO
				self.nao2Speech.stopSpeechReco()				
		self.nao2Speech.stopSpeechReco()

		#NAO1 RELEASES THE BOTTLE
		self.nao1Arm.releaseBottle()

		#self.nao1Legs.walkTo(0, 0.1, 0)


	#DEMO2: NAO1 & NAO2 TRY TO PUSH THE BUTTON_________________________________________________________________
	def startDemo2(self):
		'''
		nao1Speech = getNaoSpeech(self.nao1.ip, self.nao1.port,"Heather22Enhanced")
		nao1Speech.initDevice(False)
		nao1Speech.genSpeech("Hey Nao Get the $#%^@ up")

		nao1Leg = getNaoLegMoves(self.nao1.ip, self.nao1.port)
		nao1Leg.initDevice()
		nao1Arm = getNaoArmMoves(self.nao1.ip, self.nao1.port)
		nao1Arm.initDevice()

		nao1Leg.kneelDown()
		time.sleep(2)
		nao1Arm.moveArmsInFront()
		time.sleep(2)
		nao1Leg.bendForward()
		time.sleep(2)
		nao1Leg.sitStraight()
		time.sleep(2)
		self.nao1.stiffnessOff()
		'''
		
	def stopNao(self):
		self.nao1.initDevice()
		self.nao2.initDevice()

		self.nao1.stiffnessOff()
		self.nao2.stiffnessOff()

		
#_____________________________________________________________________________________________________________________				
#_____________________________________________________________________________________________________________________				
try:		
	naoDemo = NaoOpening()
	naoDemo.initDemo()
	naoDemo.startDemo1()
	#naoDemo.stopNao()
except Exception,e:	
	print "error while executing the demo: "+str(e)	
	#STOP SPEECH RECO
	naoDemo.nao2Speech.stopSpeechReco()		
		
#naoDemo.startDemo1()
#naoDemo.startDemo2()
		
		
