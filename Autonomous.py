from vex import *

brain = Brain()

controller_1 = Controller(PRIMARY) ##This is the controller object so we can get input from the controls
conveyor = Motor(Ports.PORT13, GearSetting.RATIO_6_1, True)  #conveyor belt connect to port 1
right_motor1 = Motor(Ports.PORT9, GearSetting.RATIO_6_1, True) 
left_motor1 = Motor(Ports.PORT10, GearSetting.RATIO_6_1, False) #port 10 connect to the left, port 9 connect to the right
right_motor2 = Motor(Ports.PORT12, GearSetting.RATIO_18_1, True) 
left_motor2 = Motor(Ports.PORT20, GearSetting.RATIO_18_1, False) 
claw = Pneumatics(brain.three_wire_port.a)
FrontSpindle = Motor(Ports.PORT2, GearSetting.RATIO_6_1, False)
claw.close()
def ClawUp():
    claw.close()
def ClawDown():
    claw.open()
def MoveClaw():
    if claw.value() == 0:
        claw.open()
    else:
        claw.close()
def MoveSpindle():
    if FrontSpindle.velocity() == 0:
        FrontSpindle.spin(FORWARD)
    else:
        FrontSpindle.stop()
def SpinSpindle():
    FrontSpindle.spin(FORWARD)
def StopSpindle():
    FrontSpindle.stop()
def SpinConveyor():
    conveyor.spin(FORWARD)
def StopConveyor():
    conveyor.stop()
def foward(length):
    length = length / 13.5

    right_motor1.spin_for(FORWARD,length,TURNS,wait=False)  #one full turn will move 13.5 inches
    left_motor1.spin_for(FORWARD,length,TURNS,wait=False)
    right_motor2.spin_for(FORWARD,length,TURNS,wait=False)  #one full turn will move 13.5 inches
    left_motor2.spin_for(FORWARD,length,TURNS,wait=True)
def backward(length):
    length = length / 13.5
    right_motor1.spin_for(REVERSE,length,TURNS,wait=False)
    left_motor1.spin_for(REVERSE,length,TURNS,wait=False)
    right_motor2.spin_for(REVERSE,length,TURNS,wait=False)
    left_motor2.spin_for(REVERSE,length,TURNS,wait=True)
def right(degree):
    degree = degree / 90 * 0.96
    left_motor1.spin_for(FORWARD,degree,TURNS,wait=False) 
    right_motor1.spin_for(REVERSE,degree,TURNS,wait=False) #0.96 spin will turn 90 degrees
    left_motor2.spin_for(FORWARD,degree,TURNS,wait=False) 
    right_motor2.spin_for(REVERSE,degree,TURNS,wait=True)
def left(degree):
    degree = degree / 90 * 0.96
    right_motor1.spin_for(FORWARD,degree,TURNS,wait=False)
    left_motor1.spin_for(REVERSE,degree,TURNS,wait=False)
    right_motor2.spin_for(FORWARD,degree,TURNS,wait=False)
    left_motor2.spin_for(REVERSE,degree,TURNS,wait=True)

right_motor1.set_velocity(45/3*1.05,PERCENT)
left_motor1.set_velocity(45/3,PERCENT)
right_motor2.set_velocity(45*1.05,PERCENT)
left_motor2.set_velocity(45,PERCENT)
FrontSpindle.set_velocity(40,PERCENT)
conveyor.set_velocity(50,PERCENT) #works at 50%
backward(33)
ClawDown()
SpinConveyor()
SpinSpindle()
right(105)
foward(23)


# def user_control():
#     FrontSpindle.set_velocity(100,PERCENT)
    
#     controller_1.buttonR1.pressed(MoveSpindle)
#     controller_1.buttonL1.pressed(MoveClaw)
    
#     while True:

#     #MOTOR CONTROL
#         right_motor1.set_velocity((controller_1.axis3.position() - controller_1.axis4.position())/3*1.05, PERCENT)
#         left_motor1.set_velocity((controller_1.axis3.position() + controller_1.axis4.position())/3, PERCENT)
#         right_motor2.set_velocity((controller_1.axis3.position() - controller_1.axis4.position())*1.05, PERCENT)
#         left_motor2.set_velocity((controller_1.axis3.position() + controller_1.axis4.position()), PERCENT)
#         conveyor.set_velocity((controller_1.axis2.position())*0.65,PERCENT)
#         right_motor1.spin(FORWARD)
#         left_motor1.spin(FORWARD)
#         right_motor2.spin(FORWARD)
#         left_motor2.spin(FORWARD)
#         conveyor.spin(FORWARD)

#         wait(5, MSEC)


# # create competition instance
# comp = Competition(user_control, autonomous)

# # actions to do when the program starts
# brain.screen.clear_screen()
