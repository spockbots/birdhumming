#!/usr/bin/env micropython

from ev3dev2.motor import OUTPUT_A, OUTPUT_B, MoveTank, SpeedPercent
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_2
from ev3dev2.button import Button

from ev3dev2.sensor import INPUT_2, INPUT_3, INPUT_4


from time import sleep


button = Button() # up, down, left, right, enter, backspace

# Connect EV3 color sensor
color_sensor_2 = ColorSensor(INPUT_2)
color_sensor_3 = ColorSensor(INPUT_3)
color_sensor_4 = ColorSensor(INPUT_4)

# Put the color sensor into COL-REFLECT mode
# to measure reflected light intensity.
# In this mode the sensor will return a value between 0 and 100
#cl.mode='COL-REFLECT'

color_sensor_2.mode='COL-REFLECT'
color_sensor_3.mode='COL-REFLECT'
color_sensor_4.mode='COL-REFLECT'



tank = MoveTank(OUTPUT_A, OUTPUT_B)
tank.on(SpeedPercent(50), SpeedPercent(50))
sleep(1.5)
tank.off()

#while True:
#
#    txt = "exit"
#    if button.check_buttons(buttons=['backspace']):
#        exit()
#    else:
#        txt = "AAAA"
#
#    sleep(0.5)
#    print("%s 2: %3d 3: %3d 4: %3d" % (
#        txt,
#        color_sensor_2.value(), 
#        color_sensor_3.value(), 
#        color_sensor_4.value()), 
#        end="\r")

#sleep(0.5)
# I get max 80 with white paper, 3mm separation 
# and 5 with black plastic, same separation
