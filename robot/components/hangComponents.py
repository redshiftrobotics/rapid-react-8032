import wpilib
import rev


class HangComponents:
    # Motors
    leadScrewMotor: rev.CANSparkMax

    # Sensors
    topLeadScrewSensor: wpilib.DigitalInput
    bottomLeadScrewSensor: wpilib.DigitalInput

    def __init__(self):
        ### General Setup ###
        self.enabled = False

        self.leadScrewSpeed = 0

    def enable(self):
        self.enabled = True

    def getBottomLeadScrewSensor(self):
        return self.bottomLeadScrewSensor.get()

    def getTopLeadScrewSensor(self):
        return self.topLeadScrewSensor.get()

    def setLeadScrewMotorSpeed(self, speed: float):
        #IMPORTANT TODO make inverted variable !!!!!!!!!!!! leadscrew negative goes up and positive goes down
        self.leadScrewSpeed = speed

    def execute(self):
        if self.enabled == True:
            wpilib.SmartDashboard.putNumber("SpeedleadScrewMotor", self.leadScrewSpeed)
            self.leadScrewMotor.set(self.leadScrewSpeed)

        self.leadScrewSpeed = 0
