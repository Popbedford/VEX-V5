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
left_motor_front = Motor(Ports.PORT3,GearSetting.RATIO_18_1,False)
left_motor_rear = Motor(Ports.PORT8,GearSetting.RATIO_18_1,False)
right_motor_front = Motor(Ports.PORT7,GearSetting.RATIO_18_1,True)
right_motor_rear = Motor(Ports.PORT1,GearSetting.RATIO_18_1,True)
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
        #rubber
        if controller.buttonL2.pressing()==True:
            rubber_wheel_motor.set_velocity(-50, PERCENT)
        elif controller.buttonR2.pressing()==True:
            rubber_wheel_motor.set_velocity(100, PERCENT)
        else:
            rubber_wheel_motor.set_velocity(0, PERCENT)

comp = Competition(user_control, autonomous)

drivetrain.drive(REVERSE)
drivetrain.turn(LEFT)
conveyor.spin(FORWARD)
rubber_wheel_motor.spin(REVERSE)

controller.screen.print("I Am The Cadasio Conveyer Bot 2000 With The Low Taper Fade And The 67 Trim From Tescos")
controller.screen.new_line()
controller.screen.print("My Creators Were The Lesser Gene Baker, The Least Nik on the Hill Dasgupta, Morer So Ethan Lad And The MOST Ilyas Hosein And The Other Worldly Laith Shadid")
controller.screen.new_line()