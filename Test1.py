from vex import *

brain = Brain()

controller_1 = Controller(PRIMARY) ##This is the controller object so we can get input from the controls
elevenwattmotor = Motor(Ports.PORT19, GearSetting.RATIO_18_1, True) 
fivewattmotor = Motor(Ports.PORT19, GearSetting.RATIO_18_1, True)

def foward(length):
    
def autonomous(): #1 foward = 11 inches, 1 turn is around 53 degrees
    pass
    


def user_control():
    brain.screen.clear_screen()
    while True:
        elevenwattmotor.set_velocity(controller_1,axis1)
        fivewattmotor.set_velocity(90, PERCENT)
    #MOTOR CONTROL
        
        elevenwattmotor.spin(FORWARD)
        fivewattmotor.spin(FORWARD)
        wait(5, MSEC)


# create competition instance
comp = Competition(user_control, autonomous)

# actions to do when the program starts
brain.screen.clear_screen()
