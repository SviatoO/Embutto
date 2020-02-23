import RPi.GPIO as GPIO
import time

servoPIN = 17
secondPin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
GPIO.setup(secondPin, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(50) # Initialization
pin = GPIO.PWM(secondPin, 50)
pin.start(50)
try:
  while True:
    print("input p")
    num1 = int(input())
    p.ChangeDutyCycle(num1)
    time.sleep(1)
    print("input pin:")
    num2 =int(input())
    p.ChangeDutyCycle(num2)
    print("input your value")
    num1 = int(input())
    p.ChangeDutyCycle(num1)
    time.sleep(0.5)
    p.ChangeDutyCycle(2)
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()
