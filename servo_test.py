import RPi.GPIO as GPIO
from time import sleep
servo_pin =17

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

p.start(0)
p1.start(0)
for angle in range (0, 180):
   rotation = angle / 18
   p.ChangeDutyCycle(rotation + 2,5)

for angle in range (180, 0):
   rotation = angle / 18
