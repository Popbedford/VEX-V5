# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       DasgUPTAn                                                    #
# 	Created:      11/3/2025, 1:24:01 PM                                        #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
# Library imports
from vex import *
controller=Controller()
brain = Brain()
left_motor_front = Motor(Ports.PORT18,GearSetting.RATIO_18_1,False)
left_motor_rear = Motor(Ports.PORT17,GearSetting.RATIO_18_1,False)
right_motor_front = Motor(Ports.PORT20,GearSetting.RATIO_18_1,True)
right_motor_rear = Motor(Ports.PORT19,GearSetting.RATIO_18_1,True)
left_motors = MotorGroup(left_motor_front, left_motor_rear)
right_motors = MotorGroup(right_motor_front, right_motor_rear)

drivetrain = DriveTrain(left_motors, right_motors, 300, 320, 320, MM, 1)

def axis_changed():
    pass
def autonomous():
    brain.screen.clear_screen()
    brain.screen.print("autonomous code")
    

def user_control():
    brain.screen.clear_screen()
    brain.screen.print("driver control")
    # place driver control in this while loop
    while True:
        x=controller.axis2.position()
        drivetrain.set_drive_velocity(x, PERCENT)
        brain.screen.print(x)
        drivetrain.set_turn_velocity(controller.axis1.position(), PERCENT)
        

# create competition instance
comp = Competition(user_control, autonomous)

# actions to do when the program starts
brain.screen.print("hello")
#
controller.axis1.changed(axis_changed)
drivetrain.drive(FORWARD)
drivetrain.turn(RIGHT)
