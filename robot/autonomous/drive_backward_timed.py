import wpilib
from components.driveTrain import DriveTrain
from magicbot.state_machine import AutonomousStateMachine, timed_state


class DriveBackwardTimed(AutonomousStateMachine):

    MODE_NAME = "Drive backward timed"
    DEFAULT = False

    driveTrain: DriveTrain

    @timed_state(duration=2.5, first=True) # type:ignore
    def driveBackwardTimed(self):
        self.driveTrain.tankDrive(-0.15, -0.15)