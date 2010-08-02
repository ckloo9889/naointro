from get_nao_speech import *
naoSpeech = getNaoSpeech("127.0.0.1",9559)# "192.168.0.80",9559
naoSpeech.initDevice()
naoSpeech.naoChat()
naoSpeech.stopSpeechReco()

