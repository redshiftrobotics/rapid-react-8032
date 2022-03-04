from components.driveTrain import DriveTrain
from magicbot.state_machine import AutonomousStateMachine, state


class ScoreAndDriveBackward(AutonomousStateMachine):

    MODE_NAME = "Score and drive backward"
    DEFAULT = False

    driveTrain: DriveTrain

    @state(first=True)  # type:ignore
    def driveBackward(self):
        target = -110
        self.driveTrain.driveToDistance(target)
