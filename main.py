"""
Created by Ihor Chernyshev
Created on Apr 2025
This program controls servo through potentiometer
"""

import time
import board
import analogio
import pwmio
from adafruit_motor import servo

# setup
potentiometer = analogio.AnalogIn(board.GP26)
pwm = pwmio.PWMOut(board.A1, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo
my_servo = servo.Servo(pwm)

# This variable helps calculate exact angle at which servo should go
angle_val = const(365)

while True:
    potentiometer_val = potentiometer.value / angle_val
    my_servo.angle = potentiometer_val
  
