from PIL import Image
import pytesseract
import time
import mraa
import cv2  #from http://stackoverflow.com/questions/11094481/capturing-a-single-image-from-my-webcam-in-java-or-python
#import RPLCD
#import serial
import enchant
from enchant.checker import SpellChecker

cam = SimpleCV.Camera()


d = enchant.Dict()
checker = SpellChecker()
#lcd = CharLCD(cols=16, rows=2, pin_rs=12, pin_e=11, pins_data=[10,9,8,7])
sol1 = mraa.Gpio(6)
sol1.dir(mraa.DIR_OUT)
sol2 = mraa.Gpio(5)
sol2.dir(mraa.DIR_OUT)
sol3 = mraa.Gpio(4)
sol3.dir(mraa.DIR_OUT)
sol4 = mraa.Gpio(3)
sol4.dir(mraa.DIR_OUT)
sol5 = mraa.Gpio(2)
sol5.dir(mraa.DIR_OUT)
sol6 = mraa.Gpio(1)
sol6.dir(mraa.DIR_OUT)

letA = [1,0,0,0,0,0]
letB = [1,1,0,0,0,0]
letC = [1,0,0,1,0,0]
letD = [1,0,0,1,1,0]
letE = [1,0,0,0,1,0]
letF = [1,1,0,1,0,0]
letG = [1,1,0,1,1,0]
letH = [1,1,0,0,1,0]
letI = [0,1,0,0,1,0]
letJ = [0,1,0,1,1,0]
letK = [1,0,1,0,0,0]
letL = [1,1,1,0,0,0]
letM = [1,0,1,1,0,0]
letN = [1,0,1,1,1,0]
let0 = [1,0,1,0,1,0]
letP = [1,1,1,1,0,0]
letQ = [1,1,1,1,1,0]
letR = [1,1,1,0,1,0]
letS = [0,1,1,1,0,0]
letT = [0,1,1,1,1,0]
letU = [1,0,1,0,0,1]
letV = [1,1,1,0,0,1]
letW = [0,1,0,1,1,1]
letX = [1,0,1,1,0,1]
letY = [1,0,1,1,1,1]
letZ = [1,0,1,0,1,1]
letPound = [0,0,1,1,1,1]
letPer = [0,1,0,0,1,1]
letComm = [0,1,0,0,0,0]
letQuest = [0,1,1,0,0,1]
letSemi = [0,1,1,0,0,0]
letExec = [0,1,1,0,1,0]
reset = [1,1,1,1,1,1]

def setPin(letPin):
	digPin = 6
	sol1.write(abs(1-letPin[0]))
	sol2.write(abs(1-letPin[1]))
	sol3.write(abs(1-letPin[2]))
	sol4.write(abs(1-letPin[3]))
	sol5.write(abs(1-letPin[4]))
	sol6.write(abs(1-letPin[5]))
image_file = cam.getImage()
image_file.save("filename.jpg")
#image_file = 'unnamed.jpg'
im = Image.open(image_file) #opening image file
im = im.save('test.tif')
im = Image.open('test.tif') #change image format
im.load()
im.split()
#arduino = serial.Serial('/dev/tty.usbmodemFA131', 9600, timeout=2) #open connection to serial port
time.sleep(2)
text = pytesseract.image_to_string(im) #run Tesseract library to convert image to string
#arduino.write(text)
print "=====output=======\n"
print text
#checker.set_text(text)
for error in checker:
	#print "Mispelled Word: ", error.word
	#print d.suggest(error.word)
	text = text.replace(error.word,d.suggest(error.word)[0],1)
print text

while(len(text)>0):

	char1 = text[0]
	print char1
	if(char1 == "A" or char1 == "a"):
		setPin(letA)
	if(char1 == "B" or char1 == "b"):
		setPin(letB)
	if(char1 == "C" or char1 == "c"):
		setPin(letC)
	if(char1 == "D" or char1 == "d"):
		setPin(letD)
	if(char1 == "E" or char1 == "e"):
		setPin(letE)
	if(char1 == "F" or char1 == "f"):
		setPin(letF)
	if(char1 == "G" or char1 == "g"):
		setPin(letG)
	if(char1 == "H" or char1 == "h"):
		setPin(letH)
	if(char1 == "I" or char1 == "i"):
		setPin(letI)
	if(char1 == "J" or char1 == "j"):
		setPin(letJ)
	if(char1 == "K" or char1 == "k"):
		setPin(letK)
	if(char1 == "L" or char1 == "l"):
		setPin(letL)
	if(char1 == "M" or char1 == "m"):
		setPin(letM)
	if(char1 == "N" or char1 == "n"):
		setPin(letN)
	if(char1 == "O" or char1 == "o"):
		setPin(letO)
	if(char1 == "P" or char1 == "p"):
		setPin(letP)
	if(char1 == "Q" or char1 == "q"):
		setPin(letQ)
	if(char1 == "R" or char1 == "r"):
		setPin(letR)
	if(char1 == "S" or char1 == "s"):
		setPin(letS)
	if(char1 == "T" or char1 == "t"):
		setPin(letT)
	if(char1 == "U" or char1 == "u"):
		setPin(letU)
	if(char1 == "V" or char1 == "v"):
		setPin(letV)
	if(char1 == "W" or char1 == "w"):
		setPin(letW)
	if(char1 == "X" or char1 == "x"):
		setPin(letX)
	if(char1 == "Y" or char1 == "y"):
		setPin(letY)
	if(char1 == "Z" or char1 == "z"):
		setPin(letZ)
	if(char1 == "#"):
		setPin(letPound)
	if(char1 == "."):
		setPin(letPer)
	if(char1 == ","):
		setPin(letComm)
	if(char1 == "?"):
		setPin(letQuest)
	if(char1 == "!"):
		setPin(letExec)
	if(char1 == ";"):
		setPin(letSemi)
	#command = 'c1%s' % char1
	#arduino.write(command) #write each character of the string onto the serial port
	time.sleep(5)
	text = text[1:]
	setPin(reset)
	time.sleep(1.5)

#print arduino.read()

#out.close()

#print text
#arduino.close()
