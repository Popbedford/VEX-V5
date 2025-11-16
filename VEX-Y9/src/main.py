# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       DasgUPTAn                                                    #
# 	Created:      11/3/2025, 1:24:01 PM                                        #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *
controller=Controller()
brain = Brain()
left_motor_front = Motor(Ports.PORT18,GearSetting.RATIO_18_1,True)
left_motor_rear = Motor(Ports.PORT17,GearSetting.RATIO_18_1,True)
right_motor_front = Motor(Ports.PORT20,GearSetting.RATIO_18_1,False)
right_motor_rear = Motor(Ports.PORT19,GearSetting.RATIO_18_1,False)
left_motors = MotorGroup(left_motor_front, left_motor_rear)
right_motors = MotorGroup(right_motor_front, right_motor_rear)

conveyor=Motor(Ports.PORT15,GearSetting.RATIO_6_1)

drivetrain = DriveTrain(left_motors, right_motors, 300, 320, 320, MM, 1)

def turn_motor_f():
    pass

def turn_motor_b():
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

        #conveyor

        if controller.buttonL1.pressing()==True:
            conveyor.set_velocity(-50, PERCENT)
        elif controller.buttonR1.pressing()==True:
            conveyor.set_velocity(50, PERCENT)
        else:
            conveyor.set_velocity(0, PERCENT)
        

# create competition instance aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
comp = Competition(user_control, autonomous)

# actions to do when the program starts
brain.screen.print("hello")
#

drivetrain.drive(FORWARD)
drivetrain.turn(RIGHT)
conveyor.spin(FORWARD)
        
