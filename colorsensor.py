#!/usr/bin/env micropython

from ev3dev2.motor import OUTPUT_A, OUTPUT_B, 
from ev3dev2.motor import MoveTank, SpeedPercent
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_1,INPUT_2,INPUT_3,INPUT_4
from ev3dev2.button import Button

from time import sleep

# Connect EV3 color sensor

class SpockbotsColorSensor:

    def __init__(self, number):
        """
        :param: number  number of color sensor on ev3
        """
        if number == 2:
            self.sensor = ColorSensor(INPUT_2)
        elif number == 3:
            self.sensor = ColorSensor(INPUT_3)
        elif number == 4:
            self.sensor = ColorSensor(INPUT_4)
        
        self.number = number
        self.black = 1000
        self.white = 0
        self.sensor.mode='COL-REFLECT'

    def set_white(self):
        value = self.sensor.reflected_light_intensity
        if value > self.white:
            self.white = value 
    
    def set_black(self):
        value = self.sensor.reflected_light_intensity
        if value < self.black:
            self.black = value 

    """def raw_value(self):
        if self.sensor.reflected_light_intensity >= 50:
            print("%3d" % (self.sensor.reflected_light_intensity, "\n"))
        sleep (5)
        return self.sensor.reflected_light_intensity
    """

    def value(self):
        val = self.sensor.reflected_light_intensity
        b = self.black
        t1 = val - b
        t2 = self.white - self.black
        ratio = t1 / t2
        c = ratio * 100
        if c < 0: 
            c = 0
        if c > 100:
            c = 100
        return c
    
    def calibrate(self):

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
        f.write("%3d, %3d" % (colorsensor[2].black, colorsensor[2].white))
        f.close()
        return colorsensor

    
class SpockbotsColorSensors:

    def __init__(self):
        self.colorsensor = [0,0,0,0,0]
        for i in [2,3,4]:
            self.colorsensor[i] = SpockbotsColorSensor(i)

    def value(i):
        return self.colorsensor[i].value()

    def calibrate(self):
        tank = MoveTank(OUTPUT_A, OUTPUT_B)
        tank.on(SpeedPercent(-5), SpeedPercent(-5))

        while True:

            txt = "exit"
            if button.check_buttons(buttons=['backspace']):
                break
            else:
                txt = "Press Backspace to Stop"

            #print("%s 2: %3d"  % ( txt, colorsensor[2].value(), "\n"))

            for i in [2,3,4]:
                colorsensor[i].set_white()
                colorsensor[i].set_black()

        tank.off()

        f= open("color_calibrate.txt","w")
        for i in [2,3,4]:
            f.write(colorsensor[i].black)
            f.write(colorsensor[i].white)
        f.close()

    def read(self):
        f= open("color_calibrate.txt","r")
        for i in [2,3,4]:
            colorsensor[i].black = int(f.read())
            colorsensor[i].white = int(f.read())
        f.close()



# from spockbots.colorsensor import SpockbotsColorSensors
# 
#  calibration
# 
#  colersensors = SpockbotsColorSensors()
#  colorsensors.calibrate()
#
#
# use
#
#  colersensors = SpockbotsColorSensors()
#  colorsensors.read()
#
#  colorsensor.value(2)




