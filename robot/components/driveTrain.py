import magicbot
import wpilib
import rev

class DriveTrain:
    def arcadeDrive(self, xAxis,yAxis):
        self.maxSpeed = 0.2
        self.rightMotorSpeed = yAxis-xAxis
        self.leftMotorSpeed= yAxis+xAxis