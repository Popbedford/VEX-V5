from vex import *

brain = Brain()
global Left
Left = True
global Turn
Turn=2
global Mode
Mode=True
controller_1 = Controller(PRIMARY) ##This is the controller object so we can get input from the controls
right_motor_front = Motor(Ports.PORT20, GearSetting.RATIO_18_1, False)
left_motor_front = Motor(Ports.PORT11, GearSetting.RATIO_18_1, True)
right_motor_rear = Motor(Ports.PORT18, GearSetting.RATIO_18_1, False)
left_motor_rear = Motor(Ports.PORT13, GearSetting.RATIO_18_1, True)
left_motor_middle = Motor(Ports.PORT12, GearSetting.RATIO_18_1, True)
right_motor_middle = Motor(Ports.PORT19, GearSetting.RATIO_18_1, False)
Spindle1 = Motor(Ports.PORT14, GearSetting.RATIO_18_1, True)
Spindle2 = Motor(Ports.PORT15, GearSetting.RATIO_18_1, True)
Spindle3 = Motor(Ports.PORT16, GearSetting.RATIO_18_1, False)
Spindle4 = Motor(Ports.PORT17, GearSetting.RATIO_18_1, False)
push_motor1 = Pneumatics(brain.three_wire_port.a)
push_motor2 = Pneumatics(brain.three_wire_port.b)
motor_group_left = MotorGroup(left_motor_front, left_motor_middle, left_motor_rear)
motor_group_right = MotorGroup(right_motor_front, right_motor_middle, right_motor_rear)
TestTrain = DriveTrain(motor_group_left,motor_group_right,190,375,230,MM)#220,375,295
TestTrain.set_drive_velocity(100,PERCENT)
TestTrain.set_turn_velocity(100,PERCENT)
#input should be in inches, then will convert into turns

def foward(length):
   
    right_motor_front.spin_for(FORWARD,length,TURNS,wait=False)  #one full turn will move 13.5 inches
    left_motor_front.spin_for(FORWARD,length,TURNS,wait=False)
    right_motor_middle.spin_for(FORWARD,length,TURNS,wait=False)
    left_motor_middle.spin_for(FORWARD,length,TURNS,wait=False)
    right_motor_rear.spin_for(FORWARD,length,TURNS,wait=False)  #one full turn will move 13.5 inches
    left_motor_rear.spin_for(FORWARD,length,TURNS,wait=True)
def backward(length):
   
    right_motor_front.spin_for(REVERSE,length,TURNS,wait=False)
    left_motor_front.spin_for(REVERSE,length,TURNS,wait=False)
    right_motor_middle.spin_for(REVERSE,length,TURNS,wait=False)
    left_motor_middle.spin_for(REVERSE,length,TURNS,wait=False)
    right_motor_rear.spin_for(REVERSE,length,TURNS,wait=False)
    left_motor_rear.spin_for(REVERSE,length,TURNS,wait=True)
def right(degree):
   
    left_motor_front.spin_for(FORWARD,degree,TURNS,wait=False)
    right_motor_front.spin_for(REVERSE,degree,TURNS,wait=False) #0.96 spin will turn 90 degrees
    right_motor_middle.spin_for(REVERSE,degree,TURNS,wait=False)
    left_motor_middle.spin_for(FORWARD,degree,TURNS,wait=False)
    left_motor_rear.spin_for(FORWARD,degree,TURNS,wait=False)
    right_motor_rear.spin_for(REVERSE,degree,TURNS,wait=True)
def left(degree):
   
    right_motor_front.spin_for(FORWARD,degree,TURNS,wait=False)
    left_motor_front.spin_for(REVERSE,degree,TURNS,wait=False)
    right_motor_middle.spin_for(FORWARD,degree,TURNS,wait=False)
    left_motor_middle.spin_for(REVERSE,degree,TURNS,wait=False)
    right_motor_rear.spin_for(FORWARD,degree,TURNS,wait=False)
    left_motor_rear.spin_for(REVERSE,degree,TURNS,wait=True)


def aforward(length):
    TestTrain.drive_for(FORWARD,length,INCHES)
    #wait(2,SECONDS)

