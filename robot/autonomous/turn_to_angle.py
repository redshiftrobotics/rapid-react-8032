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
        if not self.driveTrain.atPIDSetPoint():
            self.driveTrain.turnToAngle(target)
