import rev


class TransportComponents:
    # Motor
    transportMotor: rev.CANSparkMax

    def __init__(self):
        self.enabled = False
        self.transportMotorSpeed = 0

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
            self.transportMotor.set(self.transportMotorSpeed)

        self.transportMotorSpeed = 0
