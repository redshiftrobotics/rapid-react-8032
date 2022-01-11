import magicbot
import wpilib
import rev

class DriveTrain:

    frontLeftMotor: rev.CANSparkMax
    frontRightMotor: rev.CANSparkMax
    backLeftMotor: rev.CANSparkMax
    backRightMotor: rev.CANSparkMax
    leftEncoder: rev.CANEncoder
    rightEncoder: rev.CANEncoder

    def arcade_drive(self, xAxis,yAxis):
        self.maxSpeed = 0.2
        self.rightMotorSpeed = yAxis-xAxis
        self.leftMotorSpeed= yAxis+xAxis

    def tank_drive(self, rightJoystickValue, leftJoystickValue):
        self.rightMotorSpeed = rightJoystickValue
        self.leftMotorSpeed = leftJoystickValue

    def execute():

