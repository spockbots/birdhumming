import spockbots.robot as robot

def run_test1():

    robot.beep()
    robot.led("LEFT", "RED")
    robot.led("RIGHT", "YELLOW")

    robot.flash()
    robot.sleep(1)
    robot.beep()
