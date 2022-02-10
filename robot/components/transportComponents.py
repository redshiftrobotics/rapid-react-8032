import wpilib
import rev


class TransportComponents:
    intakeMotor: rev.CANSparkMax

    def __init__(self):
        self.enabled = False

        self.intakeMotorSpeed = 0
        self.hangPulleyMotorSpeed = 0
        self.dropperMotorSpeed = 0
        self.leadScrewMotorSpeed = 0

    def intake(self, intakeSpeed: float):
        self.intakeMotorSpeed = intakeSpeed

    def execute(self):
        wpilib.SmartDashboard.putNumber("intake motor", self.intakeMotorSpeed)

        if self.enabled:
            self.intakeMotor.set(self.intakeMotorSpeed)

        self.intakeMotorSpeed = 0
