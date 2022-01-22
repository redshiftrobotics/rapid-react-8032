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

        if yAxis >= 0:
            self.rightMotorSpeed = yAxis-xAxis
            self.leftMotorSpeed = yAxis+xAxis
        
        else:
            self.rightMotorSpeed = yAxis+xAxis
            self.leftMotorSpeed = yAxis-xAxis


    def tank_drive(self, rightJoystickValue, leftJoystickValue):
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

        if abs(speed) <= 0.1:
            speed = 0
            return speed
        
        return speed
                  
    def execute(self):
       
        maxSpeed = 1
        minSpeed = -1
        self.leftMotorSpeed = self.adjustSpeed(self.leftMotorSpeed, maxSpeed, minSpeed)
        self.rightMotorSpeed = self.adjustSpeed(self.rightMotorSpeed, maxSpeed, minSpeed)

        if self.enabled:
            self.backLeftMotor.set(self.leftMotorSpeed)
            self.backRightMotor.set(self.rightMotorSpeed)
            self.frontLeftMotor.set(self.leftMotorSpeed)
            self.frontRightMotor.set(self.rightMotorSpeed)
        
        self.leftMotorSpeed = 0
        self.rightMotorSpeed = 0






