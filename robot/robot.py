import magicbot
import wpilib
import rev
from components.driveTrain import DriveTrain

class MyRobot(magicbot.MagicRobot):

    driveTrain: DriveTrain
    
    def createObjects(self):
        self.driverJoystick = wpilib.Joystick(0)

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

        #logitech extreme 3d. Case 10

        #get y axis - 1 (when moving joystick forward and backwards)
        wpilib.SmartDashboard.putNumber("joystick  Y value", self.driverJoystick.getY())
        #get x axis - 0 (when moving joystick sideways)
        wpilib.SmartDashboard.putNumber("joystick  X value", self.driverJoystick.getX())
        #get the rotational value - 2 (when twisting joystick) left: -1, right: 1
        wpilib.SmartDashboard.putNumber("joystick  Z value", self.driverJoystick.getZ())

        # wpilib.SmartDashboard.putNumber("joystick  radians value", self.driverJoystick.getDirectionRadians())
        # wpilib.SmartDashboard.putNumber("joystick  throttle", self.driverJoystick.getThrottle())
        # wpilib.SmartDashboard.putNumber("joystick  get top", self.driverJoystick.getTop())
        # wpilib.SmartDashboard.putNumber("joystick  trigger", self.driverJoystick.getTrigger())
        # wpilib.SmartDashboard.putNumber("joystick  get twist", self.driverJoystick.getTwist())

        # self.driveTrain.tank_drive(self.speed*leftJoystick, self.speed*rightJoystick)
        


if __name__ == '__main__':
    wpilib.run(MyRobot)



