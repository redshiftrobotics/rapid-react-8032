import imp
from pkgutil import ImpImporter
import wpilib
from components.driveTrain import DriveTrain
from magicbot.state_machine import AutonomousStateMachine, state

class NextStateTest(AutonomousStateMachine):

    MODE_NAME = "Next state test"
    DEFAULT = False

    driveTrain: DriveTrain

    @state(first=True) #type:ignore
    def firstState(self):
        target = 90
        self.driveTrain.turnToAngle(target)

        if self.driveTrain.atAnglePIDSetPoint():
            self.next_state('secondState') #type:ignore

    @state(first=False)#type:ignore
    def secondState(self):
        target = 100
        self.driveTrain.driveToDistance(target)
        
