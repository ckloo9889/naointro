from get_nao_walk import *
naoWalk = getNaoWalk("127.0.0.1",9559) # "192.168.0.80",9559
naoWalk.initDevice()
#naoWalk.walkDirection(0.8, 0.0, -0.6) #PRAMETERS BETWEEN [-1.0,1.0]
naoWalk.walkTo(0.2,0.2,1.57) #X,Y in meters, theta in radians
naoWalk.stiffnessOff()

