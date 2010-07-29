from getNaoImage import *
naoIm = getNaoImage("192.168.0.80","9559")
naoIm.initDevice()

while True:
	frame = naoIm.getImage()
	cv.ShowImage("image",frame)
	if cv.WaitKey(10)==27:
		break

naoIm.closeDevice()

