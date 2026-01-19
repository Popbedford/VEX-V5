from vex import *

brain = Brain()
controller_1 = Controller(PRIMARY)

## Drive motors
right_motor_front = Motor(Ports.PORT19, GearSetting.RATIO_18_1, False)
left_motor_front = Motor(Ports.PORT11, GearSetting.RATIO_18_1, True)
right_motor_rear = Motor(Ports.PORT17, GearSetting.RATIO_18_1, False)
left_motor_rear = Motor(Ports.PORT14, GearSetting.RATIO_18_1, True)
left_motor_middle = Motor(Ports.PORT15, GearSetting.RATIO_18_1, True)
right_motor_middle = Motor(Ports.PORT18, GearSetting.RATIO_18_1, False)

## Spindles
Spindle1 = Motor(Ports.PORT13, False)
Spindle2 = Motor(Ports.PORT12, False)
Spindle3 = Motor(Ports.PORT1, False)
Spindle4 = Motor(Ports.PORT16, False)

## Pneumatics
push_motor1 = Pneumatics(brain.three_wire_port.e)
push_motor2 = Pneumatics(brain.three_wire_port.f)

## Motor groups & drivetrain
motor_group_left = MotorGroup(
    left_motor_front,
    left_motor_rear,
    left_motor_middle
)

motor_group_right = MotorGroup(
    right_motor_front,
    right_motor_middle,
    right_motor_rear
)

Drivetrain1 = DriveTrain(motor_group_left, motor_group_right)

# input should be in inches, then will convert into turns
def foward(length):
    
    right_motor_front.spin_for(FORWARD,length,TURNS,wait=False)  #one full turn will move 13.5 inches
    left_motor_front.spin_for(FORWARD,length,TURNS,wait=False)
    right_motor_middle.spin_for(FORWARD,length,TURNS,wait=False)
    left_motor_middle.spin_for(FORWARD,length,TURNS,wait=False)
    right_motor_rear.spin_for(FORWARD,length,TURNS,wait=False)  #one full turn will move 13.5 inches
    left_motor_rear.spin_for(FORWARD,length,TURNS,wait=True)
def backward(length):
    length = length / 13.5
    right_motor_front.spin_for(REVERSE,length,TURNS,wait=False)
    left_motor_front.spin_for(REVERSE,length,TURNS,wait=False)
    right_motor_middle.spin_for(REVERSE,length,TURNS,wait=False)
    left_motor_middle.spin_for(REVERSE,length,TURNS,wait=False)
    right_motor_rear.spin_for(REVERSE,length,TURNS,wait=False)
    left_motor_rear.spin_for(REVERSE,length,TURNS,wait=True)
def right(degree):
    
    left_motor_front.spin_for(FORWARD,degree,TURNS,wait=False) 
    right_motor_front.spin_for(REVERSE,degree,TURNS,wait=False) #0.96 spin will turn 90 degrees
    left_motor_rear.spin_for(FORWARD,degree,TURNS,wait=False) 
    right_motor_rear.spin_for(REVERSE,degree,TURNS,wait=True)
def left(degree):
    
    right_motor_front.spin_for(FORWARD,degree,TURNS,wait=False)
    left_motor_front.spin_for(REVERSE,degree,TURNS,wait=False)
    right_motor_rear.spin_for(FORWARD,degree,TURNS,wait=False)
    left_motor_rear.spin_for(REVERSE,degree,TURNS,wait=True)


def pnuematic():
    if push_motor1.value() == 0:  # 0 means closed
        push_motor1.open()
        push_motor2.open()

    elif push_motor1.value() == 1:  # 1 means opened
        push_motor1.close()
        push_motor2.close()

def MoveSpindleforward():
    if Spindle1.velocity() == 0 and Spindle2.velocity() == 0:
        Spindle2.set_velocity(100, PERCENT)
        Spindle1.set_velocity(100, PERCENT)
        Spindle3.set_velocity(100, PERCENT)
        Spindle4.set_velocity(100, PERCENT)

        Spindle1.spin(FORWARD)
        Spindle2.spin(FORWARD)
        Spindle3.spin(REVERSE)
        Spindle4.spin(FORWARD)

    else:
        Spindle1.stop()
        Spindle2.stop()
        Spindle3.stop()
        Spindle4.stop()

