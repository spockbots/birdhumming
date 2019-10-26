#!/usr/bin/env micropython

import spockbots.robot as robot
from spockbots.run_test1 import run_test1
from spockbots.run_test2 import run_test2
import math
from ev3dev2.motor import OUTPUT_C, OUTPUT_D, SpeedPercent, LargeMotor, MediumMotor



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
        robot.forward(-20, 55)  
        robot.left_degrees(10, 70)
        robot.forward(-10, 8)
        robot.forward(10, 5)
        robot.forward(-10, 6)

    elif robot.button('right'):
        #run_test2()
	#robot.forward(-30, 100)
	#robot.right_degrees(30, 180)
	#robot.forward(-50, 110)
            motorD = MediumMotor(OUTPUT_D)
            motorD.run_to_rel_pos(position_sp=50, speed_sp=50)
            #motorD.run_to_rel_pos(position_sp=-360, speed_sp=50, stop_action="coast")

print(txt)
robot.flash()
