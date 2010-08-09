from get_nao_speech import *
naoSpeech = getNaoSpeech("192.168.0.80", 9559, "Heather22Enhanced") #("127.0.0.1",9559)# 
naoSpeech.initDevice(False)
for i in range(0,1000):
	result = naoSpeech.naoChat(False)
	naoSpeech.genSpeech(result)
naoSpeech.stopSpeechReco()

