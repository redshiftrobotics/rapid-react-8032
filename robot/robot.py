import magicbot
import wpilib
import rev
from components.driveTrain import DriveTrain
from components.hangComponents import HangComponents
from components.dropperComponents import DropperComponents
from components.transportComponents import TransportComponents
from hang.extendLeadScrew import ExtendLeadScrew
from hang.retractLeadScrew import RetractLeadScrew
from hang.extendPulley import ExtendPulley
from hang.retractPulley import RetractPulley
from navx import AHRS
from robotpy_ext.autonomous import AutonomousModeSelector
from components.dropperComponents import DropperComponents
from components.transportComponents import TransportComponents

from hang.extendLeadScrew import ExtendLeadScrew
from hang.retractLeadScrew import RetractLeadScrew  # type:ignore


class MyRobot(magicbot.MagicRobot):  # type:ignore

    driveTrain: DriveTrain
    # Commented out because it would mess up the robot becasue we do not currently have these mechanisms
    # hangComponents: HangComponents
    # dropperComponents: DropperComponents
    # transportComponents: TransportComponents
    # extendLeadScrew: ExtendLeadScrew
    # retractLeadScrew: RetractLeadScrew
    # extendPulley: ExtendPulley
    # retractPulley: RetractPulley

    def createObjects(self):
        self.driverJoystick = wpilib.Joystick(0)

        # initialized motors
        motorType = rev.CANSparkMaxLowLevel.MotorType.kBrushless

        self.frontLeftMotor = rev.CANSparkMax(3, motorType)
        self.frontRightMotor = rev.CANSparkMax(2, motorType)
        self.backLeftMotor = rev.CANSparkMax(4, motorType)
        self.backRightMotor = rev.CANSparkMax(1, motorType)

        self.frontLeftMotor.setInverted(True)
        self.backLeftMotor.setInverted(True)
        self.frontRightMotor.setInverted(False)
        self.backRightMotor.setInverted(False)

        # various ways to initialize encoders (not working)
        # self.leftEncoder = self.backLeftMotor.getEncoder(rev.SparkMaxRelativeEncoder.Type.kHallSensor, )
        # self.rightEncoder = self.backRightMotor.getEncoder(rev.SparkMaxRelativeEncoder.Type.kHallSensor)
        # self.leftEncoder = self.backLeftMotor.getEncoder(countsPerRev=42)
        # self.rightEncoder = self.backRightMotor.getEncoder(countsPerRev=42)

        # initialize encoders
        self.leftEncoder = self.backLeftMotor.getAlternateEncoder(1)
        self.rightEncoder = self.backRightMotor.getAlternateEncoder(1)
        # Commented out because it would mess up the robot becasue we do not currently have these mechanisms
        # self.dropperEncoder = self.dropperMotor.getAlternateEncoder(1)

        # create gyroscope. spi - communications protocol
        self.ahrs = AHRS.create_spi()  # type:ignore

        self.auto = AutonomousModeSelector("autonomous")

        # Commented out because it would mess up the robot becasue we do not currently have these mechanisms
        # _______________________mechanisms (MOTORTYPE/CHANNEL unknown)________________________

        # self.intakeMotor = rev.CANSparkMax(5, motorType)

        # self.dropperMotor = rev.CANSparkMax(6, motorType)
        # Do not know what to input for parameters. Need Channel, range, offset
        # self.dropperSensor = wpilib.AnalogPotentiometer(
        #    0
        # )  # TODO need to look over again

        # self.leadScrewMotor = rev.CANSparkMax(7, motorType)
        # self.pulleyMotor = rev.CANSparkMax(8, motorType)
        # self.topPulleySensor = wpilib.DigitalInput(
        #    0
        # )  # these channel numbers MUST BE CHANGED
        # self.bottomPulleySensor = wpilib.DigitalInput(1)
        # self.topLeadScrewSensor = wpilib.DigitalInput(2)
        # self.bottomLeadScrewSensor = wpilib.DigitalInput(3)

        # sensors unknown

    def autonomousInit(self):
        self.auto.start()
        self.driveTrain.resetEncoders()
        self.driveTrain.resetGyroYaw()
        self.driveTrain.enable()

    def autonomousPeriodic(self):
        self.auto.periodic()

    def teleopInit(self):
        self.speed = 0.2
        self.driveTrain.resetEncoders()
        self.driveTrain.resetGyroYaw()
        self.driveTrain.enable()
        # self.hangComponents.enable()

    def teleopPeriodic(self):

        # get y axis - 1 (when moving joystick forward and backwards)
        wpilib.SmartDashboard.putNumber("joystick Y value", self.driverJoystick.getY())
        # get x axis - 0 (when moving joystick sideways)
        wpilib.SmartDashboard.putNumber("joystick X value", self.driverJoystick.getX())
        # get the rotational value - 2 (when twisting joystick) left: -1, right: 1
        wpilib.SmartDashboard.putNumber("joystick Z value", self.driverJoystick.getZ())

        # Rotates on horizontal plane (spins!). 0-360 degrees
        wpilib.SmartDashboard.putNumber("NavX yaw", self.ahrs.getYaw())

        # temporary code meant for testing. Should be in higher level hang.

        # Commented out because it would mess up the robot becasue we do not currently have these mechanisms
        # buttons are randomly chosen
        # extend lead screw
        # if self.driverJoystick.getRawButton(4):
        #    self.extendLeadScrew.extendLeadScrew()

        # retracts lead screw
        # if self.driverJoystick.getRawButton(5):
        #    self.retractLeadScrew.retractLeadScrew()

        # extends pulley
        # if self.driverJoystick.getRawButton(6):
        #    self.extendPulley.extendPulley()

        # retract pulley
        # if self.driverJoystick.getRawButton(7):
        #     self.retractPulley.retractPulley()

        # if self.driverJoystick.getRawButton(10):
        #     self.hangComponents.setPulleyMotorSpeed(1)

        # if self.driverJoystick.getRawButton(9):
        #     self.hangComponents.setPulleyMotorSpeed(-1)

        # if self.driverJoystick.getRawButton(8):
        #     self.hangComponents.setLeadScrewMotorSpeed(1)

        # if self.driverJoystick.getRawButton(7):
        #     self.hangComponents.setLeadScrewMotorSpeed(-1)

        # the getX()) means that moving joystick left to right is turn. Can change to getZ() if driver wants to twist the joystick to turn.
        self.driveTrain.arcadeDrive(
            self.speed * self.driverJoystick.getX(),
            self.speed * self.driverJoystick.getY(),
        )

    def disabledPeriodic(self):
        pass


if __name__ == "__main__":
    wpilib.run(MyRobot)  # type:ignore
