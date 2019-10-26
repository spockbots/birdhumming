#!/usr/bin/env micropython

from ev3dev2.motor import OUTPUT_A, OUTPUT_B, MoveTank, SpeedPercent
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_2
from ev3dev2.button import Button

from ev3dev2.sensor import INPUT_2

from time import sleep

button = Button() # up, down, left, right, enter, backspace

# Connect EV3 color sensor
from spockbots.colorsensor

colorsensor = [0,0,0]
for i in [2]:
    colorsensor[i] = SpockbotsColorSensor(i)


tank = MoveTank(OUTPUT_A, OUTPUT_B)
tank.on(SpeedPercent(-5), SpeedPercent(-5))


while True:

    txt = "exit"
    if button.check_buttons(buttons=['backspace']):
        break
    else:
        txt = "Press Backspace to Stop"

    #print("%s 2: %3d"  % ( txt, colorsensor[2].value(), "\n"))

    for i in [2]:
        colorsensor[i].set_white()
        colorsensor[i].set_black()

tank.off()

f= open("colcal2.txt","w+")
f.write("hi this is a test")
f.write("%3d, %3d" % (colorsensor[2].black, colorsensor[2].white))
f.close()
