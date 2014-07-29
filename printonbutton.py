from time import sleep
import shutil
import setbarcode
import os
import RPi.GPIO as GPIO
from datetime import datetime



GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)  #button pin
GPIO.setup(17,GPIO.OUT) #led pin
GPIO.setup(27,GPIO.IN)  #distance sensor oin
GPIO.output(17, True)   #led ON - redy

fdev = '/dev/lp0'

p = False
while True:
   z1 = not GPIO.input(4)
   z2 = not GPIO.input(27)
   z = z1 or z2
   if ( z != p ):
      if ( z == True ): 
         GPIO.output(17, False)
         setbarcode.barcodefromconfig()
         if os.path.exists(fdev):
            shutil.copy('/home/pi/barcode.bas', fdev)
	    str = "print " + datetime.utcnow().strftime("%a %b %d %H:%M:%S EEST %Y ") + "\n"
            with open('/home/pi/prnt.log','a') as fl:
               fl.write(str)
                      
         else:
	    str = "error " + datetime.utcnow().strftime("%a %b %d %H:%M:%S EEST %Y ") + "\n"
            with open('/home/pi/prnt.log','a') as fl:
               fl.write(str)
                    
         sleep(2)
         GPIO.output(17, True)
		
	 #sleep(1)

   p = z

GPIO.output(17, False)
GPIO.cleanup()
