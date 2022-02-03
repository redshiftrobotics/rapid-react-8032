import wpilib
import rev
import magicbot
   
class Dropper():
    dropperMotor: rev.CANSparkMax
    dropperSensor: wpilib.AnalogPotentiometer #we definitely need to change this. THIS IS NOT CORRECT. JUST PLACE HOLDER. could be rev.analog input

    def __init__(self):
        self.enabled = False

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    def turnToAngle(self, targetAngle):
        pass #Need to finish. PID should be here. Add code safety stop. 

    def drop(self):
        self.turnToAngle(-45)
    
    def unDrop(self):
        #Achilles coined this function name. 
        self.turnToAngle(0)

    def execute():
        pass
        
        
            