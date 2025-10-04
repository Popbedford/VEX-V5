from vex import *

brain = Brain()

controller_1 = Controller(PRIMARY) ##This is the controller object so we can get input from the controls
conveyor = Motor(Ports.PORT1, GearSetting.RATIO_6_1, True)  #conveyor belt connect to port 1
spindle = Motor(Ports.PORT2, GearSetting.RATIO_6_1, True)
right_motor_front = Motor(Ports.PORT9, GearSetting.RATIO_6_1, True) 
left_motor_front = Motor(Ports.PORT10, GearSetting.RATIO_6_1, False) #port 10 connect to the left, port 9 connect to the right
right_motor_rear = Motor(Ports.PORT12, GearSetting.RATIO_6_1, True) 
left_motor_rear = Motor(Ports.PORT13, GearSetting.RATIO_6_1, False) 
Newmotor = Motor(Ports.PORT19, GearSetting.RATIO_6_1, True) 
push_motor = Pneumatics(brain.three_wire_port.a)
colour_sensor = Optical(Ports.PORT20)

def foward(length):
    
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
    
    left_motor_front.spin_for(FORWARD,degree,TURNS,wait=False) 
    right_motor_front.spin_for(REVERSE,degree,TURNS,wait=False) #0.96 spin will turn 90 degrees
    left_motor_rear.spin_for(FORWARD,degree,TURNS,wait=False) 
    right_motor_rear.spin_for(REVERSE,degree,TURNS,wait=True)
def left(degree):
    
    right_motor_front.spin_for(FORWARD,degree,TURNS,wait=False)
    left_motor_front.spin_for(REVERSE,degree,TURNS,wait=False)
    right_motor_rear.spin_for(FORWARD,degree,TURNS,wait=False)
    left_motor_rear.spin_for(REVERSE,degree,TURNS,wait=True)

def CheckColour():
    brain.screen.clear_screen()
    Newmotor.set_velocity(100, RPM)
    if colour_sensor.is_near_object():
        if colour_sensor.color() == Color.BLUE:
            Newmotor.spin(FORWARD)
            brain.screen.print("blue")
        else:
            Newmotor.spin(REVERSE)
            brain.screen.print("red")

def AUTONOMOUSCHECKCOLOUR():
    brain.screen.clear_screen()
    Newmotor.set_velocity(100, RPM)
    if colour_sensor.is_near_object():
        if colour_sensor.color() == Color.BLUE:
            right_motor_front.spin(FORWARD)
            brain.screen.print("blue")
        else:
            left_motor_front.spin(FORWARD)
            brain.screen.print("red")
        # Only detect colors if saturation is high enough
def MoveConveyor():
    if conveyor.velocity() == 0:
        conveyor.spin(FORWARD)
    else:
        conveyor.stop()
                

       
        

def autonomous(): #1 foward = 11 inches, 1 turn is around 53 degrees
    right_motor_front.set_velocity(67, PERCENT)
    left_motor_front.set_velocity(67, PERCENT)
    right_motor_rear.set_velocity(67, PERCENT)
    left_motor_rear.set_velocity(67, PERCENT)
    foward(45/11)
    left(1.3)
    AUTONOMOUSCHECKCOLOUR()
    


def user_control():
    brain.screen.clear_screen()
    controller_1.buttonA.pressed(CheckColour)
    

    while True:

    #MOTOR CONTROL
        right_motor_front.set_velocity((controller_1.axis3.position() - controller_1.axis4.position()), PERCENT)
        left_motor_front.set_velocity((controller_1.axis3.position() + controller_1.axis4.position()), PERCENT)
        right_motor_rear.set_velocity((controller_1.axis3.position() - controller_1.axis4.position()), PERCENT)
        left_motor_rear.set_velocity((controller_1.axis3.position() + controller_1.axis4.position()), PERCENT)
        right_motor_front.spin(FORWARD)
        left_motor_front.spin(FORWARD)
        right_motor_rear.spin(FORWARD)
        left_motor_rear.spin(FORWARD)
        
        
        
        wait(5, MSEC)


# create competition instance
comp = Competition(user_control, autonomous)

# actions to do when the program starts
brain.screen.clear_screen()
