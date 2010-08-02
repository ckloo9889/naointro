from get_nao_behaviors import *
naoBeh = getNaoBehaviors("172.0.0.0",9559)# "192.168.0.80",9559
naoBeh.initDevice()
naoBeh.callBehavior("move_rpsBeginGame.xar")

