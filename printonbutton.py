#! /usr/bin/python

from time import sleep
import RPi.GPIO as GPIO
import printlabel


GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)  #button pin
GPIO.setup(17,GPIO.OUT) #led pin
GPIO.setup(27,GPIO.IN)  #distance sensor oin
GPIO.output(17, True)   #led ON - redy

z1 = not GPIO.input(4)
z2 = not GPIO.input(27)
z = z1 and z2
if (z == True):
   GPIO.output(17, False)
   GPIO.cleanup()
   quit()

printlabel.printlabel() #first label when ready

p = False
while True:
   z1 = not GPIO.input(4)
   z2 = not GPIO.input(27)
   z = z1 or z2
   if ( z != p ):
      if ( z == True ): 
         GPIO.output(17, False)
         printlabel.printlabel()
         sleep(2)
         GPIO.output(17, True)
		
	 #sleep(1)

   p = z

GPIO.output(17, False)
GPIO.cleanup()
