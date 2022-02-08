import magicbot
import wpilib
import rev


class HangComponents:
    # any of these might be neo
    leadScrewMotor: rev.CANSparkMax
    pulleyMotor: rev.CANSparkMax

    topLeadScrewSensor: wpilib.DigitalInput  # check if this is correct
    bottomLeadScrewSensor: wpilib.DigitalInput
    topPulleySensor: wpilib.DigitalInput
    bottomPulleySensor: wpilib.DigitalInput

    def __init__(self):
        self.enabled = False

        self.leadScrewSpeed = 0
        self.pulleySpeed = 0

    def setPulleyMotorSpeed(self, speed: float):
        self.pulleySpeed = speed

    def enable(self):
        self.enabled = True

    def getTopPulleySensor(self):
        return self.topPulleySensor.get()

    def getBottomPulleySensor(self):
        return self.bottomPulleySensor.get()

    def getBottomLeadScrewSensor(self):
        return self.bottomLeadScrewSensor.get()

    def getTopLeadScrewSensor(self):
        return self.topLeadScrewSensor.get()

    def setLeadScrewMotorSpeed(self, speed: float):
        self.leadScrewSpeed = speed

    def execute(self):

        if self.enabled == True:
            self.pulleyMotor.set(self.pulleySpeed)
            self.leadScrewMotor.set(self.leadScrewSpeed)

        self.leadScrewSpeed = 0
        self.pulleySpeed = 0