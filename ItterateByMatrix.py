import smbus
import RPi.GPIO as GPIO
import time
import numpy

class MLX90614():

    MLX90614_RAWIR1=0x04
    MLX90614_RAWIR2=0x05
    MLX90614_TA=0x06
    MLX90614_TOBJ1=0x07
    MLX90614_TOBJ2=0x08

    MLX90614_TOMAX=0x20
    MLX90614_TOMIN=0x21
    MLX90614_PWMCTRL=0x22
    MLX90614_TARANGE=0x23
    MLX90614_EMISS=0x24
    MLX90614_CONFIG=0x25
    MLX90614_ADDR=0x0E
    MLX90614_ID1=0x3C
    MLX90614_ID2=0x3D
    MLX90614_ID3=0x3E
    MLX90614_ID4=0x3F

    def __init__(self, address=0x5a, bus_num=1):
        self.bus_num = bus_num
        self.address = address
        self.bus = smbus.SMBus(bus=bus_num)

    def read_reg(self, reg_addr):
        return self.bus.read_word_data(self.address, reg_addr)

    def data_to_temp(self, data):
        temp = (data*0.02) - 273.15
        return temp

    def get_amb_temp(self):
        data = self.read_reg(self.MLX90614_TA)
        return self.data_to_temp(data)

    def get_obj_temp(self):
        data = self.read_reg(self.MLX90614_TOBJ1)
        return self.data_to_temp(data)


sensor = MLX90614()
print(sensor.get_amb_temp())
print(sensor.get_obj_temp())



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
#current state
currentHorValue = 0
#row numbers
rows = 4

#max left angle for horys  
maxLeftAngle = 5.8
#max right angle of horys 
maxRightAngle = 8.6

#num of readings of IR value
readCounter = 7
horisontalStep = (maxRightAngle - maxLeftAngle) / readCounter

def setOnTopLeft():
    verticalServo.ChangeDutyCycle(maxUpAngle)
    horysontalServo.ChangeDutyCycle(maxLeftAngle)
    currentHorValue = maxUpAngle

irValues = np.array([readCounter, rows])
row = 0


def turnRight():
    angle = maxLeftAngle
    horysontalServo.ChangeDutyCycle(angle)
    cul = 0

    While(angle != maxRightAngle):
        angle += horisontalStep;
        horysontalServo.ChangeDutyCycle(angle)
        irValues[row,cul ] = sensor.get_obj_temp()
        cul++
    

def turnLeft():
    angle = maxRightAngle
    horysontalServo.ChangeDutyCycle(angle)
    cul = 0

    While(angle != maxLeftAngle):
        angle -= horisontalStep;
        horysontalServo.ChangeDutyCycle(angle)
        irValues[row,cul ] = sensor.get_obj_temp()
        cul++

def turnDown():
    verticalServo.ChangeDutyCycle(currentHorValue - ((maxUpAngle - maxDownAngle)/rows) )

    row++


