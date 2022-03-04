from components.driveTrain import DriveTrain
from magicbot.state_machine import AutonomousStateMachine, state


class TurnToAngle(AutonomousStateMachine):

    MODE_NAME = "Turn to angle"
    DEFAULT = False

    driveTrain: DriveTrain

    @state(first=True)  # type:ignore
    def turnToAngle(self):

        target = -90
        # You can get whether you are at the goal with atAnglePIDSetPoint
        self.driveTrain.turnToAngle(target)
