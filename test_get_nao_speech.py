from get_nao_speech import *
naoSpeech = getNaoSpeech("192.168.0.80", 9559) #("127.0.0.1",9559)# 
naoSpeech.initDevice(True)
while True:
	naoSpeech.naoChat(True)
	if cv.WaitKey(10)==27:
		break
naoSpeech.stopSpeechReco()

