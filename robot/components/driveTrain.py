import wpilib
import rev
import wpimath.controller
from navx import AHRS
import math
from utils.util import clamp


class DriveTrain:
    # Motors
    frontLeftMotor: rev.CANSparkMax
    frontRightMotor: rev.CANSparkMax
    backLeftMotor: rev.CANSparkMax
    backRightMotor: rev.CANSparkMax

    # Sensors
    leftEncoder: rev.SparkMaxAlternateEncoder
    rightEncoder: rev.SparkMaxAlternateEncoder
    ahrs: AHRS

    def __init__(self):
        ### General Setup ###
        self.enabled = False

        self.maxSpeed = 1

        self.rightMotorSpeed = 0
        self.leftMotorSpeed = 0

        ### PID Setup ###
        self.kWheelDiameter = 15.24  # THIS IS IN CM. 15.24 is the diameter
        self.kWheelCircumference = self.kWheelDiameter * math.pi

        # These need to be small to make the PID output reasonable
        self.kAngleP = 1 / 90
        self.kAngleI = 0
        self.kAngleD = -1 / 500
        self.kAngleTolerance = 3

        self.angleController = wpimath.controller.PIDController(
            self.kAngleP, self.kAngleI, self.kAngleD
        )
        self.angleController.setTolerance(self.kAngleTolerance)

        self.kForwardP = 1 / 100
        self.kForwardI = 0
        self.kForwardD = 0
        self.kForwardTolerance = 10

        self.forwardController = wpimath.controller.PIDController(
            self.kForwardP, self.kForwardI, self.kForwardD
        )
        self.forwardController.setTolerance(self.kForwardTolerance)

    def arcadeDrive(self, xAxis: float, yAxis: float):
        """
        Drives robot Arcade Drive
        Input: float,float
        Returns: None
        """
        # if uncomment, the robot will turn according to the joystick when moving backwards but this can cause glitches.
        # if yAxis >= 0:
        self.setRightMotorSpeed(yAxis + xAxis)
        self.setLeftMotorSpeed(yAxis - xAxis)

        # else:
        #     self.rightMotorSpeed = yAxis-xAxis
        #     self.leftMotorSpeed = yAxis+xAxis

    def tankDrive(self, rightJoystickValue: float, leftJoystickValue: float):
        """
        Drives robot Tank Drive
        Input: float,float
        Returns: None
        """
        self.setRightMotorSpeed(rightJoystickValue)
        self.setLeftMotorSpeed(leftJoystickValue)

    def enable(self):
        """
        Enables Drivetrain
        Input: None
        Returns: None
        """
        self.enabled = True

    def disable(self):
        """
        Disables Drivetrain
        Input: None
        Returns: None
        """
        self.enabled = False

    def getLeftEncoder(self):
        """
        Return the position of the right encoder
        Input: None
        Returns: float
        """
        return self.leftEncoder.getPosition()

    def getRightEncoder(self):
        """
        Return the position of the right encoder
        Input: None
        Returns: float
        """
        return self.rightEncoder.getPosition()

    def getRightDistance(self):
        """
        Return the distance the right wheel has gone
        Input: None
        Returns: float
        """
        rightDistance = self.getRightEncoder() * self.kWheelCircumference
        return rightDistance

    def getLeftDistance(self):
        """
        Return the distance the left wheel has gone
        Input: None
        Returns: float
        """
        leftDistance = self.getLeftEncoder() * self.kWheelCircumference
        return leftDistance

    def resetEncoders(self):
        """
        Resets Encoders
        Input: None
        Returns: None
        """
        self.leftEncoder.setPosition(0.0)
        self.rightEncoder.setPosition(0.0)

    def setRightMotorSpeed(self, speed: float):
        """
        Sets the right motor speed
        Input: float
        Returns: None
        """
        self.rightMotorSpeed = speed

    def setLeftMotorSpeed(self, speed: float):
        """
        Sets the left motor speed
        Input: float
        Returns: None
        """
        self.leftMotorSpeed = speed

    def turnToAngle(self, targetAngle: float):
        """
        Turns the robot to a certain angle, needs odometry reset before using
        Input: float
        Returns: None
        """
        newSpeed = self.angleController.calculate(self.getAngle(), targetAngle)

        self.setRightMotorSpeed(-newSpeed)
        self.setLeftMotorSpeed(newSpeed)

    def driveToDistance(self, targetDistance: float):
        """
        Drives the robot a certain distance using PID, needs odometry reset before using
        Input: float
        Returns: None
        """
        newLeftSpeed = self.forwardController.calculate(
            self.getLeftDistance(), targetDistance
        )
        newRightSpeed = self.forwardController.calculate(
            self.getRightDistance(), targetDistance
        )

        self.setLeftMotorSpeed(newLeftSpeed)
        self.setRightMotorSpeed(newRightSpeed)

    def getAngle(self):
        """
        Returns angle of robot
        Input: None
        Returns: float
        """
        return self.ahrs.getYaw()

    def resetGyroYaw(self):
        """
        Resets gyro yaw
        Input: None
        Returns: None
        """
        self.ahrs.zeroYaw()

    def atAnglePIDSetPoint(self):
        """
        Returns if the angle PID is at it's setpoint
        Input: None
        Returns: boolean
        """
        return self.angleController.atSetpoint()

    def resetOdometry(self):
        """
        Resets gyro yaw & encoders
        Input: None
        Returns: None
        """
        self.resetEncoders()
        self.resetGyroYaw()

    def getMaxSpeed(self):
        return self.maxSpeed

    def setMaxSpeed(self, speed: float):
        self.maxSpeed = speed

    def execute(self):
        self.leftMotorSpeed = clamp(self.leftMotorSpeed, 1, -1)
        self.rightMotorSpeed = clamp(self.rightMotorSpeed, 1, -1)

        self.leftMotorSpeed = self.leftMotorSpeed * self.getMaxSpeed()
        self.rightMotorSpeed = self.rightMotorSpeed * self.getMaxSpeed()

        wpilib.SmartDashboard.putNumber("leftMotorSpeed", self.leftMotorSpeed)
        wpilib.SmartDashboard.putNumber("rightMotorSpeed", self.rightMotorSpeed)

        if self.enabled:
            self.backLeftMotor.set(self.leftMotorSpeed)
            self.backRightMotor.set(self.rightMotorSpeed)
            self.frontLeftMotor.set(self.leftMotorSpeed)
            self.frontRightMotor.set(self.rightMotorSpeed)

        self.leftMotorSpeed = 0
        self.rightMotorSpeed = 0
