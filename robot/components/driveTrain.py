from magicbot import tunable
import wpilib
import rev
import wpimath.controller
from navx import AHRS


class DriveTrain:

    frontLeftMotor: rev.CANSparkMax
    frontRightMotor: rev.CANSparkMax
    backLeftMotor: rev.CANSparkMax
    backRightMotor: rev.CANSparkMax
    leftEncoder: rev.SparkMaxAlternateEncoder  # rev.SparkMaxRelativeEncoder
    rightEncoder: rev.SparkMaxAlternateEncoder  # rev.SparkMaxRelativeEncoder
    ahrs: AHRS

    def __init__(self):
        self.enabled = False

        self.rightMotorSpeed = 0
        self.leftMotorSpeed = 0

        # These need to be small to make the PID output resonable
        self.kP = 1 / 180
        self.kI = 0
        self.kD = 0
        self.kTolerence = 3

        self.angleController = wpimath.controller.PIDController(
            self.kP, self.kI, self.kD
        )
        self.angleController.setTolerance(self.kTolerence)

    def arcadeDrive(self, xAxis: float, yAxis: float):

        # if uncomment, the robot will turn according to the joystick when moving backwards but this can cause glitches.
        # if yAxis >= 0:
        self.setRightMotorSpeed(yAxis + xAxis)
        self.setLeftMotorSpeed(yAxis - xAxis)

        # else:
        #     self.rightMotorSpeed = yAxis-xAxis
        #     self.leftMotorSpeed = yAxis+xAxis

    def tankDrive(self, rightJoystickValue: float, leftJoystickValue: float):
        self.setRightMotorSpeed(rightJoystickValue)
        self.setLeftMotorSpeed(leftJoystickValue)

    def enable(self):

        self.enabled = True

    def disable(self):
        self.enabled = False

    # TODO move to utilities file
    def adjustSpeed(self, speed: float, maxSpeed: float, minSpeed: float):
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

    def setRightMotorSpeed(self, speed: float):
        self.rightMotorSpeed = speed

    def setLeftMotorSpeed(self, speed: float):
        self.leftMotorSpeed = speed

    def turnToAngle(self, targetAngle: float):
        newSpeed = self.angleController.calculate(self.getAngle(), targetAngle)

        wpilib.SmartDashboard.putNumber("PID Output", newSpeed)
        self.setRightMotorSpeed(newSpeed)
        self.setLeftMotorSpeed(-newSpeed)

    def getAngle(self):
        return self.ahrs.getYaw()

    def resetGyroYaw(self):
        self.ahrs.zeroYaw()

    def atPIDSetPoint(self):
        return self.angleController.atSetpoint()

    def execute(self):

        maxSpeed = 0.3
        minSpeed = -0.3
        self.leftMotorSpeed = self.adjustSpeed(self.leftMotorSpeed, maxSpeed, minSpeed)
        self.rightMotorSpeed = self.adjustSpeed(
            self.rightMotorSpeed, maxSpeed, minSpeed
        )

        wpilib.SmartDashboard.putNumber("leftWheel", self.getLeftWheelDistance())
        wpilib.SmartDashboard.putNumber("RightWheel", self.getRightWheelDistance())

        wpilib.SmartDashboard.putNumber("rightMotor value", self.rightMotorSpeed)
        wpilib.SmartDashboard.putNumber("leftMotor value", self.leftMotorSpeed)

        if self.enabled:
            self.backLeftMotor.set(self.leftMotorSpeed)
            self.backRightMotor.set(self.rightMotorSpeed)
            self.frontLeftMotor.set(self.leftMotorSpeed)
            self.frontRightMotor.set(self.rightMotorSpeed)

        self.leftMotorSpeed = 0
        self.rightMotorSpeed = 0
