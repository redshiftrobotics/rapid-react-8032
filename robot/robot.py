from pydoc_data import topics
import magicbot
from robotpy_ext.control.toggle import Toggle  # type: ignore
import wpilib
import rev
from components.driveTrain import DriveTrain
from components.hangComponents import HangComponents
from components.dropperComponents import DropperComponents
from components.transportComponents import TransportComponents

from hang.extendLeadScrew import ExtendLeadScrew
from hang.retractLeadScrew import RetractLeadScrew
from navx import AHRS
from robotpy_ext.autonomous import AutonomousModeSelector  # type:ignore
from components.dropperComponents import DropperComponents
from components.transportComponents import TransportComponents

import utils.joystickUtils as joystickUtils
import utils.motorUtils as motorUtils
import utils.sensorUtils as sensorUtils
import utils.util as util


class MyRobot(magicbot.MagicRobot):  # type:ignore

    driveTrain: DriveTrain

    hangComponents: HangComponents
    extendLeadScrew: ExtendLeadScrew
    retractLeadScrew: RetractLeadScrew

    ### These mechanisms don't exist yet ###
    # dropperComponents: DropperComponents
    # transportComponents: TransportComponents

    def createObjects(self):
        ### Joystick Setup ###
        self.driverJoystick = wpilib.Joystick(joystickUtils.kDriverJoystickID)
        self.slowButtonToggle = Toggle(self.driverJoystick, joystickUtils.kSlowButton)
        self.driverYJoystickAccelerationLimiter = util.AccelerationLimiter(100000, 1) # 14 0.9
        self.driverXJoystikcAccelerationLimiter = util.AccelerationLimiter(100000, 1) # 30 0.9

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

        # self.frontLeftMotor.setIdleMode(rev.CANSparkMax.IdleMode.kCoast)
        # self.backLeftMotor.setIdleMode(rev.CANSparkMax.IdleMode.kCoast)
        # self.frontRightMotor.setIdleMode(rev.CANSparkMax.IdleMode.kCoast)
        # self.backRightMotor.setIdleMode(rev.CANSparkMax.IdleMode.kCoast)
        
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
        with self.consumeExceptions():
            self.leadScrewMotor = rev.CANSparkMax(
                motorUtils.kLeadScrewMotorID, motorUtils.kCANSparkMaxBrushless
            )

     
            self.topLeadScrewSensor = wpilib.DigitalInput(
                sensorUtils.kTopLeadScrewSensorID
            )
            self.bottomLeadScrewSensor = wpilib.DigitalInput(
                sensorUtils.kBottomLeadScrewSensorID
            )

        ### Auto Setup ###
        with self.consumeExceptions():
            self.auto = AutonomousModeSelector("autonomous")
    
    def robotInit(self):
        wpilib.CameraServer.launch()
        super().robotInit()

        

    def autonomousInit(self):
        self.auto.start()
        self.driveTrain.resetEncoders()
        self.driveTrain.resetGyroYaw()
        self.driveTrain.enable()
        self.driveTrain.setMaxSpeed(1)

    def autonomousPeriodic(self):
        self.auto.periodic()

    def teleopInit(self):
        self.driveTrain.resetEncoders()
        self.driveTrain.resetGyroYaw()
        self.driveTrain.enable()
        
        with self.consumeExceptions():
           self.hangComponents.enable()

        ### These mechanisms don't exist yet ###
        with self.consumeExceptions():
            self.hangComponents.enable()

    def teleopPeriodic(self):
        ### Hang Control Code ###

        wpilib.SmartDashboard.putBoolean(
           "topLeadScrewSensor", self.hangComponents.getTopLeadScrewSensor()
        )
        wpilib.SmartDashboard.putBoolean(
           "bottomLeadScrewSensor", self.hangComponents.getBottomLeadScrewSensor()
        )

        

        with self.consumeExceptions():
            if self.operatorJoystick.getRawButton(joystickUtils.kLeadScrewExtendButton):

                
                self.extendLeadScrew.extendLeadScrew()
                # self.hangComponents.setLeadScrewMotorSpeed(
                #     joystickUtils.kLeadScrewSpeed
                # )

        with self.consumeExceptions():
            if self.operatorJoystick.getRawButton(
                joystickUtils.kLeadScrewRetractButton
            ):
                self.retractLeadScrew.retractLeadScrew()
                # self.hangComponents.setLeadScrewMotorSpeed(
                #     -joystickUtils.kLeadScrewSpeed
                # )

        ### Drivetrain Control Code ###

        # with self.consumeExceptions():
        # self.driveTrain.setMaxSpeed(joystickUtils.kNormalSpeed)

        with self.consumeExceptions():
            if self.driverJoystick.getTrigger(): # Can also be: self.driverJoystick.getRawButtonPressed(joystickUtils.kNitroButton):
                self.driveTrain.setMaxSpeed(joystickUtils.kNitroSpeed)
            if self.slowButtonToggle.get():
                self.driveTrain.setMaxSpeed(joystickUtils.kSlowSpeed)
            wpilib.SmartDashboard.putBoolean(
                "nitro button pressed", self.driverJoystick.getTrigger()
            )
            wpilib.SmartDashboard.putNumber(
                "code max speed", self.driveTrain.getMaxSpeed()
            )

        # `getX` left to right is turns the robot. Replace with `getZ` for twist
        self.driveTrain.arcadeDrive(
            util.deadBand(joystickUtils.isXAxisReversed * self.driverXJoystikcAccelerationLimiter.calculate(self.driverJoystick.getX()), joystickUtils.kDeadband),
            util.deadBand(joystickUtils.isYAxisReversed * self.driverYJoystickAccelerationLimiter.calculate(self.driverJoystick.getY()), joystickUtils.kDeadband)
        )
        
        wpilib.SmartDashboard.putNumber("Leadscrew motor speed",self.leadScrewMotor.get())

        wpilib.SmartDashboard.putNumber("joyX", self.driverJoystick.getX())

    def disabledPeriodic(self):
        pass


if __name__ == "__main__":
    wpilib.run(MyRobot)  # type:ignore
