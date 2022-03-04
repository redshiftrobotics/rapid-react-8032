from components.driveTrain import DriveTrain
from magicbot.state_machine import AutonomousStateMachine, state


class DriveForward(AutonomousStateMachine):

    MODE_NAME = "Drive Forward"
    DEFAULT = False

    driveTrain: DriveTrain

    @state(first=True)  # type:ignore
    def driveToDistance(self):
        target = 100
        self.driveTrain.driveToDistance(target)
