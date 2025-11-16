from vex import *

brain = Brain()

controller_1 = Controller(PRIMARY) ##This is the controller object so we can get input from the controls
Conveyor = Motor(Ports.PORT20, GearSetting.RATIO_18_1, True)  #Conveyor belt connect to port 1
right_motor_front = Motor(Ports.PORT19, GearSetting.RATIO_6_1, True) 
left_motor_front = Motor(Ports.PORT18, GearSetting.RATIO_6_1, False) #port 10 connect to the left, port 9 connect to the right
right_motor_rear = Motor(Ports.PORT17, GearSetting.RATIO_6_1, True) 
left_motor_rear = Motor(Ports.PORT16, GearSetting.RATIO_6_1, False) 
Spindle1 = Motor(Ports.PORT15, GearSetting.RATIO_6_1, True) 
push_motor1 = Pneumatics(brain.three_wire_port.g)
push_motor2 = Pneumatics(brain.three_wire_port.h)
motor_group_left = MotorGroup(left_motor_front,left_motor_rear)
motor_group_right = MotorGroup(right_motor_front,left_motor_front)
TestTrain = DriveTrain(motor_group_left,motor_group_right,220,375,295)
#input should be in inches, then will convert into turns
def foward(length):
    TestTrain.drive_for(FORWARD,length,INCHES)
def backward(length):
    TestTrain.drive_for(backward,length,INCHES)
def right(degree):
    TestTrain.turn_for(degree,DEGREES)
def left(degree):
    TestTrain.turn_for(degree,DEGREES)

# def CheckColour():
#     brain.screen.clear_screen()
    
#     if colour_sensor.is_near_object():
#         if colour_sensor.color() == Color.BLUE:
            
#             brain.screen.print("blue")
#         else:
            
#             brain.screen.print("red")

# def AUTONOMOUSCHECKCOLOUR():
#     brain.screen.clear_screen()
    
#     if colour_sensor.is_near_object():
#         if colour_sensor.color() == Color.BLUE:
#             right_motor_front.spin(FORWARD)
#             brain.screen.print("blue")
#         else:
#             left_motor_front.spin(FORWARD)
#             brain.screen.print("red")
        # Only detect colors if saturation is high enough
def MoveConveyor():
    if Conveyor.velocity() == 0:
        Conveyor.spin(FORWARD)
    else:
        Conveyor.stop()

def Push():
    if push_motor1.value() == 0:
        Open()
    else:
        Close()
        
    

    
def Open():
    push_motor1.open()
    push_motor2.close()

def Close():
    push_motor1.close()
    push_motor2.open()
                

def MoveSpindle():
    if Spindle1.velocity() == 0:
        Spindle1.spin(FORWARD)
        
    else:
        Spindle1.stop()
        

       
        

def autonomous(): #1 foward = 11 inches, 1 turn is around 53 degrees
    right_motor_front.set_velocity(45, PERCENT)
    left_motor_front.set_velocity(45, PERCENT)
    right_motor_rear.set_velocity(45, PERCENT)
    left_motor_rear.set_velocity(45, PERCENT)
    Conveyor.set_velocity(50,PERCENT)
    Spindle1.set_velocity(82,PERCENT)
    MoveSpindle()
    wait(1, SECONDS)
    foward(32)
    wait(1, SECONDS)
    Conveyor.spin_for(FORWARD,0.25,SECONDS)
    # backward(10.5)
    # wait(1, SECONDS)
    # left(25)
    # wait(1, SECONDS)
    #AUTONOMOUSCHECKCOLOUR()
    


def user_control():
    Conveyor.set_velocity(50,PERCENT)
    Spindle1.set_velocity(75,PERCENT)
    brain.screen.clear_screen()
    controller_1.buttonA.pressed(MoveSpindle)
    controller_1.buttonB.pressed(MoveConveyor)
    controller_1.buttonR1.pressed(Push)
    
    while True:

    #MOTOR CONTROL
        motor_group_left.set_velocity((controller_1.axis3.position() + controller_1.axis4.position()), PERCENT)
        motor_group_right.set_velocity((controller_1.axis3.position() - controller_1.axis4.position()), PERCENT)
        Conveyor.set_velocity(50, PERCENT)
        motor_group_left.spin(FORWARD)
        motor_group_right.spin(FORWARD)
        wait(5, MSEC)


# create competition instance
comp = Competition(user_control, autonomous)

# actions to do when the program starts
brain.screen.clear_screen()
