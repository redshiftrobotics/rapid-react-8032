import wpilib
import rev


class Transport:
    intakeMotor: rev.CANSparkMax

    def __init__(self):
        self.enabled = False

    def setIntakeSpeed(self, intakeSpeed: float):
        self.intakeMotorSpeed = intakeSpeed

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    def execute(self):
        # wpilib.SmartDashboard.putNumber("intake motor", self.intakeMotorSpeed)
        if self.enabled:
            self.intakeMotor.set(self.intakeMotorSpeed)

        self.intakeMotorSpeed = 0
