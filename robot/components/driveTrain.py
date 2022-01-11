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