from vex import *

brain = Brain()

controller_1 = Controller(PRIMARY) ##This is the controller object so we can get input from the controls
conveyor = Motor(Ports.PORT1, GearSetting.RATIO_6_1, True)  #conveyor belt connect to port 1
right_motor1 = Motor(Ports.PORT9, GearSetting.RATIO_18_1, True) 
left_motor1 = Motor(Ports.PORT10, GearSetting.RATIO_18_1, False) #port 10 connect to the left, port 9 connect to the right
right_motor2 = Motor(Ports.PORT12, GearSetting.RATIO_6_1, True) 
left_motor2 = Motor(Ports.PORT13, GearSetting.RATIO_6_1, False)   
#swipe on 11, front black thingy on 13
claw = Pneumatics(brain.three_wire_port.a)
FrontSpindle = Motor(Ports.PORT2, GearSetting.RATIO_18_1, False)

claw.set(False)

def conveyorstart():
    conveyor.spin(FORWARD)
def conveyorreverse():
    conveyor.spin(REVERSE)
def conveyorstop():
    conveyor.stop()
def spindlestart():
    FrontSpindle.spin(FORWARD)
def spindlestop():
    FrontSpindle.stop()


def ClawUp():
    claw.set(False)
def ClawDown():
    claw.set(True)
    



def forward(length):
    length = length / 13.5
    right_motor1.spin_for(FORWARD,length,TURNS,wait=False)  #one full turn will move 13.5 inches
    left_motor1.spin_for(FORWARD,length,TURNS,wait=False)
    right_motor2.spin_for(FORWARD,length,TURNS,wait=False)  #one full turn will move 13.5 inches
    left_motor2.spin_for(FORWARD,length,TURNS,wait=False)
def backward(length):
    length = length / 13.5
    right_motor1.spin_for(REVERSE,length,TURNS,wait=False)
    left_motor1.spin_for(REVERSE,length,TURNS,wait=False)
    right_motor2.spin_for(REVERSE,length,TURNS,wait=False)
    left_motor2.spin_for(REVERSE,length,TURNS,wait=False)
def right(degree):
    degree = degree / 90 * 0.96
    left_motor1.spin_for(FORWARD,degree,TURNS,wait=False) 
    right_motor1.spin_for(REVERSE,degree,TURNS,wait=False) #0.96 spin will turn 90 degrees
    left_motor2.spin_for(FORWARD,degree,TURNS,wait=False) 
    right_motor2.spin_for(REVERSE,degree,TURNS,wait=False)
def left(degree):
    degree = degree / 90 * 0.96
    right_motor1.spin_for(FORWARD,degree,TURNS,wait=False)
    left_motor1.spin_for(REVERSE,degree,TURNS,wait=False)
    right_motor2.spin_for(FORWARD,degree,TURNS,wait=False)
    left_motor2.spin_for(REVERSE,degree,TURNS,wait=False)

def autonomous():
    right_motor1.set_velocity(65,PERCENT)
    left_motor1.set_velocity(65,PERCENT)
    right_motor2.set_velocity(90,PERCENT)
    left_motor2.set_velocity(90,PERCENT)
    FrontSpindle.set_velocity(25,PERCENT)
    conveyor.set_velocity(50,PERCENT) #works at 50%
    conveyor.spin(FORWARD)
    FrontSpindle.spin(FORWARD)
    backward(58.42)
    left(135)
    forward(17)
    ClawDown()
    wait(3, SECONDS)
    left(90)
    backward(25)
    FrontSpindle.spin(FORWARD)
    conveyorstart()







# Main Controller loop to set motors to controller axis postiions
while True:
    ##MOTOR CONTROL
    FrontSpindle.spin(FORWARD)
    conveyor.spin(FORWARD)
    wait(5, MSEC)
