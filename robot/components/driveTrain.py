import magicbot
import wpilib
import rev
from navx import AHRS


class DriveTrain():

    frontLeftMotor: rev.CANSparkMax
    frontRightMotor: rev.CANSparkMax
    backLeftMotor: rev.CANSparkMax
    backRightMotor: rev.CANSparkMax
    leftEncoder: rev.SparkMaxAlternateEncoder #rev.SparkMaxRelativeEncoder
    rightEncoder: rev.SparkMaxAlternateEncoder #rev.SparkMaxRelativeEncoder
    ahrs: AHRS

    def __init__(self):
        self.enabled = False

        self.rightMotorSpeed = 0
        self.leftMotorSpeed = 0
        
        #encoders currently not working on robot
        # self.drivetrain_leftEncoder = self.backLeftMotor.getEncoder(rev.SparkMaxRelativeEncoder.kHallSensor)
        # self.drivetrain_rightEncoder = self.backRightMotor.getEncoder(rev.SparkMaxRelativeEncoder.kHallSensor)


    def arcadeDrive(self, xAxis,yAxis):

        #if uncomment, the robot will turn according to the joystick when moving backwards but this can cause glitches. 
        # if yAxis >= 0:
        self.rightMotorSpeed = yAxis+xAxis
        self.leftMotorSpeed = yAxis-xAxis
        
        # else:
        #     self.rightMotorSpeed = yAxis-xAxis
        #     self.leftMotorSpeed = yAxis+xAxis


    def tankDrive(self, rightJoystickValue, leftJoystickValue):
        self.rightMotorSpeed = rightJoystickValue
        self.leftMotorSpeed = leftJoystickValue

    def enable(self):
    
        self.enabled = True

    def disable(self):
        self.enabled = False
   
    def adjustSpeed(self, speed, maxSpeed, minSpeed):
        if speed > maxSpeed:
            return maxSpeed

        if speed < minSpeed:
            return minSpeed

        if abs(speed) <= 0.01:
            speed = 0
            return speed
        
        return speed
    
    def getLeftWheelDistance(self):
        return self.leftEncoder.getPosition()

    def getRightWheelDistance(self):
        return self.rightEncoder.getPosition()

    def resetEncoders(self):
        self.leftEncoder.setPosition(0.0)
        self.rightEncoder.setPosition(0.0)

                  
    def execute(self):
       
        maxSpeed = 1
        minSpeed = -1
        self.leftMotorSpeed = self.adjustSpeed(self.leftMotorSpeed, maxSpeed, minSpeed)
        self.rightMotorSpeed = self.adjustSpeed(self.rightMotorSpeed, maxSpeed, minSpeed)

        wpilib.SmartDashboard.putNumber('leftWheel', self.getLeftWheelDistance())
        wpilib.SmartDashboard.putNumber('RightWheel', self.getRightWheelDistance())

        wpilib.SmartDashboard.putNumber("rightMotor value", self.rightMotorSpeed)
        wpilib.SmartDashboard.putNumber("leftMotor value", self.leftMotorSpeed)

        if self.enabled:
            self.backLeftMotor.set(self.leftMotorSpeed)
            self.backRightMotor.set(self.rightMotorSpeed)
            self.frontLeftMotor.set(self.leftMotorSpeed)
            self.frontRightMotor.set(self.rightMotorSpeed)
        
        self.leftMotorSpeed = 0
        self.rightMotorSpeed = 0






