from smbus2 import SMBus
from mlx90614 import MLX90614
import RPi.GPIO as GPIO
import time

#initialise IR sensor
bus = SMBus(1)
sensor = MLX90614(bus, address=0x5A)

#init Servo hor
horysontalServoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
horysontalServo = GPIO.PWM(horysontalServoPIN, 50) # GPIO 17 for PWM with 50Hz
horysontalServo.start(maxLeftAngle) # Initialization
#init Servo ver
verticalServoPIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
verticalServo = GPIO.PWM(verticalServoPIN, 50) # GPIO 18 for PWM with 50Hz
verticalServo.start(8.5) # Initialization

#start angle of ver servo
maxDownAngle = 8.5
#end angle of ver servo
maxUpAngle = 10.3

#max left angle for horys  
maxLeftAngle = 5.8
#max right angle of horys 
maxRightAngle = 8.6
#time needed for servo2 to turn
timeToTurn = getTime()

def getTime:
	horysontalServo.ChangeDutyCycle(maxLeftAngle)
	start = time.getTime()
	horysontalServo.ChangeDutyCycle(maxRightAngle)
	if(horysontalServo.angle() == maxRightAngle)
		endTime = time.getTime()


#how many times do we want to read value from IR
readCounter = 7
#delay between IR readings
readDelayTime = timeToTurn/readCounter








print sensor.get_amb_temp()
print sensor.get_obj_temp()
bus.close()