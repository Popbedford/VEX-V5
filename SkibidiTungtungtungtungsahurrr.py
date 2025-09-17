from vex import *

brain = Brain()

controller_1 = Controller(PRIMARY) ##This is the controller object so we can get input from the controls
conveyor = Motor(Ports.PORT13, GearSetting.RATIO_6_1, True)  #conveyor belt connect to port 1
right_motor_front = Motor(Ports.PORT9, GearSetting.RATIO_6_1, True) 
left_motor_front = Motor(Ports.PORT10, GearSetting.RATIO_6_1, False) #port 10 connect to the left, port 9 connect to the right
right_motor_rear = Motor(Ports.PORT12, GearSetting.RATIO_6_1, True) 
left_motor_rear = Motor(Ports.PORT20, GearSetting.RATIO_6_1, False) 
push_motor = Pneumatics(brain.three_wire_port.a)
FrontSpindle = Motor(Ports.PORT2, GearSetting.RATIO_6_1, False)


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

    right_motor_front.spin_for(FORWARD,length,TURNS,wait=False)  #one full turn will move 13.5 inches
    left_motor_front.spin_for(FORWARD,length,TURNS,wait=False)
    right_motor_rear.spin_for(FORWARD,length,TURNS,wait=False)  #one full turn will move 13.5 inches
    left_motor_rear.spin_for(FORWARD,length,TURNS,wait=True)
def backward(length):
    length = length / 13.5
    right_motor_front.spin_for(REVERSE,length,TURNS,wait=False)
    left_motor_front.spin_for(REVERSE,length,TURNS,wait=False)
    right_motor_rear.spin_for(REVERSE,length,TURNS,wait=False)
    left_motor_rear.spin_for(REVERSE,length,TURNS,wait=True)
def right(degree):
    degree = degree / 90 * 0.96
    left_motor_front.spin_for(FORWARD,degree,TURNS,wait=False) 
    right_motor_front.spin_for(REVERSE,degree,TURNS,wait=False) #0.96 spin will turn 90 degrees
    left_motor_rear.spin_for(FORWARD,degree,TURNS,wait=False) 
    right_motor_rear.spin_for(REVERSE,degree,TURNS,wait=True)
def left(degree):
    degree = degree / 90 * 0.96
    right_motor_front.spin_for(FORWARD,degree,TURNS,wait=False)
    left_motor_front.spin_for(REVERSE,degree,TURNS,wait=False)
    right_motor_rear.spin_for(FORWARD,degree,TURNS,wait=False)
    left_motor_rear.spin_for(REVERSE,degree,TURNS,wait=True)

def autonomous():
    right_motor_front.set_velocity(55/3,PERCENT)
    left_motor_front.set_velocity(55/3,PERCENT)
    right_motor_rear.set_velocity(55,PERCENT)
    left_motor_rear.set_velocity(55,PERCENT)
    FrontSpindle.set_velocity(50,PERCENT)
    conveyor.set_velocity(80,PERCENT) #works at 5 H0%
    backward(40)
    ClawDown()
    SpinConveyor()
    SpinSpindle()
    right(90)
    foward(46)


def user_control():
    FrontSpindle.set_velocity(100,PERCENT)
    
    controller_1.buttonR1.pressed(MoveSpindle)
    controller_1.buttonL1.pressed(MoveClaw)
    
    while True:

    #MOTOR CONTROL
        right_motor1.set_velocity((controller_1.axis3.position() - controller_1.axis4.position())/3, PERCENT)
        left_motor1.set_velocity((controller_1.axis3.position() + controller_1.axis4.position())/3, PERCENT)
        right_motor2.set_velocity((controller_1.axis3.position() - controller_1.axis4.position()), PERCENT)
        left_motor2.set_velocity((controller_1.axis3.position() + controller_1.axis4.position()), PERCENT)
        conveyor.set_velocity((controller_1.axis2.position()),PERCENT)
        right_motor1.spin(FORWARD)
        left_motor1.spin(FORWARD)
        right_motor2.spin(FORWARD)
        left_motor2.spin(FORWARD)
        conveyor.spin(FORWARD)

        wait(5, MSEC)


# create competition instance
comp = Competition(user_control, autonomous)

# actions to do when the program starts
brain.screen.clear_screen()