def abackward(length):
    TestTrain.drive_for(REVERSE,length,INCHES)

def aright(d):
    TestTrain.turn_for(d,DEGREES)

def aleft(d):
    TestTrain.turn_for(d,DEGREES)

def pnuematic():
    if push_motor1.value() == 0:# 0 means closed
        push_motor1.open()
        push_motor2.open()
   
    elif push_motor1.value() == 1:# 1 means opened
        push_motor1.close()
        push_motor2.close()

def MoveSpindleforward():
    if Spindle1.velocity() == 0 or Spindle2.velocity() == 0 or Spindle3.velocity() == 0 or Spindle4.velocity() == 0:
        Spindle1.set_velocity(100,PERCENT)
        Spindle2.set_velocity(100,PERCENT)
        Spindle3.set_velocity(100,PERCENT)
        Spindle4.set_velocity(201,RPM)
        Spindle1.spin(FORWARD)
        Spindle2.spin(FORWARD)
        Spindle3.spin(FORWARD)
        Spindle4.spin(FORWARD)
       
    else:
        Spindle1.stop()
        Spindle2.stop()
        Spindle3.stop()
        Spindle4.stop()

def MoveSpindlebackwards():
    if Spindle1.velocity() == 0 or Spindle2.velocity() == 0 or Spindle3.velocity() == 0 or Spindle4.velocity() == 0:
        Spindle1.set_velocity(100,PERCENT)
        Spindle2.set_velocity(100,PERCENT)
        Spindle3.set_velocity(100,PERCENT)
        Spindle4.set_velocity(201,RPM)
        Spindle1.spin(REVERSE)
        Spindle2.spin(REVERSE)
        Spindle3.spin(REVERSE)
        Spindle4.spin(REVERSE)
       
    else:
        Spindle1.stop()
        Spindle2.stop()
        Spindle3.stop()
        Spindle4.stop()

def spindle_pickup_only():
    if Spindle1.velocity() == 0 or Spindle2.velocity() == 0:
        Spindle2.set_velocity(100,PERCENT)
        Spindle1.set_velocity(100,PERCENT)
        Spindle1.spin(FORWARD)
        Spindle2.spin(FORWARD)
        Spindle3.stop()
        Spindle4.stop()
       
    else:
        Spindle1.stop()
        Spindle2.stop()
        Spindle3.stop()
        Spindle4.stop()

def Middle_goal_score():
    if Spindle1.velocity() == 0 and Spindle2.velocity() == 0 and Spindle3.velocity() == 0 and Spindle4.velocity() == 0:
        Spindle1.set_velocity(100,PERCENT)
        Spindle2.set_velocity(100,PERCENT)
        Spindle3.set_velocity(100,PERCENT)
        Spindle4.set_velocity(201,RPM)
        Spindle1.spin(FORWARD)
        Spindle2.spin(FORWARD)
        Spindle3.spin(FORWARD)
        Spindle4.spin(REVERSE)
       
    else:
        Spindle1.stop()
        Spindle2.stop()
        Spindle3.stop()
        Spindle4.stop()

def TurnUpN():
    global Turn
    Turn+=1
   
def TurnDownN():
    global Turn
    if Turn>1:
        Turn-=1

def SwitchMode():
    global Mode
    if Mode==True:
        Mode=False
    else:
        Mode=True

def pre_autonomous():
    push_motor1.open()
    push_motor2.open()
   
    pass

def TurnSide(Direction, degree): # Direction is "R" or "L", and assumes you are on the right side.
    if (not Left):
        if Direction == "R":
            right(degree)
        else:
            left(degree)
    else:
        if Direction == "R":
            left(degree)
        else:
            right(degree)

