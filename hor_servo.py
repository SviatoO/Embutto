from RPIO import PWM

servo = PWM.Servo()

servo.set_servo(18, 1200)

#servo.set_servo(18, 2000)

servo.stop_servo(18)
