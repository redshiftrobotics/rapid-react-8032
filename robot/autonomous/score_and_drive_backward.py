from lib2to3.pgen2 import driver
import wpilib
from components.driveTrain import DriveTrain
from components.dropperComponents import DropperComponents
from magicbot.state_machine import AutonomousStateMachine, state


class ScoreAndDriveBackward(AutonomousStateMachine):

    MODE_NAME = "Score and drive backward"
    DEFAULT = False

    driveTrain: DriveTrain
    dropperComponents: DropperComponents

    # first state
    @state(first=True)  # type:ignore
    def depositPayload(self):
        self.dropperComponents.drop()
        if self.dropperComponents.atDropperPIDAnglePoint():
            self.next_state("resetDropper")  # type:ignore

    @state(first=False)  # type:ignore
    def resetDropper(self):
        self.dropperComponents.unDrop()
        if self.dropperComponents.atDropperPIDAnglePoint():
            self.next_state("")  # type: ignore

    @state(first=False)  # type:ignore
    def driveBackward(self):
        target = -100
        self.driveTrain.driveToDistance(target)
