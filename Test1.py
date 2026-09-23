# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       Popdham                                                      #
# 	Created:      9/23/2026, 6:19:38 PM                                        #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

brain = Brain()

controller_1 = Controller(PRIMARY) ##This is the controller object so we can get input from the controls
Conveyor = Motor(Ports.PORT20, GearSetting.RATIO_18_1, True)  #Conveyor belt connect to port 1
right_motor_front = Motor(Ports.PORT19, GearSetting.RATIO_18_1, True) 
left_motor_front = Motor(Ports.PORT18, GearSetting.RATIO_18_1, False) #port 10 connect to the left, port 9 connect to the right
right_motor_rear = Motor(Ports.PORT17, GearSetting.RATIO_18_1, True) 
left_motor_rear = Motor(Ports.PORT16, GearSetting.RATIO_18_1, False) 
right_motor_middle = Motor(Ports.PORT15, GearSetting.RATIO_18_1, False) 
left_motor_middle = Motor(Ports.PORT14, GearSetting.RATIO_18_1, False) 
rmg = MotorGroup(right_motor_front, right_motor_middle, right_motor_rear)
lmg = MotorGroup(left_motor_front, left_motor_middle, left_motor_rear)
Autodrive = DriveTrain(rmg, lmg, 219.440247, 380, 385, units=MM, externalGearRatio=1.0)
#input should be in inches, then will convert into turns
def foward(length):
    Autodrive.drive_for(FORWARD, length, INCHES)
    
def backward(length):
    Autodrive.drive_for(FORWARD, length, INCHES)

def right(degree):
    Autodrive.turn(RIGHT, degree, VelocityUnits.DPS)

def left(degree):
    Autodrive.turn(LEFT, degree, VelocityUnits.DPS)

def autonomous(): #1 foward = 11 inches, 1 turn is around 53 degrees
    pass
    


def user_control():
    brain.screen.clear_screen()

    while True:

    #MOTOR CONTROL
        rmg.set_velocity(controller_1.axis3.position(), PERCENT)
        lmg.set_velocity(controller_1.axis4.position(), PERCENT)
        rmg.spin(FORWARD)
        lmg.spin(FORWARD)
        wait(5, MSEC)


# create competition instance
comp = Competition(user_control, autonomous)

# actions to do when the program starts
brain.screen.clear_screen()
