import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

horyzontal_servo = GPIO.PWM(11, 50)
vertical_servo = GPIO.PWM(12, 50)

horyzontal_servo.start(0)
vertical_servo.start(0)

time.sleep(2)

def SetAngle(angle):
	duty = angle / 18 + 2
	GPIO.output(11, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(11, False)
	pwm.ChangeDutyCycle(0)

SetAngle(90)
