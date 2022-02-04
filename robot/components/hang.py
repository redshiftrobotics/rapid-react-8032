import magicbot
import wpilib
import rev

class Hang():
    #any of these might be neo
    leadScrewMotor: rev.CANSparkMax
    pulleyMotor: rev.CANSparkMax

    topLeadScrewSensor: wpilib.DigitalInput #check if this is correct
    bottomLeadScrewSensor: wpilib.DigitalInput
    topPulleySensor: wpilib.DigitalInput
    bottomPulleySensor: wpilib.DigitalInput

    def __init__(self):
        self.enable = False

        self.leadScrewSpeed = 0
        self.pulleySpeed = 0
    
    def setPulleyMotorSpeed(self, speed):
        self.pulleySpeed = speed

    def getTopPulleySensor(self):
        return self.topPulleySensor.get()

    def getBottomPulleySensor(self):
        return self.bottomPulleySensor.get()

    def getBottomLeadScrewSensor(self):
        return self.bottomLeadScrewSensor.get()

    def getTopLeadScrewSensor(self):
        return self.topLeadScrewSensor.get()
        
    def pulleyToTop(self):
        pass
    def pulleyToBottom(self):
        pass

    def leadScrewToTop(self):
        pass
    def leadScrewToBottom(self):
        pass

    
