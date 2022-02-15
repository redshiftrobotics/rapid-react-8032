from magicbot.state_machine import AutonomousStateMachine, state
import wpilib  # type:ignore
from components.driveTrain import DriveTrain


class DriveForward(AutonomousStateMachine):

    MODE_NAME = "Drive Forward"
    DEFAULT = False

    driveTrain: DriveTrain

    # @timed_state(duration=3, first=True)  # type:ignore
    # def driveForward(self):
    #     self.driveTrain.arcadeDrive(0, 0.1)

    @state(first=True)  # type:ignore
    def driveToDistance(self):
        target = 100
        self.driveTrain.driveToDistance(target)
        wpilib.SmartDashboard.putNumber(
            "left distance", self.driveTrain.getLeftDistance()
        )
        wpilib.SmartDashboard.putNumber(
            "right distance", self.driveTrain.getRightDistance()
        )