def MoveSpindleforward2():
    if Spindle1.velocity() == 0 and Spindle2.velocity() == 0:
        Spindle2.set_velocity(100, PERCENT)
        Spindle1.set_velocity(100, PERCENT)
        Spindle3.set_velocity(100, PERCENT)
        Spindle4.set_velocity(100, PERCENT)

        Spindle1.spin(REVERSE)
        Spindle2.spin(FORWARD)
        Spindle3.spin(REVERSE)
        Spindle4.spin(FORWARD)

    else:
        Spindle1.stop()
        Spindle2.stop()
        Spindle3.stop()
        Spindle4.stop()

def MoveSpindleforward3():
    if Spindle3.velocity() == 0 and Spindle2.velocity() == 0:
        Spindle1.set_velocity(100, PERCENT)
        Spindle2.set_velocity(100, PERCENT)
        Spindle3.set_velocity(100, PERCENT)
        Spindle4.set_velocity(100, PERCENT)

        Spindle1.stop()
        Spindle2.stop()
        Spindle3.spin(REVERSE)
        Spindle4.spin(FORWARD)

    else:
        Spindle1.stop()
        Spindle2.stop()
        Spindle3.stop()
        Spindle4.stop()

def MoveSpindlebackwards():
    if Spindle1.velocity() == 0 and Spindle2.velocity() == 0:
        Spindle2.set_velocity(100, PERCENT)
        Spindle1.set_velocity(100, PERCENT)
        Spindle3.set_velocity(100, PERCENT)
        Spindle4.set_velocity(100, PERCENT)

        Spindle1.spin(REVERSE)
        Spindle2.spin(REVERSE)
        Spindle3.spin(FORWARD)
        Spindle4.spin(REVERSE)

    else:
        Spindle1.stop()
        Spindle2.stop()
        Spindle3.stop()
        Spindle4.stop()

def MoveSpindlebackwards2():
    if Spindle1.velocity() == 0 and Spindle2.velocity() == 0:
        Spindle2.set_velocity(100, PERCENT)
        Spindle1.set_velocity(100, PERCENT)
        Spindle3.set_velocity(100, PERCENT)
        Spindle4.set_velocity(100, PERCENT)

        Spindle1.spin(FORWARD)
        Spindle2.spin(REVERSE)
        Spindle3.spin(FORWARD)
        Spindle4.spin(REVERSE)

    else:
        Spindle1.stop()
        Spindle2.stop()
        Spindle3.stop()
        Spindle4.stop()

# autonomous not working yet
def autonomous():
    foward(12.5)
    wait(500, MSEC)
    backward(12.5)
    wait(500, MSEC)
    right(5)
    backward(12.5)
    wait(500, MSEC)
    right(5)
    backward(2)
    wait(500, MSEC)
    MoveSpindle()

def user_control():
    push_motor1.close()
    push_motor2.close()

    brain.screen.clear_screen()

    controller_1.buttonA.pressed(MoveSpindleforward)
    controller_1.buttonX.pressed(MoveSpindleforward2)
    controller_1.buttonR1.pressed(pnuematic)
    controller_1.buttonB.pressed(MoveSpindlebackwards)
    controller_1.buttonY.pressed(MoveSpindlebackwards2)
    controller_1.buttonL1.pressed(MoveSpindleforward3)

    while True:

        # MOTOR CONTROL
        motor_group_left.set_velocity(
            controller_1.axis3.position(),
            PERCENT
        )
        motor_group_right.set_velocity(
            controller_1.axis2.position(),
            PERCENT
        )

        motor_group_left.spin(FORWARD)
        motor_group_right.spin(FORWARD)

        wait(5, MSEC)

# create competition instance
comp = Competition(user_control, autonomous)

# actions to do when the program starts
brain.screen.clear_screen()

autonomous()  # for testing
user_control()
