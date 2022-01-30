from traceback import print_exception
import magicbot
import wpilib
import rev
from components.driveTrain import DriveTrain
from navx import AHRS
from robotpy_ext.autonomous import AutonomousModeSelector

class MyRobot(magicbot.MagicRobot):

    driveTrain: DriveTrain
    
    def createObjects(self):
        self.driverJoystick = wpilib.Joystick(0)

        #initialized motors
        motorType = rev.CANSparkMaxLowLevel.MotorType.kBrushless
        
        self.frontLeftMotor = rev.CANSparkMax(3, motorType)
        self.frontRightMotor = rev.CANSparkMax(2, motorType)
        self.backLeftMotor = rev.CANSparkMax(4, motorType)
        self.backRightMotor = rev.CANSparkMax(1, motorType)

        self.frontLeftMotor.setInverted(True)
        self.backLeftMotor.setInverted(True)
        self.frontRightMotor.setInverted(False)
        self.backRightMotor.setInverted(False)

        #various ways to initialize encoders (not working)
        # self.leftEncoder = self.backLeftMotor.getEncoder(rev.SparkMaxRelativeEncoder.Type.kHallSensor, )
        # self.rightEncoder = self.backRightMotor.getEncoder(rev.SparkMaxRelativeEncoder.Type.kHallSensor)
        # self.leftEncoder = self.backLeftMotor.getEncoder(countsPerRev=42)
        # self.rightEncoder = self.backRightMotor.getEncoder(countsPerRev=42)

        #initialize encoders
        self.leftEncoder = self.backLeftMotor.getAlternateEncoder(1)
        self.rightEncoder = self.backRightMotor.getAlternateEncoder(1)

        #create gyroscope. spi - communications protocol 
        self.ahrs = AHRS.create_spi()

        self.auto = AutonomousModeSelector("autonomous")
        
    def autonomousInit(self):
        self.auto.start()
        self.driveTrain.enable()

    def autonomousPeriodic(self):
        self.auto.periodic()

    def teleopInit(self):
        self.speed = 0.2
        self.driveTrain.resetEncoders()
        self.driveTrain.enable()
    
    def teleopPeriodic(self):

        #get y axis - 1 (when moving joystick forward and backwards)
        wpilib.SmartDashboard.putNumber("joystick Y value", self.driverJoystick.getY())
        #get x axis - 0 (when moving joystick sideways)
        wpilib.SmartDashboard.putNumber("joystick X value", self.driverJoystick.getX())
        #get the rotational value - 2 (when twisting joystick) left: -1, right: 1
        wpilib.SmartDashboard.putNumber("joystick Z value", self.driverJoystick.getZ())

        #Rotates on horizontal plane (spins!). 0-360 degrees
        wpilib.SmartDashboard.putNumber("NavX yaw", self.ahrs.getYaw())
        #Rotates on horizontal plane. 0 -> whatever degree. Angle will not reset to 0 at 360. 
        wpilib.SmartDashboard.putNumber("NavX angle", self.ahrs.getAngle())

        #tilts forward 
        wpilib.SmartDashboard.putNumber("NavX pitch", self.ahrs.getPitch())

        #tilts sideways
        wpilib.SmartDashboard.putNumber("NavX roll", self.ahrs.getRoll())

        #the getX()) means that moving joystick left to right is turn. Can change to getZ() if driver wants to twist the joystick to turn.
        self.driveTrain.arcadeDrive(self.speed*self.driverJoystick.getX(), self.speed*self.driverJoystick.getY())

    def disabledPeriodic(self):
        pass


if __name__ == '__main__':
    wpilib.run(MyRobot)



