import RPi.GPIO as GPIO
import time

servoPIN = 18
#secondPin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
#GPIO.setup(secondPin, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(50) # Initialization
#pin = GPIO.PWM(secondPin, 50)
#pin.start(50)

for i in range(56, 86)
  p.ChangeDutyCycle(i/10)
  time.sleep(10)
  
try:
  print("ASDA")
  while True:
    print("input p")
    num1 = float(input())
    p.ChangeDutyCycle(num1)
    time.sleep(1)
    #print("input pin:")
    #num2 =int(input())
    #p.ChangeDutyCycle(num2)
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()
