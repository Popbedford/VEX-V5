def AutonForward(length):
    BotDriveTrain.set_drive_velocity(100,PERCENT)
    BotDriveTrain.drive_for(FORWARD,length,INCHES)

def AutonBackward(length):
    BotDriveTrain.set_drive_velocity(100,PERCENT)
    BotDriveTrain.drive_for(REVERSE,length,INCHES)

def AutonRight(degree):
    BotDriveTrain.set_drive_velocity(100,PERCENT)
    BotDriveTrain.turn_for(RIGHT,90,DEGREES)

def AutonLeft(degree):
    BotDriveTrain.set_drive_velocity(100,PERCENT)
    BotDriveTrain.turn_for(LEFT,90,DEGREES)

def MoveSpindleForward():
    if Spindle1.velocity() == 0:
        Spindles.set_velocity(100,PERCENT)
        Spindles.spin(FORWARD)
    else:
        Spindles.stop()
