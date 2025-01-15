
# Library imports
from vex import *

controller_1 = Controller(PRIMARY) ##This is the controller object so we can get input from the controls
conveyer = Motor(Ports.PORT1, GearSetting.RATIO_6_1, True)  #conveyor belt connect to port 1
right_motor = Motor(Ports.PORT9, GearSetting.RATIO_18_1, True) 
left_motor = Motor(Ports.PORT10, GearSetting.RATIO_18_1, False)   #port 10 connect to the left, port 9 connect to the right
#swipe on 11, front black thingy on 13
swipe = Motor(Ports.PORT11, GearSetting.RATIO_6_1,True)
FrontSpindle = Motor(Ports.PORT13, GearSetting.RATIO_18_1, True)

claw.set(False)

def conveyerstart():
    conveyer.spin(FORWARD)
def conveyerreverse():
    conveyer.spin(REVERSE)
def conveyerstop():
    conveyer.stop()
def spindlestart():
    FrontSpindle.spin(FORWARD)
def spindlestop():
    FrontSpindle.stop()


def ClawUp():
    claw.set(False)
def ClawDown():
    claw.set(True)
    

def SwipeUpDown():
    if swipe.position(DEGREES) == 0:
        swipe.spin_to_position(90,DEGREES,wait=True)
    else:
        swipe.spin_to_position(0,DEGREES,wait=True)


def foward(length):
    length = length / 13.5
    right_motor.spin_for(FORWARD,length,TURNS,wait=False)  #one full turn will move 13.5 inches
    left_motor.spin_for(FORWARD,length,TURNS,wait=False)
def backward(length):
    length = length / 13.5
    right_motor.spin_for(REVERSE,length,TURNS,wait=False)
    left_motor.spin_for(REVERSE,length,TURNS,wait=False)
def right(degree):
    degree = degree / 90 * 0.96
    left_motor.spin_for(FORWARD,degree,TURNS,wait=False) 
    right_motor.spin_for(REVERSE,degree,TURNS,wait=False) #0.96 spin will turn 90 degrees
def left(degree):
    degree = degree / 90 * 0.96
    right_motor.spin_for(FORWARD,degree,TURNS,wait=False)
    left_motor.spin_for(REVERSE,degree,TURNS,wait=False)


FrontSpindle.set_velocity(25,PERCENT)
conveyer.set_velocity(50,PERCENT) #works at 50%



controller_1.buttonR1.pressed(spindlestart)
controller_1.buttonR2.pressed(spindlestop)
controller_1.buttonL1.pressed(ClawUp)
controller_1.buttonL2.pressed(ClawDown)

# Main Controller loop to set motors to controller axis postiions
while True:

    ##MOTOR CONTROL
    right_motor.set_velocity((controller_1.axis3.position() - controller_1.axis4.position()), PERCENT)
    left_motor.set_velocity((controller_1.axis3.position() + controller_1.axis4.position()), PERCENT)
    conveyer.set_velocity((controller_1.axis2.position()*0.5),PERCENT)
    right_motor.spin(FORWARD)
    left_motor.spin(FORWARD)
    conveyer.spin(FORWARD)
    wait(5, MSEC)






