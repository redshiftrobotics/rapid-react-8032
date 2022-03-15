from components.driveTrain import DriveTrain
from magicbot.state_machine import AutonomousStateMachine, timed_state


class DriveBackward(AutonomousStateMachine):

    MODE_NAME = "Drive forward, deposit, drive backward"

    driveTrain: DriveTrain

    @timed_state(duration=3, first=True)  # type:ignore
    def driveBackwardTimed(self):
        self.driveTrain.tankDrive(-0.2, -0.2)
