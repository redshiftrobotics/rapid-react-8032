import magicbot
import wpilib
import rev

class DriveTrain():

    frontLeftMotor: rev.CANSparkMax
    frontRightMotor: rev.CANSparkMax
    backLeftMotor: rev.CANSparkMax
    backRightMotor: rev.CANSparkMax
    # leftEncoder: rev.CANEncoder
    # rightEncoder: rev.CANEncoder

    def __init__(self):
        self.enabled = False

        self.rightMotorSpeed = 0
        self.leftMotorSpeed = 0 


    def arcade_drive(self, xAxis,yAxis):
        self.rightMotorSpeed = yAxis+xAxis
        self.leftMotorSpeed = yAxis-xAxis

    def tank_drive(self, rightJoystickValue, leftJoystickValue):
        self.rightMotorSpeed = rightJoystickValue
        self.leftMotorSpeed = leftJoystickValue

    def enable(self):
    
        self.enabled = True

    def disable(self):
        self.enabled = False
   
    def capSpeed(self, speed, maxSpeed, minSpeed):
        if speed > maxSpeed:
            return maxSpeed

        if speed < minSpeed:
            return minSpeed
        
        return speed
            
    def execute(self):
       
        # maxSpeed = 1
        # minSpeed = -1
        # self.leftMotorSpeed = self.capSpeed(self.leftMotorSpeed, maxSpeed, minSpeed)
        # self.rightMotorSpeed = self.capSpeed(self.rightMotorSpeed, maxSpeed, minSpeed)

        if self.enabled:
            self.backLeftMotor.set(self.leftMotorSpeed)
            self.backRightMotor.set(self.rightMotorSpeed)
            self.frontLeftMotor.set(self.leftMotorSpeed)
            self.frontRightMotor.set(self.rightMotorSpeed)
        
        # self.leftMotorSpeed = 0
        # self.rightMotorSpeed = 0






