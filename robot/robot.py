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
from robotpy_ext.autonomous import AutonomousModeSelector  # type:ignore
from components.dropperComponents import DropperComponents
from components.transportComponents import TransportComponents

from hang.extendLeadScrew import ExtendLeadScrew
from hang.retractLeadScrew import RetractLeadScrew  # type:ignore
from joystickUtils import *
from motorUtils import *


class MyRobot(magicbot.MagicRobot):  # type:ignore

    driveTrain: DriveTrain
    hangComponents: HangComponents
    # # dropperComponents: DropperComponents
    # # transportComponents: TransportComponents
    extendLeadScrew: ExtendLeadScrew
    retractLeadScrew: RetractLeadScrew
    extendPulley: ExtendPulley
    retractPulley: RetractPulley

    def createObjects(self):
        self.driverJoystick = wpilib.Joystick(kDriverJoystickNum)
        self.operatorJoystick = wpilib.Joystick(kOperatorJoystickNum)

        # initialized motors
        motorType = rev.CANSparkMaxLowLevel.MotorType.kBrushless

        self.frontLeftMotor = rev.CANSparkMax(3, motorType)
        self.frontRightMotor = rev.CANSparkMax(2, motorType)
        self.backLeftMotor = rev.CANSparkMax(4, motorType)
        self.backRightMotor = rev.CANSparkMax(1, motorType)

        self.frontLeftMotor.setInverted(isFrontLeftMotorReversed)
        self.backLeftMotor.setInverted(isBackLeftMotorReversed)
        self.frontRightMotor.setInverted(isFrontRightMotorReversed)
        self.backRightMotor.setInverted(isBackRightMotorReversed)

        # initialize encoders
        self.leftEncoder = self.backLeftMotor.getAlternateEncoder(kTicksPerRev)
        self.rightEncoder = self.backRightMotor.getAlternateEncoder(kTicksPerRev)

        # create gyroscope. spi - communications protocol
        self.ahrs = AHRS.create_spi()  # type:ignore

        self.auto = AutonomousModeSelector("autonomous")

        # TODO update the motors with the variables for motorUtils
        # Commented out because it would mess up the robot becasue we do not currently have these mechanisms
        # _______________________mechanisms (MOTORTYPE/CHANNEL unknown)________________________

        # self.intakeMotor = rev.CANSparkMax(5, motorType)

        # self.dropperMotor = rev.CANSparkMax(6, motorType)
        # Do not know what to input for parameters. Need Channel, range, offset
        # self.dropperSensor = wpilib.AnalogPotentiometer(
        #    0
        # )  # TODO need to look over again

        self.leadScrewMotor = rev.CANSparkMax(7, motorType)
        self.pulleyMotor = rev.CANSparkMax(8, motorType)
        self.topPulleySensor = wpilib.DigitalInput(
            0
        )  # these channel numbers MUST BE CHANGED
        self.bottomPulleySensor = wpilib.DigitalInput(1)
        self.topLeadScrewSensor = wpilib.DigitalInput(2)
        self.bottomLeadScrewSensor = wpilib.DigitalInput(3)


    def autonomousInit(self):
        self.auto.start()
        self.driveTrain.resetEncoders()
        self.driveTrain.resetGyroYaw()
        self.driveTrain.enable()

    def autonomousPeriodic(self):
        self.auto.periodic()
        

    def teleopInit(self):
        self.driveTrain.resetEncoders()
        self.driveTrain.resetGyroYaw()
        self.driveTrain.enable()
        self.slowButtonToggle = False
        self.hangComponents.enable()
        

    def teleopPeriodic(self):

        # get y axis - 1 (when moving joystick forward and backwards)
        wpilib.SmartDashboard.putNumber("joystick Y value", self.driverJoystick.getY())
        # get x axis - 0 (when moving joystick sideways)
        wpilib.SmartDashboard.putNumber("joystick X value", self.driverJoystick.getX())
        # get the rotational value - 2 (when twisting joystick) left: -1, right: 1
        wpilib.SmartDashboard.putNumber("joystick Z value", self.driverJoystick.getZ())

        # Rotates on horizontal plane (spins!). 0-360 degrees
        wpilib.SmartDashboard.putNumber("NavX yaw", self.ahrs.getYaw())

        wpilib.SmartDashboard.putBoolean("magnetSensor", self.topPulleySensor.get())

        # temporary code meant for testing. Should be in higher level hang.

        # Commented out because it would mess up the robot becasue we do not currently have these mechanisms
        # buttons are randomly chosen
        # extend lead screw
        if self.driverJoystick.getRawButton(kLeadScrewExtendButton):
            self.extendLeadScrew.extendLeadScrew()

        # retracts lead screw
        if self.driverJoystick.getRawButton(kLeadScrewRetractButton):
            self.retractLeadScrew.retractLeadScrew()

        # extends pulley
        if self.driverJoystick.getRawButton(kPulleyExtendButton):
            self.extendPulley.extendPulley()

        # retract pulley
        if self.driverJoystick.getRawButton(kPulleyRetractButton):
            self.retractPulley.retractPulley()


        #Slow mode for speed
        if self.operatorJoystick.getRawButtonPressed(kSlowButton):
            self.slowButtonToggle=not self.slowButtonToggle

        #Nitro mode, makes the speed variable go up when pressing the trigger button on joystick
        if self.driverJoystick.getTrigger(): #Can also be substituted for self.driverJoystick.getRawButton(kFastButton)
            if self.slowButtonToggle:
                self.driveTrain.setSpeed(normalSpeed) 
            else:
                self.driveTrain.setSpeed(nitroSpeed)
        else:
            if self.slowButtonToggle:
                self.driveTrain.setSpeed(slowSpeed)
            else:
                self.driveTrain.setSpeed(normalSpeed)

        #the getX()) means that moving joystick left to right is turn. Can change to getZ() if driver wants to twist the joystick to turn.
        if self.driverJoystick.getX() != 0 and self.driverJoystick.getY() != 0:
            self.driveTrain.arcadeDrive(
                isYAxisReversed * self.driveTrain.getSpeed() * self.driverJoystick.getX(),
                isYAxisReversed * self.driveTrain.getSpeed() * self.driverJoystick.getY(),
            )

        

    def disabledPeriodic(self):
        pass


if __name__ == "__main__":
    wpilib.run(MyRobot)  # type:ignore
