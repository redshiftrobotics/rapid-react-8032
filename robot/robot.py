import magicbot
import wpilib
import rev
from components.driveTrain import DriveTrain
from components.hangComponents import HangComponents
from navx import AHRS
from robotpy_ext.autonomous import AutonomousModeSelector

class MyRobot(magicbot.MagicRobot):

    driveTrain: DriveTrain
    hangComponents: HangComponents
    
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

        #_______________________mechanisms (MOTORTYPE/CHANNEL unknown)________________________

        self.intakeMotor = rev.CANSparkMax(5, motorType)

        self.dropperMotor = rev.CANSparkMax(6, motorType)
        #Do not know what to input for parameters. Need Channel, range, offset
        self.dropperSensor = wpilib.AnalogPotentiometer(0) #TODO need to look over again
       
        self.leadScrewMotor = rev.CANSparkMax(7, motorType)
        self.pulleyMotor = rev.CANSparkMax(8, motorType)
        self.topPulleySensor = wpilib.DigitalInput(0)#these channel numbers MUST BE CHANGED
        self.bottomPulleySensor = wpilib.DigitalInput(1)
        self.topLeadScrewSensor = wpilib.DigitalInput(2)
        self.bottomLeadScrewSensor = wpilib.DigitalInput(3)



        #sensors unknown
        
    def autonomousInit(self):
        self.auto.start()
        self.driveTrain.enable()

    def autonomousPeriodic(self):
        self.auto.periodic()


    def teleopInit(self):
        self.speed = 0.2
        self.driveTrain.resetEncoders()
        self.driveTrain.enable()
        self.hangComponents.enable()
    
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

        # wpilib.SmartDashboard.putNumber("get top pressed", self.driverJoystick.getTopPressed())
        # wpilib.SmartDashboard.putNumber("get top", self.driverJoystick.getTop())
        # wpilib.SmartDashboard.putNumber("get trigger", self.driverJoystick.getTrigger())
        # wpilib.SmartDashboard.putNumber("get trigger pressed", self.driverJoystick.getTriggerPressed())
        wpilib.SmartDashboard.putNumber("1", self.driverJoystick.getRawButton(1))
        wpilib.SmartDashboard.putNumber("2", self.driverJoystick.getRawButton(2))
        wpilib.SmartDashboard.putNumber("3", self.driverJoystick.getRawButton(3))
        wpilib.SmartDashboard.putNumber("4", self.driverJoystick.getRawButton(4))
        wpilib.SmartDashboard.putNumber("5", self.driverJoystick.getRawButton(5))
        wpilib.SmartDashboard.putNumber("6", self.driverJoystick.getRawButton(6))
        wpilib.SmartDashboard.putNumber("7", self.driverJoystick.getRawButton(7))
        wpilib.SmartDashboard.putNumber("8", self.driverJoystick.getRawButton(8))
        wpilib.SmartDashboard.putNumber("9", self.driverJoystick.getRawButton(9))
        wpilib.SmartDashboard.putNumber("10", self.driverJoystick.getRawButton(10))

        #temporary code meant for testing. Should be in higher level hang.
        wpilib.SmartDashboard.putBoolean("top pulley sensor", self.hangComponents.getTopPulleySensor())
        wpilib.SmartDashboard.putBoolean("bottom pulley sensor", self.hangComponents.getBottomPulleySensor())
        wpilib.SmartDashboard.putBoolean("bottom leadscrew sensor", self.hangComponents.getBottomLeadScrewSensor())
        wpilib.SmartDashboard.putBoolean("top leadscrew sensor", self.hangComponents.getTopLeadScrewSensor())

        if self.driverJoystick.getRawButton(10):
            self.hangComponents.setPulleyMotorSpeed(1)

        if self.driverJoystick.getRawButton(9):
            self.hangComponents.setPulleyMotorSpeed(-1)

        if self.driverJoystick.getRawButton(8):
            self.hangComponents.setLeadScrewMotorSpeed(1)

        if self.driverJoystick.getRawButton(7):
            self.hangComponents.setLeadScrewMotorSpeed(-1)

        #the getX()) means that moving joystick left to right is turn. Can change to getZ() if driver wants to twist the joystick to turn.
        self.driveTrain.arcadeDrive(self.speed*self.driverJoystick.getX(), self.speed*self.driverJoystick.getY())



    def disabledPeriodic(self):
        pass

if __name__ == '__main__':
    wpilib.run(MyRobot)



