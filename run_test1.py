from ev3dev2.sound import Sound
from time import sleep

sound = Sound()
sound.play_tone(1500, 2)

sound.play_file('/home/robot/sounds/Dog bark 1.wav')
sound.beep()

import spockbots.robot as robot

def run_test1():

    robot.beep()
    robot.led("LEFT", "RED")
    robot.led("RIGHT", "YELLOW")

    robot.flash()
    robot.sleep(1)
    robot.beep()
