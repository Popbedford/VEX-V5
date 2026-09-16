# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       Popdham                                                      #
# 	Created:      9/16/2026, 1:21:08 PM                                        #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

brain = Brain()

controller_1 = Controller(PRIMARY) ##This is the controller object so we can get input from the controls
elevenwattmotor = Motor(Ports.PORT19, GearSetting.RATIO_18_1, True) 
fivewattmotor = Motor(Ports.PORT19, GearSetting.RATIO_18_1, True)


def autonomous(): #1 foward = 11 inches, 1 turn is around 53 degrees
    pass
    


def user_control():
    brain.screen.clear_screen()
    while True:
        elevenwattmotor.set_velocity(controller_1.axis3.position()-controller_1.axis4.position())
        fivewattmotor.set_velocity(controller_1.axis1.position()-controller_1.axis2.position())
    #MOTOR CONTROL
        
        elevenwattmotor.spin(FORWARD)
        fivewattmotor.spin(FORWARD)
        wait(5, MSEC)


# create competition instance
comp = Competition(user_control, autonomous)

# actions to do when the program starts
brain.screen.clear_screen()
