import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

servo_horizontal = GPIO.PWM(18, 50)
servo_vertical = GPIO.PWM(17, 50)
servo_vertical.start(0)
servo_horizontal.start(0)


def SetVertycalAngle(angle):
	duty_vertical = angle / 18 + 2
	GPIO.output(17, True)
	servo_vertical.ChangeDutyCycle(duty_vertical)
	sleep(1)
	GPIO.output(17, False)
	servo_vertical.ChangeDutyCycle(0)

def SetHorizontalAngle(angle):
	duty_horizontal = angle / 18 + 2
	GPIO.output(18, True)
	servo_horizontal.ChangeDutyCycle(duty_horizontal)
	sleep(1)
	GPIO.output(18, False)
	servo_horizontal.ChangeDutyCycle(0)

#SetVertycalAngle(90)
#SetHorizontalAngle(90)
while 1:
    print('Input value: ')
    val = int(input())
    servo_horizontal.ChangeDutyCycle(val)

pwm.stop()
GPIO.cleanup()
