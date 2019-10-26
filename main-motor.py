#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import time
import math
# Write your program here
brick.sound.beeps(1)
#brick.sound.beep(60)
#brick.sound.beep(1000, 1000, 50)
leftmotor = Motor (Port.A)
rightmotor = Motor (Port.D)

diameter = 56
axletrack = 114

#robot = DriveBase (left, right, diameter, axletrack)


#robot.drive(200, 0.5)

def forward(speed,distance):
    circumferance = diameter * math.pi
    angle = (distance * 360) / circumferance
    leftmotor.run_angle(speed,angle,Stop.COAST,False)
    rightmotor.run_angle(speed,angle,Stop.COAST,False)

def left(speed, angle):
    leftmotor.run_angle(speed,-angle,Stop.COAST,False)
    rightmotor.run_angle(speed,angle,Stop.COAST,False)
    time.sleep(1)

def right(speed, angle):
    rightmotor.run_angle(speed,-angle,Stop.COAST,False)
    leftmotor.run_angle(speed,angle,Stop.COAST,False)
    time.sleep(1)

#forward(1000,500)
left (1000, 180)

right(1000, 180)
time.sleep(3)