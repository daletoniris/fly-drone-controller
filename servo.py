import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BOARD)
 
motor1 = 3
aux = 11
GPIO.setup(aux,GPIO.IN) 
GPIO.setup(motor1,GPIO.OUT)
if aux == 1:
 print "Turning motor on"
 GPIO.output(motor1,GPIO.HIGH)

 
sleep(2)
 
print "Stopping motor"

 
GPIO.cleanup()
