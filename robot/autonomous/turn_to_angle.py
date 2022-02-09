from navx import AHRS
from components.driveTrain import DriveTrain
from magicbot.state_machine import AutonomousStateMachine, state


class TurnToAngle(AutonomousStateMachine):

    MODE_NAME = "Turn to angle"
    DEFAULT = False

    driveTrain: DriveTrain
    ahrs: AHRS

    @state(first=True)  # type:ignore
    def turnToAngle(self):

        target = 90

        if self.ahrs.getYaw() != 90:

            current = self.ahrs.getYaw()

            if current > target:
                self.driveTrain.arcadeDrive(-0.2, 0)

            if current < target:
                self.driveTrain.arcadeDrive(0.2, 0)
