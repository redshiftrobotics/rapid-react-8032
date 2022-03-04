import magicbot
from robotpy_ext.control.toggle import Toggle
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

import utils.joystickUtils as joystickUtils
import utils.motorUtils as motorUtils
import utils.sensorUtils as sensorUtils


class MyRobot(magicbot.MagicRobot):  # type:ignore

    driveTrain: DriveTrain

    ### These mechanisms don't exist yet ###
    # hangComponents: HangComponents
    # extendLeadScrew: ExtendLeadScrew
    # retractLeadScrew: RetractLeadScrew
    # extendPulley: ExtendPulley
    # retractPulley: RetractPulley

    # dropperComponents: DropperComponents
    # transportComponents: TransportComponents

    def createObjects(self):
        ### Joystick Setup ###
        self.driverLeftJoystick = wpilib.Joystick(joystickUtils.kDriverLeftJoystickID)
        self.driverRightJoystick = wpilib.Joystick(joystickUtils.kDriverRightJoystickID)
        self.slowButtonToggle = Toggle(self.driverRightJoystick, joystickUtils.kSlowButton) # The right joystick controls drivetrain speed

        self.operatorJoystick = wpilib.Joystick(joystickUtils.kOperatorJoystickID)

        #### Drivetrain Setup ###
        self.frontLeftMotor = rev.CANSparkMax(
            motorUtils.kFrontLeftMotorID, motorUtils.kCANSparkMaxBrushless
        )
        self.frontRightMotor = rev.CANSparkMax(
            motorUtils.kFrontRightMotorID, motorUtils.kCANSparkMaxBrushless
        )
        self.backLeftMotor = rev.CANSparkMax(
            motorUtils.kBackLeftMotorID, motorUtils.kCANSparkMaxBrushless
        )
        self.backRightMotor = rev.CANSparkMax(
            motorUtils.kBackRightMotorID, motorUtils.kCANSparkMaxBrushless
        )

        self.frontLeftMotor.setInverted(motorUtils.isFrontLeftMotorReversed)
        self.backLeftMotor.setInverted(motorUtils.isBackLeftMotorReversed)
        self.frontRightMotor.setInverted(motorUtils.isFrontRightMotorReversed)
        self.backRightMotor.setInverted(motorUtils.isBackRightMotorReversed)

        # initialize encoders
        self.leftEncoder = self.backLeftMotor.getAlternateEncoder(
            motorUtils.kTicksPerRev
        )
        self.rightEncoder = self.backRightMotor.getAlternateEncoder(
            motorUtils.kTicksPerRev
        )

        # Create gyroscope. spi - communications protocol
        self.ahrs = AHRS.create_spi()  # type:ignore

        ### These mechanisms don't exist yet ###

        ### Intake Setup ###
        # with self.consumeExceptions():
        #     self.intakeMotor = rev.CANSparkMax(motorUtils.kIntakeMotorID, motorUtils.kCANSparkMaxBrushed)
        #     self.intakeMotor.setInverted(motorUtils.isIntakeMotorReversed)

        ### Dropper Setup ###
        # with self.consumeExceptions():
        #     self.dropperMotor = rev.CANSparkMax(motorUtils.kDropperMotorID, motorUtils.kCANSparkMaxBrushed)
        #     self.dropperMotor.setInverted(motorUtils.isDropperMotorReversed)
        #     self.dropperSensor = wpilib.AnalogPotentiometer(
        #         sensorUtils.kDropperSensorID,
        #         sensorUtils.kDropperSensorStart,
        #         sensorUtils.kDropperSensorEnd,
        # )

        ### Hang Setup ###
        # with self.consumeExceptions():
        #     self.leadScrewMotor = rev.CANSparkMax(motorUtils.kPulleyMotorID, motorUtils.kCANSparkMaxBrushless)
        #     self.pulleyMotor = rev.CANSparkMax(motorUtils.kLeadScrewMotorID, motorUtils.kCANSparkMaxBrushed)

        #     self.topPulleySensor = wpilib.DigitalInput(sensorUtils.kTopPulleySensorID)
        #     self.bottomPulleySensor = wpilib.DigitalInput(
        #         sensorUtils.kBottomPulleySensorID
        #     )
        #     self.topLeadScrewSensor = wpilib.DigitalInput(
        #         sensorUtils.kTopLeadScrewSensorID
        #     )
        #     self.bottomLeadScrewSensor = wpilib.DigitalInput(
        #         sensorUtils.kBottomLeadScrewSensorID
        #     )

        ### Auto Setup ###
        with self.consumeExceptions():
            self.auto = AutonomousModeSelector("autonomous")

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

        ### These mechanisms don't exist yet ###
        # with self.consumeExceptions():
        #     self.hangComponents.enable()

    def teleopPeriodic(self):
        ### These mechanisms don't exist yet ###
        ### Hang Control Code ###
        # with self.consumeExceptions():
        #     if self.driverJoystick.getRawButton(joystickUtils.kLeadScrewExtendButton):
        #         self.extendLeadScrew.extendLeadScrew()

        # with self.consumeExceptions():
        #     if self.driverJoystick.getRawButton(joystickUtils.kLeadScrewRetractButton):
        #         self.retractLeadScrew.retractLeadScrew()

        # with self.consumeExceptions():
        #     if self.driverJoystick.getRawButton(joystickUtils.kPulleyExtendButton):
        #         self.extendPulley.extendPulley()

        # with self.consumeExceptions():
        #     if self.driverJoystick.getRawButton(joystickUtils.kPulleyRetractButton):
        #         self.retractPulley.retractPulley()

        ### Drivetrain Control Code ###

        # The right joystick controls drivetrain speed
        self.driveTrain.setMaxSpeed(joystickUtils.kNormalSpeed)
        if self.driverRightJoystick.getRawButtonPressed(joystickUtils.kNitroButton):
            self.driveTrain.setMaxSpeed(joystickUtils.kNitroSpeed)
        if self.slowButtonToggle.get():
            self.driveTrain.setMaxSpeed(joystickUtils.kSlowSpeed)

        # `getX` left to right is turns the robot. Replace with `getZ` for twist
        self.driveTrain.tankDrive(
            joystickUtils.isYAxisReversed * self.driverLeftJoystick.getX(),
            joystickUtils.isYAxisReversed * self.driverRightJoystick.getY(),
        )

    def disabledPeriodic(self):
        pass


if __name__ == "__main__":
    wpilib.run(MyRobot)  # type:ignore
