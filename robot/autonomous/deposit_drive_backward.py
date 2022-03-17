from components.driveTrain import DriveTrain
from components.dropperComponents import DropperComponents
from components.transportComponents import TransportComponents

from magicbot.state_machine import AutonomousStateMachine, timed_state, state


class DepositDriveBackward(AutonomousStateMachine):

    MODE_NAME = "Deposit, drive backward"
    DEFAULT = True

    driveTrain: DriveTrain
    dropperComponents: DropperComponents
    transportComponents: TransportComponents

    @timed_state(duration=2, first=True, next_state="backOutOfTarmac")  # type:ignore
    def depositBall(self):
        self.dropperComponents.drop()
        self.transportComponents.setIntakeSpeed(0.2)

    @state()  # type:ignore
    def backOutOfTarmac(self):
        target = -100
        self.driveTrain.driveToDistance(target)
        self.dropperComponents.unDrop()
