import sys
from nao_config import *
from get_nao_arm_moves import *
from get_nao_head_moves import *
from get_nao_speech import *


class NaoOpening:
	def __init__(self):
		self.nao1 = NaoConfig("192.168.0.87", 9559)
		#self.nao1 = NaoConfig("127.0.0.1", 9559)
		self.nao1.initDevice()
		self.nao1.initPos()
	
	def startDemo(self):
		nao1Arm = getNaoArmMoves(self.nao1.ip, self.nao1.port)
		nao1Arm.initDevice()
		nao1Arm.initPos()
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

		self.nao1.stiffnessOff()

naoDemo = NaoOpening()
naoDemo.startDemo()		
		
		