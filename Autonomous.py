from vex import *

brain = Brain()

controller_1 = Controller(PRIMARY) ##This is the controller object so we can get input from the controls
conveyor = Motor(Ports.PORT13, GearSetting.RATIO_18_1, True)  #conveyor belt connect to port 1
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

def autonomous():
    ClawUp()
    right_motor1.set_velocity(60/3*1.05,PERCENT)
    left_motor1.set_velocity(60/3,PERCENT)
    right_motor2.set_velocity(60,PERCENT)
    left_motor2.set_velocity(60,PERCENT)
    FrontSpindle.set_velocity(40,PERCENT)
    conveyor.set_velocity(75,PERCENT) #works at 50%
    SpinConveyor()
    SpinSpindle()
    backward(10)
    right(90)
    backward(23.08)
    right(45)
    backward(33.64)
    ClawUp()
    foward(32.64)
    right(135)
    backward(70)
    ClawDown()
    backward(23.08)
    left(45)
    backward(33.64)
    ClawUp()
    foward(131)
    right(90)
    backward(33)
    ClawDown()
    left(45)
    backward(23.08*2)
    right(45)
    backward(33)
    ClawUp()
    right(135)
    backward(35)
    ClawDown()
    backward(93)
    left(45)
    backward(15)
    ClawUp()
