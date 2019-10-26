#!/usr/bin/env micropython

import spockbots.robot as robot
import math

txt = "run"
print(txt)
robot.flash()

while True:

    if robot.button('backspace'):
        break
    elif robot.button('up'):
        #push to circle 1
        robot.forward(25, 36)
        robot.forward(-25, 36)
    elif robot.button('down'):
        #push to circle 2
        #rotations=distance_to_rotation(65)
        #tank.on_for_rotations(40, 40,rotations)
        robot.forward(40, 65)
        robot.forward(-20, 63) 
    elif robot.button('left'):
        # two way gate for swing
        #may need to change distance to 145 at full charge
        robot.forward(-20, 150)
        robot.forward(20, 30)   

    elif robot.button('right'):
        motorD = MediumMotor(OUTPUT_D)
        #medium motor must on port D; full speed is 900; 
        #30 turns 30 degrees clockwise; -30 turns other way
        # be sure to use wait_while('running')!
        motorD.run_to_rel_pos(position_sp=30, speed_sp=100, stop_action="brake")
        motorD.wait_while('running')
        motorD.run_to_rel_pos(position_sp=-30, speed_sp=100, stop_action="brake")
        motorD.wait_while('running')

        #trying to go up ramp not working
        #robot.forward(-30, 100)
        #robot.forward(30, 40)
        
        #run_test2()
	#robot.forward(-30, 100)
	#robot.right_degrees(30, 180)
	#robot.forward(-50, 110)
           

