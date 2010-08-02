from get_nao_arm_moves import *
naoArm = getNaoArmMoves("127.0.0.1",9559) #"192.168.0.80", 9559
naoArm.initDevice()
naoArm.initPos()
		
#naoArm.moveArm(0.2, -0.2, 0.5, 0.5, 0.9, 0.2, "open")
#time.sleep(3)
#naoArm.moveArm(-1.3, 0.2, -0.7, 1.8, -0.2, -0.4, "close")
#time.sleep(5)

naoArm.grabObject()

#naoArm.moveArmEllipse()
naoArm.stiffnessOff()
