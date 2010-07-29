from getNaoBehaviors import *
naoBeh = getNaoBehaviors("192.168.0.80","9559")
naoBeh.initDevice()
naobeh.callBehavior("move_rpsBeginGame.xar")

