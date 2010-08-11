import sys
import thread
import math
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
		self.nao1       = NaoConfig("192.168.0.87", 9559) #"127.0.0.1", 9559
		self.nao1Speech = getNaoSpeech(self.nao1.ip, self.nao1.port, "Kenny22Enhanced")
		self.nao1Speech.initDevice(False)
		self.nao1Arm    = getNaoArmMoves(self.nao1.ip, self.nao1.port)
		self.nao1Arm.initDevice()
		self.nao1Head   = getNaoHeadMoves(self.nao1.ip, self.nao1.port)
		self.nao1Head.initDevice()
		self.nao1Legs   = getNaoLegMoves(self.nao1.ip, self.nao1.port)
		self.nao1Legs.initDevice()

		self.nao2         = NaoConfig("192.168.0.80", 9559) #"127.0.0.1", 9559
		self.nao2Speech   = getNaoSpeech(self.nao2.ip, self.nao2.port, "Heather22Enhanced")
		self.nao2Speech.initDevice(False)
		self.nao2Legs     = getNaoLegMoves(self.nao2.ip, self.nao2.port)
		self.nao2Legs.initDevice()
		self.nao2Behavior = getNaoBehaviors(self.nao2.ip, self.nao2.port)
		self.nao2Behavior.initDevice()

	#SEND NAOS TO THE INITIAL POSITIONS IN THE SPACE_____________________________________________	
	def initDemo(self):
		self.nao1.initDevice()
		self.nao1.initPos()
		self.nao2.initDevice()
		self.nao2.initPos()
		
		lockNaos = thread.allocate_lock()
		lockNaos.acquire(1)
		try:
			thread.start_new_thread(self.nao1Legs.walkTo, (0.3,0.3,0))
			thread.start_new_thread(self.nao2Legs.walkTo, (0.3,-0.3,0))
		except Exception,e:
			print "error in threading while walking to initial position "+str(e)	
			lockNaos.release()
		lockNaos.release()		
			
		#NAO2 IS SITTING
		self.nao2Behavior.callBehavior("sitdown")

		#NAO1 IS HOLDING A BOTTLE
		self.nao1Arm.initPosHoldBottle()

	#MAKE NAO2(RED) WALK TO NAO1(BLUE)_______________________________________________________________________________					
	def nao2Walk2Nao1(self):
		posNao1 = self.nao1Legs.motionDevice.getRobotPosition(True)	
		posNao2 = self.nao2Legs.motionDevice.getRobotPosition(True)
		
		print "BLUE NAO >> "+str(posNao1)
		print "RED NAO >> "+str(posNao2)
		
		nao2Legs.walkTo(math.fabs(posNao1[0]-posNao2[0])-0.1,
						math.fabs(posNao1[1]-posNao2[1]),
						math.fabs(posNao1[2]-posNao2[2]))

	#DEMO1: RELEASE BOTTLE__________________________________________________________________________________										
	def startDemo1(self):
		time.sleep(3)

		#NAO1 CALLS FOR NAO2
		self.nao1Speech.genSpeech("Hey Nao Get up")
		time.sleep(1)
		self.nao1Speech.genSpeech("Holiday is over Get up")
		time.sleep(1)
		self.nao1Head.moveHeadYawAbs([90],[2.0])
		time.sleep(1)
		self.nao1Speech.genSpeech("Nao wont get up, can you all together ask him to get up on my count of three?")
		time.sleep(1)
		self.nao1Speech.genSpeech("1 2 3")
		
		#REPLACE THIS WITH RECOGNITION!!!!!
		time.sleep(5)

		#NAO2 GETS UP AND WALKS TO NAO1
		self.nao2Walk2Nao1()

		#NAO2 RECOGNIZES IF THE CROWD SAID "GO" & NAO1 RELEASES THE BOTTLE		
		self.nao2Speech.genSpeech("what's up? What are you holding that bottle for?")
		time.sleep(1)
		self.nao1Speech.genSpeech("We have to open the new Informatics institute today!")
		time.sleep(1)
		self.nao2Speech.genSpeech("How do we do that?")
		time.sleep(1)
		
		#NAO1 POINTS TOWARS AIBO ?!?!
	
		self.nao1Speech.genSpeech("All we have to do is hit that button over there")
		time.sleep(1)
		self.nao2Speech.genSpeech("OK then go!")
		time.sleep(3)
		self.nao2Speech.genSpeech("I can't hear you!")
		time.sleep(1)
		self.nao2Speech.genSpeech("we NEED to say go all together after 3")
		time.sleep(1)
		self.nao2Speech.genSpeech("1 2 3")

		#REPLACE THIS WITH RECOGNITION!!!!!		
		time.sleep(5)

		#NAO1 RELEASES THE BOTTLE
		nao1Arm.releaseBottle()

		self.nao1.stiffnessOff()
		self.nao2.stiffnessOff()

	#DEMO2: NAO1 & NAO2 TRY TO PUSH THE BUTTON_________________________________________________________________
	def startDemo2(self):
		"""
		nao1Speech = getNaoSpeech(self.nao1.ip, self.nao1.port,"Heather22Enhanced")
		nao1Speech.initDevice(False)
		nao1Speech.genSpeech("Hey Nao Get the fuck up")

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
		"""
				
naoDemo = NaoOpening()
naoDemo.initDemo()

#naoDemo.startDemo1()
#naoDemo.startDemo2()
		
		