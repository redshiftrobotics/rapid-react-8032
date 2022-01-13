import magicbot
import wpilib
import rev
from components.driveTrain import DriveTrain

class MyRobot(magicbot.MagicRobot):

    drivetrain: DriveTrain
    
    def createObjects(self):
        self.driverJoystick = wpilib.Joystick(0)
        #we do not know why it has to be setZChannel. We also don't underdstand the 
        self.driverJoystick.setZChannel(5)

        self.frontLeftMotor = rev.CANSarkMax(0, rev.CANSparkMaxLowLevel.kBrushless)
        self.frontRightMotor = rev.CANSarkMax(1, rev.CANSparkMaxLowLevel.kBrushless)
        self.backLeftMotor = rev.CANSarkMax(2, rev.CANSparkMaxLowLevel.kBrushless)
        self.backRightMotor = rev.CANSarkMax(3, rev.CANSparkMaxLowLevel.kBrushless)
        


    def teleopInit(self):
        #zero speed
        #enable motor
        pass

    def teleopPeriodic(self):
        #get joystick
        #call tank drive
        pass



