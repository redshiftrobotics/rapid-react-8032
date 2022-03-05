import wpilib
import rev


class HangComponents:
    # Motors
    leadScrewMotor: rev.CANSparkMax
    pulleyMotor: rev.CANSparkMax

    # Sensors
    topLeadScrewSensor: wpilib.DigitalInput
    bottomLeadScrewSensor: wpilib.DigitalInput
    topPulleySensor: wpilib.DigitalInput
    bottomPulleySensor: wpilib.DigitalInput

    def __init__(self):
        ### General Setup ###
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
            # self.driveTrain.tankDrive(self.pulleySpeed,self.leadScrewSpeed)

        self.leadScrewSpeed = 0
        self.pulleySpeed = 0
        wpilib.SmartDashboard.putBoolean("TopPulley 9",self.topPulleySensor.get())
        wpilib.SmartDashboard.putBoolean("BottomPulley 7",self.bottomPulleySensor.get())
        wpilib.SmartDashboard.putBoolean("TopLeadScrew 5",self.topLeadScrewSensor.get())
        wpilib.SmartDashboard.putBoolean("BotoomLeadscrew 6",self.bottomLeadScrewSensor.get())
