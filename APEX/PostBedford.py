from vex import *

brain = Brain()
arm_velocity_switcher=1
controller_1 = Controller(PRIMARY) ##This is the controller object so we can get input from the controls
controller_2 = Controller()

right_motor_front = Motor(Ports.PORT17, GearSetting.RATIO_18_1, False)
#right_motor_middle = Motor(Ports.PORT4, GearSetting.RATIO_18_1, False)
right_motor_rear = Motor(Ports.PORT18, GearSetting.RATIO_18_1, False)
motor_group_right = MotorGroup(right_motor_front, right_motor_rear)

left_motor_front = Motor(Ports.PORT20, GearSetting.RATIO_18_1, True)
#left_motor_middle = Motor(Ports.PORT3, GearSetting.RATIO_18_1, True)
left_motor_rear = Motor(Ports.PORT19, GearSetting.RATIO_18_1, True)
motor_group_left = MotorGroup(left_motor_front, left_motor_rear)

strafe=Motor(Ports.PORT16)
arm = Motor(Ports.PORT12, GearSetting.RATIO_36_1)
claw=Motor(Ports.PORT11)
distance_sensor = Distance(Ports.PORT14)

def controlled_place():#
    #start of new section
    if distance_sensor.is_object_detected:
        distance_to_tower = distance_sensor.object_distance()
    else:
        distance_to_tower=48#correct distance
    correct_distance=48
    distance_per_rev=220
    diff=distance_to_tower-correct_distance
    #motor_group_left.spin_for(REVERSE, 360*(diff/distance_per_rev),DEGREES,100, wait=False)
    #motor_group_right.spin_for(REVERSE, 360*(diff/distance_per_rev), DEGREES,100, wait=True)
    #end of new section
    claw.set_velocity(-100)
    arm.set_velocity(25)
    arm.spin_for(FORWARD, 1000, MSEC, )
    claw.spin_for(FORWARD, 1000, MSEC, )
    wait(1000)
    claw.spin_for(FORWARD, 750, MSEC, 100)
def user_control():
    global arm_velocity_switcher
    while True:
    #MOTOR CONTROL
        # Single joystick control
        
        motor_group_left.set_velocity((controller_1.axis3.position() + (controller_1.axis1.position())), PERCENT)
        motor_group_right.set_velocity((controller_1.axis3.position() - (controller_1.axis1.position())), PERCENT)
        strafe.set_velocity(controller_1.axis4.position())
        #claw - arm
        if controller_1.buttonA.pressing():
            controlled_place()
        #claw - claw
        if controller_1.buttonL2.pressing():
            claw.set_velocity(100)
        elif controller_1.buttonR2.pressing():
            claw.set_velocity(-100)
        else:
            claw.set_velocity(0)
        if controller_1.buttonL1.pressing():
            arm.set_velocity(1)
            arm_velocity_switcher/=-1
            if controller_1.buttonL2.pressing()==False: claw.set_velocity(-100)
            #claw.spin_for(FORWARD, 2000, MSEC)
        elif controller_1.buttonR1.pressing():
            arm.set_velocity(-50)
            if controller_1.buttonL2.pressing()==False: 
                claw.set_velocity(-100)
                #claw.spin_for(FORWARD, 2000, MSEC)
        else: arm.set_velocity(0)
        arm.spin(FORWARD)
        claw.spin(FORWARD)
        strafe.spin(FORWARD)
        motor_group_right.spin(REVERSE)
        motor_group_left.spin(REVERSE)
        wait(5, MSEC)

def autonomous():
    #go forward 16-4.8
    controller_1.screen.print("running autonomous!")
    motor_group_left.spin_for(REVERSE, 360*((160-48)/220),DEGREES,100, wait=False)
    motor_group_right.spin_for(REVERSE, 360*((160-48)/220), DEGREES,100, wait=True)
    arm.spin_for(FORWARD, 2000, MSEC, -25)
    claw.set_velocity(-100)
    arm.set_velocity(25)
    arm.spin_for(FORWARD, 3000, MSEC, )
    claw.spin_for(FORWARD, 3000, MSEC, )
    wait(3000)
    claw.spin_for(FORWARD, 1000, MSEC, 100)

# create competition instance
comp = Competition(user_control,autonomous)
user_control()

# actions to do when the program starts
brain.screen.clear_screen()
