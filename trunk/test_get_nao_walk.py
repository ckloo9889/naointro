from get_nao_leg_moves import *
from nao_config import *

nao2 = NaoConfig("192.168.0.80", 9559) #"127.0.0.1", 9559

nao2.initDevice()
nao2.initPos()

nao2Legs     = getNaoLegMoves(nao2.ip, nao2.port)
nao2Legs.initDevice()
nao2Legs.walkTo(0.3,-0.3,0)
nao2.stiffnessOff()