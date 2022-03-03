from lib2to3.pgen2 import driver
import wpilib
from components.driveTrain import DriveTrain
from components.dropperComponents import DropperComponents
from magicbot.state_machine import AutonomousStateMachine, state


class ScoreAndDriveBackward(AutonomousStateMachine):

    MODE_NAME = "Score and drive backward"
    DEFAULT = False

    driveTrain: DriveTrain
    #dropperComponents: DropperComponents

    # first state
   
    @state(first=True)  # type:ignore
    def driveBackward(self):
        target = -110
        self.driveTrain.driveToDistance(target)

