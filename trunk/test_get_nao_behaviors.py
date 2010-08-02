from get_nao_behaviors import *
naoBeh = getNaoBehaviors("127.0.0.1",9559)# "192.168.0.80",9559
naoBeh.initDevice()
naoBeh.callBehavior("hello/behavior.xar")

