import rev
import utils.util as util


class TransportComponents:
    # Motor
    transportMotor: rev.CANSparkMax
    intakeShooterMotor: rev.CANSparkMax

    def __init__(self):
        self.enabled = False
        self.transportMotorSpeed = 0
        self.intakeShooterSpeed = 0
        self.transportAccelerationLimiter = util.AccelerationLimiter(100000, 1, False)
        self.intakShooterAccelerationLimiter = util.AccelerationLimiter(100000, 1, False)

    def setTransportSpeed(self, transportSpeed: float):
        self.transportMotorSpeed = transportSpeed

    def getTransportSpeed(self):
        return self.transportMotorSpeed

    def setIntakeShooterSpeed(self, intakeShooterSpeed: float):
        self.intakeShooterSpeed = intakeShooterSpeed

    def getIntakeShooterSpeed(self):
        return self.intakeShooterSpeed

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    def execute(self):
        if self.enabled:
            self.transportMotor.set(self.transportAccelerationLimiter.calculate(self.transportMotorSpeed))
            self.intakeShooterMotor.set(self.intakShooterAccelerationLimiter.calculate(self.intakeShooterSpeed))

        self.transportMotorSpeed = 0
        self.intakeShooterSpeed = 0
