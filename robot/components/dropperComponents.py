import wpimath.controller
import rev
from util import remap


class DropperComponents:
    dropperMotor: rev.CANSparkMax
    # dropperSensor: wpilib.AnalogPotentiometer  # we definitely need to change this. THIS IS NOT CORRECT. JUST PLACE HOLDER. could be rev.analog input
    dropperEncoder: rev.SparkMaxAlternateEncoder

    def __init__(self):
        self
        self.enabled = False
        self.lowAngle = -45
        self.startAngle = 0

        self.dropperMotorSpeed = 0

        # These need to be small to make the PID output resonable / in the motors range
        self.kP = 0
        self.kI = 0
        self.kD = 0
        self.kTolerence = 3

        self.angleController = wpimath.controller.PIDController(
            self.kP, self.kI, self.kD
        )
        self.angleController.setTolerance(self.kTolerence)

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    def turnToAngle(self, targetAngle: float):
        # Might need to fix
        self.setMotor(self.angleController.calculate(self.getAngle(), targetAngle))

    def drop(self):
        # for button (driver preference)
        self.turnToAngle(self.lowAngle)

    def setMotor(self, speed: float):
        self.dropperMotorSpeed = speed

    def unDrop(self):
        # for button (driver preference)
        # Achilles coined this function name.
        self.turnToAngle(self.startAngle)

    def variationDrop(self, input: float):
        # for slider (driver preference)
        angle = remap(input, -1, 1, self.lowAngle, self.startAngle)
        self.turnToAngle(angle)

    def getAngle(self) -> float:
        # Could be with encoder or with potentiometer
        # This is a tmeporary value
        return 0

    def execute(self):
        if self.enabled:
            self.dropperMotor.set(self.dropperMotorSpeed)
        self.dropperMotorSpeed = 0
