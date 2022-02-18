import wpilib
import rev
from components.driveTrain import DriveTrain

class HangComponents:
    # any of these might be neo
    # leadScrewMotor: rev.CANSparkMax
    # pulleyMotor: rev.CANSparkMax

    driveTrain: DriveTrain

    topLeadScrewSensor: wpilib.DigitalInput  # check if this is correct
    bottomLeadScrewSensor: wpilib.DigitalInput
    topPulleySensor: wpilib.DigitalInput
    bottomPulleySensor: wpilib.DigitalInput

    def __init__(self):
        self.enabled = False

        self.leadScrewSpeed = 0
        self.pulleySpeed = 0

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

    def setPulleyMotorSpeed(self, speed: float):
        self.pulleySpeed = speed


    def execute(self):

        if self.enabled == True:
            # self.pulleyMotor.set(self.pulleySpeed)
            # self.leadScrewMotor.set(self.leadScrewSpeed)
            wpilib.SmartDashboard.putBoolean("Hang Component Pulley Extend",True)
            self.driveTrain.tankDrive(self.pulleySpeed,self.leadScrewSpeed)

        self.leadScrewSpeed = 0
        self.pulleySpeed = 0
