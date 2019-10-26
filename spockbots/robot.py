from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D 
from ev3dev2.motor import MoveTank, SpeedPercent, LargeMotor, MediumMotor
from ev3dev2.sound import Sound
from ev3dev2.led import Leds
from ev3dev2.button import Button
import time
import math
from spockbots.colorsensor import SpockbotsColorSensors
from ev3dev2.wheel import Wheel

colersensors = SpockbotsColorSensors()

# Wheel https://www.bricklink.com/v2/catalog/catalogitem.page?P=86652c01#T=C
diameter=6.24 # mm
width=20      # mm
tire = Wheel(diameter, 20) # width is 20mm

sound = Sound()
leds = Leds()

tank = MoveTank(OUTPUT_B, OUTPUT_A)
tank.left_motor.polarity='inversed'
tank.right_motor.polarity='inversed'

ev3button = Button() 

def button(which):
    # which = up, down, left, right, enter, backspace
    return ev3button.check_buttons(buttons=[which])

def stop():
    tank.on(SpeedPercent(0), SpeedPercent(0))

def calibrate():
    colorsensors.calibrate()

def colorvalue(port):
    return colersensors.value(port)

def read():
    colersensors.read()

def gotoblack(speed, port, black=10):
    """
    The robot moves to the black line while using the sensor on the given port
    """
    tank.on(SpeedPercent(speed), SpeedPercent(speed))
    while (colorvalue(port) > black):
        pass
    stop()

def gotowhite(speed, sensor, white=90):
    """
    The robot moves to the black line while using the sensor on the given port
    """
    tank.on(SpeedPercent(speed), SpeedPercent(speed))
    while (colorvalue(port) < white):
        pass
    stop()



def forever():
    True

def reset_distance():
    """
    Resests the distnace measure of the motor to 0
    """
    raise NotImplementedError

def dist(cm):
    # check if the robot traveled the distance 
    raise NotImplementedError

def followline_simple(run, port):
    """
    Follows the line on a given port. 
    run is a True-False function. 
    If its true it continues.
    If its falls it stops

    Example:

    robot.followline_simple(robot.forever())

    """
    # this needs to be replaced with the spockbots color sensors
    cs = ColorSensor(port)
    cs.mode = 'COL-REFLECT'
 
    while (run):
        while (cs.value() < 15):
            tank.on(SpeedPercent(10), SpeedPercent(20))
        while (cs.value() > 15):
            tank.on(SpeedPercent(20), SpeedPercent(10))
    tank.on(SpeedPercent(0), SpeedPercent(0))

def sleep(seconds):
    """
    The robot will sleep for the number of seconds
    """
    time.sleep(seconds)

def beep():
    """
    The robot will make a beep
    """
    sound.beep()

def led(group, color):
    """
    The robot will switch on the LEDS with the given color

    group:
        LEFT
        RIGHT

    color:
        BLACK
        RED
        GREEN
        AMBER
        ORANGE
        YELLOW
    """
    # direction, LEFT
    # Color: GREEN, RED
    leds.set_color(group, color)
[]
def flash():
    """
    The robot will flash the LEDs and beep twice
    """
    sound.beep()
    sound.beep()

    for color in ["BLACK", "RED", "GREEN"]:
        led("LEFT", color)
        led("RIGHT", color)
        sleep(0.1)
        
def distance_to_rotation(distance):
    """
    calculation to convert the distence from 
    cm into rotations.
    """
    circumference=diameter*math.pi
    rotation=distance/circumference 
    return rotation 

def forward_rotations (speed, rotations):
    """
    The robot moves forward with the given number of 
    rotations
    """
    tank.on_for_rotations(speed,speed,rotations)

def left (speed,rotations):
    """
    The robot truns left with the number of rotations
    """
    tank.on_for_rotations(speed,-speed,rotations)

def left_degrees (speed,degrees):
    """
    The robot turns left with the given number of degrees
    """
    tank.on_for_degrees(speed,-speed,degrees)

def right (speed,rotations):
    """
    The robot turns right with the number of rotations
    """
    tank.on_for_rotations(-speed,speed,rotations)

def right_degrees (speed,degrees):
    """
    The robot turns left with the given number of degrees
    """
    tank.on_for_degrees(-speed,speed,degrees)

def left_90_degrees (speed):
    """
    The robot turns left by 90 degrees
    """
    if speed==25:
        sound.speak("slow left")
        left_degrees(speed,146.5)
    elif speed==40: 
        sound.speak("fast left")  
        raise NotImplementedError         

def right_90_degrees (speed):
    """
    The robot turns left by 90 degrees
    """
    if speed==25:
        sound.speak("slow right")
        right_degrees(speed,146.5)
    elif speed==40: 
        sound.speak("fast right")           
        raise NotImplementedError         

def forward(speed, distance):
    rotations=distance_to_rotation(distance)
    forward_rotations(speed, rotations)

 
# forward_rotations(10,1) 
# left(25,146.5)
# left_90_degrees(25)
# left_90_degrees(40)
# forward(25,100)
