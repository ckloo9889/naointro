from get_nao_image import *
naoIm = getNaoImage("127.0.0.1",9559) # "192.168.0.80",9559
naoIm.initDevice()

while True:
	frame = naoIm.getImage()
	cv.ShowImage("image",frame)
	if cv.WaitKey(10)==27:
		break

naoIm.closeDevice()

