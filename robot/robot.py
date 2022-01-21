import magicbot
import wpilib
import rev
from components.driveTrain import DriveTrain

class MyRobot(magicbot.MagicRobot):

    driveTrain: DriveTrain
    
    def createObjects(self):
        self.driverJoystick = wpilib.Joystick(0)

        motorType = rev.CANSparkMaxLowLevel.MotorType.kBrushless
        self.frontLeftMotor = rev.CANSparkMax(1, motorType)
        self.frontRightMotor = rev.CANSparkMax(2, motorType)
        self.backLeftMotor = rev.CANSparkMax(3, motorType)
        self.backRightMotor = rev.CANSparkMax(4, motorType)
        # self.frontLeftMotor = rev.CANSparkMax(1, 0)
        # self.frontRightMotor = rev.CANSparkMax(2, 0)
        # self.backLeftMotor = rev.CANSparkMax(3, 0)
        # self.backRightMotor = rev.CANSparkMax(4, 0)

    def teleopInit(self):
        self.speed = 0.2

    def disabledPeriodic(self):
        pass

    def teleopPeriodic(self):
        #get joystick data
        #call tank drive
        self.driveTrain.enable()

        #logitech extreme 3d. Case 10

        #get y axis - 1 (when moving joystick forward and backwards)
        wpilib.SmartDashboard.putNumber("joystick Y value", self.driverJoystick.getY())
        #get x axis - 0 (when moving joystick sideways)
        wpilib.SmartDashboard.putNumber("joystick X value", self.driverJoystick.getX())
        #get the rotational value - 2 (when twisting joystick) left: -1, right: 1
        wpilib.SmartDashboard.putNumber("joystick Z value", self.driverJoystick.getZ())

        # wpilib.SmartDashboard.putNumber("joystick  radians value", self.driverJoystick.getDirectionRadians())
        # wpilib.SmartDashboard.putNumber("joystick  throttle", self.driverJoystick.getThrottle())
        # wpilib.SmartDashboard.putNumber("joystick  get top", self.driverJoystick.getTop())
        # wpilib.SmartDashboard.putNumber("joystick  trigger", self.driverJoystick.getTrigger())
        # wpilib.SmartDashboard.putNumber("joystick  get twist", self.driverJoystick.getTwist())

        # self.driveTrain.arcade_drive(self.speed*self.driverJoystick.getX(), self.speed*self.driverJoystick.getY())



if __name__ == '__main__':
    wpilib.run(MyRobot)



