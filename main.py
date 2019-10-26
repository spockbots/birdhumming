#!/usr/bin/env micropython

import spockbots.robot as robot
from spockbots.run_test1 import run_test1
from spockbots.run_test2 import run_test2
import math


while True:
    txt = "exit"
    if robot.button('backspace'):
        break
    elif robot.button('up'):
        #run_swing()
	robot.forward(-20, 36)
	robot.forward(20, 36)
    elif robot.button('down'):
        #run_tree()
	robot.forward(-20, 60)
	robot.forward(20, 60)
    elif robot.button('left'):
        #run_test1()
	robot.forward(-20, 138)
	robot.forward(20,20)
	robot.forward(-20,20)
	robot.forward(20,20)
    elif robot.button('right'):
        #run_test2()
	robot.forward(-30, 100)
	robot.right_degrees(30, 180)
	robot.forward(-50, 110)


print(txt)
robot.flash()
