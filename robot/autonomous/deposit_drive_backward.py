from components.driveTrain import DriveTrain
from components.transportComponents import TransportComponents

from magicbot.state_machine import AutonomousStateMachine, timed_state, state
import utils.joystickUtils as joystickUtils


class DepositDriveBackward(AutonomousStateMachine):

    MODE_NAME = "Deposit, drive backward"
    DEFAULT = False

    driveTrain: DriveTrain
    transportComponents: TransportComponents

    @timed_state(duration=2, first=True, next_state="backOutOfTarmac")  # type:ignore
    def depositBall(self):
        self.transportComponents.setTransportSpeed(joystickUtils.kTransportSpeed)

    @state()  # type:ignore
    def backOutOfTarmac(self):
        target = -100
        self.driveTrain.driveToDistance(target)
