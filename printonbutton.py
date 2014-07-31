from time import sleep
import shutil
import setbarcode
import os
import RPi.GPIO as GPIO
from datetime import datetime

fdev = '/dev/usb/lp0'
flog = '/home/pi/prn.log'
fbar = '/home/pi/barcode.bas'

def printlabel():
    setbarcode.barcodefromconfig()
    if os.path.exists(fdev):
        shutil.copy(fbar, fdev)
        str = "print "
            
    else:
	str = "error "
        
    str = str + datetime.utcnow().strftime("%a %b %d %H:%M:%S EEST %Y ") + "\n"
    with open(flog,'a') as fl:
        fl.write(str)
        
    return 

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)  #button pin
GPIO.setup(17,GPIO.OUT) #led pin
GPIO.setup(27,GPIO.IN)  #distance sensor oin
GPIO.output(17, True)   #led ON - redy

printlabel() #first label when ready

p = False
while True:
   z1 = not GPIO.input(4)
   z2 = not GPIO.input(27)
   z = z1 or z2
   if ( z != p ):
      if ( z == True ): 
         GPIO.output(17, False)
         printlabel()
         sleep(2)
         GPIO.output(17, True)
		
	 #sleep(1)

   p = z

GPIO.output(17, False)
GPIO.cleanup()
