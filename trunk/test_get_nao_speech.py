from get_nao_speech import *
naoSpeech = getNaoSpeech("192.168.0.80", 9559, "Heather22Enhanced") #("127.0.0.1",9559)# 
naoSpeech.initDevice(False)
contor = 0
while(contor<5):
	result = naoSpeech.naoChat(False)
	if(len(result)>0):
		contor += 1
		#naoSpeech.genSpeech("you said "+result)
	if cv.WaitKey(10) >= 0:
		break    
naoSpeech.stopSpeechReco()

