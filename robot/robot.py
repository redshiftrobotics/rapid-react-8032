import magicbot
import wpilib
import rev
from components.driveTrain import DriveTrain

class MyRobot(magicbot.MagicRobot):

    driveTrain: DriveTrain
    
    def createObjects(self):
        self.driverJoystick = wpilib.Joystick(0)
        #we do not know why it has to be setZChannel. We also don't underdstand the 5. 
        self.driverJoystick.setZChannel(5)

        self.frontLeftMotor = rev.CANSarkMax(0, rev.CANSparkMaxLowLevel.kBrushless)
        self.frontRightMotor = rev.CANSarkMax(1, rev.CANSparkMaxLowLevel.kBrushless)
        self.backLeftMotor = rev.CANSarkMax(2, rev.CANSparkMaxLowLevel.kBrushless)
        self.backRightMotor = rev.CANSarkMax(3, rev.CANSparkMaxLowLevel.kBrushless)

    def teleopInit(self):
        self.speed = 0.2

    def teleopPeriodic(self):
        #get joystick data
        #call tank drive
        self.driveTrain.enabled()
        leftJoystick = self.driverJoystick.getY()
        rightJoystick = self.driverJoystick.getZ()

        self.driveTrain.tank_drive(self.speed*leftJoystick, self.speed*rightJoystick)


if __name__ == '__main__':
    wpilib.run(MyRobot)



