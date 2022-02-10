import wpilib
import rev
from ..util import remap


class DropperComponents:
    dropperMotor: rev.CANSparkMax
    #dropperSensor: wpilib.AnalogPotentiometer  # we definitely need to change this. THIS IS NOT CORRECT. JUST PLACE HOLDER. could be rev.analog input
    dropperEncoder: rev.SparkMaxAlternateEncoder

    def __init__(self):
        self
        self.enabled = False
        self.lowAngle = -45
        self.startAngle = 0

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    def turnToAngle(self, targetAngle: float):
        pass  # Need to finish. PID should be here. Add code safety stop.

    def drop(self):
        # for button (driver preference)
        self.turnToAngle(self.lowAngle)

    def unDrop(self):
        # for button (driver preference)
        # Achilles coined this function name.
        self.turnToAngle(self.startAngle)

    def variationDrop(self, input: float):
        # for slider (driver preference)
        angle = remap(input, -1, 1, self.lowAngle, self.startAngle)
        self.turnToAngle(angle)
    
    def getAngle(self):
        #Could be with encoder or with potentiometer
        pass

    def execute(self):
        pass