def autonomousOld():
    # right_motor_front.set_velocity(67, PERCENT)
    # left_motor_front.set_velocity(67, PERCENT)
    # right_motor_rear.set_velocity(67, PERCENT)
    # left_motor_rear.set_velocity(67, PERCENT)
    # left_motor_middle.set_velocity(67, PERCENT)
    # right_motor_middle.set_velocity(67, PERCENT)
    # mvsqr = 1.56
    # r_angle = 0.85
    # foward(1.5*mvsqr)
    # wait(500,MSEC)
    # left(r_angle)
    # wait(500,MSEC)
    # foward(mvsqr)
    # wait(500,MSEC)
    # spindle_pickup_only()
    # backward(mvsqr*2)
    # wait(500,MSEC)
    # MoveSpindleforward()
    if (not Left):
        right_motor_front.set_velocity(67, PERCENT)
        left_motor_front.set_velocity(67, PERCENT)
        right_motor_rear.set_velocity(67, PERCENT)
        left_motor_rear.set_velocity(67, PERCENT)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
        left_motor_middle.set_velocity(67, PERCENT)
        right_motor_middle.set_velocity(67, PERCENT)
        mvsqr = 1.56
        r_angle = 0.83
        pnuematic()
        foward(1.5*mvsqr)
        wait(500,MSEC)
        right(r_angle)
        wait(500,MSEC)
        foward(mvsqr)
        wait(500,MSEC)
        spindle_pickup_only()
        wait(3, SECONDS)
        backward(mvsqr*2.167)
        wait(500,MSEC)
        MoveSpindleforward()
    else:
        right_motor_front.set_velocity(67, PERCENT)
        left_motor_front.set_velocity(67, PERCENT)
        right_motor_rear.set_velocity(67, PERCENT)
        left_motor_rear.set_velocity(67, PERCENT)
        left_motor_middle.set_velocity(67, PERCENT)
        right_motor_middle.set_velocity(67, PERCENT)
        mvsqr = 1.56
        r_angle = 0.85
        foward(1.55*mvsqr)
        wait(500,MSEC)
        left(r_angle)
        wait(500,MSEC)
        foward(mvsqr)
        wait(500,MSEC)
        spindle_pickup_only()
        backward(mvsqr*2)
        wait(500,MSEC)
        MoveSpindleforward()

def autonomous():
   
    right_motor_front.set_velocity(67, PERCENT)
    left_motor_front.set_velocity(67, PERCENT)
    right_motor_rear.set_velocity(67, PERCENT)
    left_motor_rear.set_velocity(67, PERCENT)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
    left_motor_middle.set_velocity(67, PERCENT)
    right_motor_middle.set_velocity(67, PERCENT)
    mvsqr = 1.56
    r_angle = 0.83
    pnuematic()
    foward(1.55*mvsqr)
    wait(500,MSEC)
    TurnSide("R",r_angle)
    wait(500,MSEC)
    foward(0.95*mvsqr)
    wait(500,MSEC)
    spindle_pickup_only()
    wait(3, SECONDS)
    backward(mvsqr*2.167)
    wait(500,MSEC)
    MoveSpindleforward()
   
def autonomous_skills():
    pnuematic()
    MoveSpindleforward()
    foward(1.56)
    wait(90, SECONDS)
    pass

def user_control():

   
    brain.screen.clear_screen()
    controller_1.buttonA.pressed(MoveSpindleforward)
    controller_1.buttonB.pressed(MoveSpindlebackwards)
    controller_1.buttonX.pressed(Middle_goal_score)
    controller_1.buttonR1.pressed(pnuematic)
    controller_1.buttonL1.pressed(spindle_pickup_only)
    controller_1.buttonUp.pressed(TurnDownN)
    controller_1.buttonDown.pressed(TurnUpN)
    controller_1.buttonRight.pressed(SwitchMode)
   
    while True:

    #MOTOR CONTROL
        if Mode==True:
            motor_group_left.set_velocity((controller_1.axis3.position() + (controller_1.axis4.position()/Turn)), PERCENT)
            motor_group_right.set_velocity((controller_1.axis3.position() - (controller_1.axis4.position()/Turn)), PERCENT)
        else:
            motor_group_left.set_velocity(controller_1.axis3.position(), PERCENT)
            motor_group_right.set_velocity(controller_1.axis2.position(), PERCENT)
       
        motor_group_left.spin(FORWARD)
        motor_group_right.spin(FORWARD)

        wait(5, MSEC)


# create competition instance


# actions to do when the program starts
brain.screen.clear_screen()
comp = Competition(user_control, autonomous)
pre_autonomous()
