#!/usr/bin/env micropython

from ev3dev2.motor import OUTPUT_A, OUTPUT_B, SpeedPercent, 
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_2
from ev3dev2.button import Button


from time import sleep

def diagonal_lift(speed, degree, portA, portB):
    motorA = MediumMotor(portA)
    motorB = MediumMotor(portB)
    
    #positive speed could run motor clockwise or counter-clockwise
    #if so, uncomment line below
    #speed = speed * -1
    motorA.run_to_rel_pos(degree, speed)
    motorB.run_to_rel_pos(degree, speed)
