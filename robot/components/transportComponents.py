import rev
import utils.util as util


class TransportComponents:
    # Motor
    transportMotor: rev.CANSparkMax

    def __init__(self):
        self.enabled = False
        self.transportMotorSpeed = 0
        self.accelerationLimiter = util.AccelerationLimiter(100000, 1, False)

    def setTransportSpeed(self, transportSpeed: float):
        self.transportMotorSpeed = transportSpeed

    def getTransportSpeed(self):
        return self.transportMotorSpeed

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    def execute(self):
        if self.enabled:
            self.transportMotor.set(
                self.accelerationLimiter.calculate(self.transportMotorSpeed)
            )

            # Old code, use if accelerationLimiter does not work / do not need it anymore
            # self.transportMotor.set(self.transportMotorSpeed)

        self.transportMotorSpeed = 0
