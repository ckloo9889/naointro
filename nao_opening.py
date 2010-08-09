import sys
from nao_config import *
from get_nao_arm_moves import *
from get_nao_head_moves import *
from get_nao_walk import *
from get_nao_speech import *
from get_nao_behaviors import *

class NaoOpening:
	def __init__(self):
		self.nao1 = NaoConfig("192.168.0.87", 9559)
		#self.nao1 = NaoConfig("127.0.0.1", 9559)
		self.nao1.initDevice()
		self.nao1.initPos()

		#self.nao2 = NaoConfig("192.168.0.80", 9559)
		#self.nao2 = NaoConfig("127.0.0.1", 9559)
		#self.nao2.initDevice()
		#self.nao2.initPos()
		
		#nao2Behave = getNaoBehaviors(self.nao2.ip, self.nao2.port)
		#nao2Behave.initDevice()
		#nao2Behave.callBehavior("sitdown")

		self.nao1.stiffnessOff()
		#self.nao2.stiffnessOff()
		
					
	def nao2Walk2Nao1(self,nao1Legs,nao2Legs):
		#name           = "CameraTop"
		#space          = 2
		#useSensorValue = True
		#result1 = nao1Legs.motionDevice.getPosition(name,space,useSensorValue)	
		#result2 = nao2Legs.motionDevice.getPosition(name,space,useSensorValue)	
		result1 = nao1Legs.motionDevice.getRobotPosition(True)	
		result2 = nao2Legs.motionDevice.getRobotPosition(True)
		print result1
		print result2
		
		
		nao2Legs.walkTo(100*result1[0]-result2[0],100*result1[1]-result2[1],result1[2]-result2[2])
					
	def startDemo1(self):
		
	
		'''
		nao1Arm = getNaoArmMoves(self.nao1.ip, self.nao1.port)
		nao1Arm.initDevice()
		nao1Arm.initPosHoldBottle()
		time.sleep(5)
		nao1Head = getNaoHeadMoves(self.nao1.ip, self.nao1.port)
		nao1Head.initDevice()

		nao1Speech = getNaoSpeech(self.nao1.ip, self.nao1.port,"Heather22Enhanced")
		nao1Speech.initDevice(False)
		time.sleep(3)
		nao1Speech.genSpeech("Hey Nao Get up")
		time.sleep(1)
		nao1Speech.genSpeech("Holiday is over Get up")
		time.sleep(1)
		nao1Head.moveHeadYawAbs([90],[2.0])
		time.sleep(1)
		nao1Speech.genSpeech("Nao wont get up, can you all together ask him to get up on my count of three?")
		time.sleep(1)
		nao1Speech.genSpeech("1 2 3")
		time.sleep(5)
		nao1Arm.releaseBottle()

		nao1Legs  = getNaoLegMoves(self.nao1.ip, self.nao1.port)
		nao1Legs.initDevice()
		nao2Legs  = getNaoLegMoves(self.nao2.ip, self.nao2.port)
		nao2Legs.initDevice()
		self.nao2Walk2Nao1(nao1Legs,nao2Legs)
		#self.nao1.stiffnessOff()
		'''
		
		

	def startDemo2(self):
		#nao1Speech = getNaoSpeech(self.nao1.ip, self.nao1.port,"Heather22Enhanced")
		#nao1Speech.initDevice(False)
		#nao1Speech.genSpeech("Hey Nao Get the fuck up")

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
		
				
naoDemo = NaoOpening()
#naoDemo.startDemo1()
#naoDemo.startDemo2()
		
		