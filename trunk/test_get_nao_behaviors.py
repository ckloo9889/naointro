from get_nao_behaviors import *
naoBeh = getNaoBehaviors("192.168.0.80",9559)# "192.168.0.80",9559
naoBeh.initDevice()
naoBeh.callBehavior("standup")

