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
left_motor_front = Motor(Ports.PORT3,GearSetting.RATIO_18_1,True)
left_motor_rear = Motor(Ports.PORT8,GearSetting.RATIO_18_1,False)
right_motor_front = Motor(Ports.PORT1,GearSetting.RATIO_18_1,False)
right_motor_rear = Motor(Ports.PORT6,GearSetting.RATIO_18_1,True)
left_motors = MotorGroup(left_motor_front, left_motor_rear)
right_motors = MotorGroup(right_motor_front, right_motor_rear)

conveyor=Motor(Ports.PORT9,GearSetting.RATIO_6_1)
rubber_wheel_motor=Motor(Ports.PORT2, GearSetting.RATIO_18_1)

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
        x=controller.axis1.position()
        drivetrain.set_drive_velocity(x, PERCENT)
        brain.screen.print(x)
        drivetrain.set_turn_velocity(controller.axis2.position(), PERCENT)

        #conveyor

        if controller.buttonL1.pressing()==True:
            conveyor.set_velocity(-50, PERCENT)
        elif controller.buttonR1.pressing()==True:
            conveyor.set_velocity(50, PERCENT)
        else:
            conveyor.set_velocity(0, PERCENT)
        #rubber
        if controller.buttonL2.pressing()==True:
            rubber_wheel_motor.set_velocity(-50, PERCENT)
        elif controller.buttonR2.pressing()==True:
            rubber_wheel_motor.set_velocity(50, PERCENT)
        else:
            rubber_wheel_motor.set_velocity(0, PERCENT)

# create competition instance aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
comp = Competition(user_control, autonomous)

# actions to do when the program starts
brain.screen.print("hello")
#

drivetrain.drive(FORWARD)
drivetrain.turn(RIGHT)
conveyor.spin(FORWARD)
rubber_wheel_motor.spin(REVERSE)

controller.screen.print("I Am The Cadasio Conveyer Bot 2000 With The Low Taper Fade Amd the 67 Trim Fro Tescos")
controller.screen.new_line()
controller.screen.print("My Creators Were Gene Baker, Nikhil Dasgupta And Lesser So Ilyas Hosein")

        
