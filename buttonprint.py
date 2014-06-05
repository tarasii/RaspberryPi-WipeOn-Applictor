from time import sleep
import os
import RPi.GPIO as GPIO

def getch():
	import sys, tty, termios
	old_settings = termios.tcgetattr(0)
	new_settings = old_settings[:]
	new_settings[3] &= ~termios.ICANON & ~termios.ECHO
	new_settings[6][termios.VMIN]=1
	new_settings[6][termios.VTIME]=0
	try:
		termios.tcsetattr(0, termios.TCSANOW, new_settings)
		ch = sys.stdin.read(1)
	finally:
		termios.tcsetattr(0, termios.TCSANOW, old_settings)
	return ch


GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.IN)
GPIO.output(17, False)

#c = getch()
#print "helo"
#print c

p = False
#while ( ord(c) != 27 ):
while True:
	#c = getch()
	z1 = not GPIO.input(4)
	z2 = not GPIO.input(27)
	#c = getch()
	#print c
	z = z1 or z2
	if ( z != p ):
		#print z
		if ( z == True ): 
		        GPIO.output(17, True)
			os.system("/home/pi/printbarcode.sh")
			sleep(2)
		        GPIO.output(17, False)
		
		#sleep(1)

	p = z

GPIO.output(17, True)
GPIO.cleanup()
