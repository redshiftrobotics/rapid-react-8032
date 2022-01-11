import magicbot
import wpilib
import rev

class DriveTrain:

    def tank_drive(self, RightJoystickValue, LeftJoystickValue):
        RightMotorValue = RightJoystickValue
        LeftMotorValue = LeftJoystickValue