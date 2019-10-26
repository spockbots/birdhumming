#!/usr/bin/env micropython

import spockbots.robot as robot
from spockbots.run_test1 import run_test1
from spockbots.run_test2 import run_test2


while True:
    txt = "exit"
    if robot.button('backspace'):
        break
    elif robot.button('up'):
        run_swing()
    elif robot.button('down'):
        run_tree()
    elif robot.button('left'):
        run_test1()
    elif robot.button('right'):
        run_test2()


print(txt)
robot.flash()
