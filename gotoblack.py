#!/usr/bin/env micropython

from ev3dev2.motor import OUTPUT_A, OUTPUT_B, MoveTank, SpeedPercent
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_2
from ev3dev2.button import Button

from ev3dev2.sensor import INPUT_2

from time import sleep
from spockbots.colorsensor import SpockbotsColorSensors



def gotoblack(speed, black, sensor):
    sensor = SpockbotsColorSensors()
    sensor.read()
    tank = MoveTank(OUTPUT_A, OUTPUT_B)
    tank.on(SpeedPercent(speed), SpeedPercent(speed))
    
    while (sensor.value() > black):
        pass

    tank.on(SpeedPercent(0), SpeedPercent(0))


gotoblack(25, 8, 2)