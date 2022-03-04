import wpilib
import wpimath.controller
import rev
from utils.util import remap


class DropperComponents:
    # Motors
    dropperMotor: rev.CANSparkMax

    # Sensors
    dropperSensor: wpilib.AnalogPotentiometer  # we definitely need to change this. THIS IS NOT CORRECT. JUST PLACE HOLDER. could be rev.analog input
    dropperEncoder: rev.SparkMaxAlternateEncoder

    def __init__(self):
        ### General Setup ###
        self.enabled = False
        self.lowAngle = -45
        self.startAngle = 0

        self.dropperMotorSpeed = 0

        ### PID Setup ###
        # These need to be small to make the PID output resonable / in the motors range
        self.kP = 0
        self.kI = 0
        self.kD = 0
        self.kTolerance = 3

        self.angleController = wpimath.controller.PIDController(
            self.kP, self.kI, self.kD
        )
        self.angleController.setTolerance(self.kTolerance)

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    def turnToAngle(self, targetAngle: float):
        self.setMotor(self.angleController.calculate(self.getAngle(), targetAngle))

    def drop(self):
        self.turnToAngle(self.lowAngle)

    def setMotor(self, speed: float):
        self.dropperMotorSpeed = speed

    def unDrop(self):
        self.turnToAngle(self.startAngle)

    def variationDrop(self, input: float):
        angle = remap(input, -1, 1, self.lowAngle, self.startAngle)
        self.turnToAngle(angle)

    def getAngle(self) -> float:
        # Could be with encoder or with potentiometer
        # This is a temporary value
        return 0

    def atDropperPIDAnglePoint(self):
        return self.angleController.atSetpoint()

    def execute(self):
        if self.enabled:
            self.dropperMotor.set(self.dropperMotorSpeed)
        self.dropperMotorSpeed = 0
