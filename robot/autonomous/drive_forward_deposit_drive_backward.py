from components.driveTrain import DriveTrain
from components.transportComponents import TransportComponents
import utils.joystickUtils as joystickUtils
from magicbot.state_machine import AutonomousStateMachine, timed_state, state


class DriveForwardDepositDriveBackward(AutonomousStateMachine):

    MODE_NAME = "Deposit and drive backward"
    DEFAULT = False

    driveTrain: DriveTrain
    transportComponents: TransportComponents

    @state(first=True)  # type:ignore
    def driveToHub(self):
        target = -100
        self.driveTrain.driveToDistance(target)

        if self.driveTrain.atDistancePIDSetPoint():
            self.next_state("depositBall")  # type: ignore

    @timed_state(duration=1.5, next_state="backOutOfTarmac")  # type:ignore
    def depositBall(self):
        self.transportComponents.setTransportSpeed(joystickUtils.kTransportSpeed)

    @state()  # type:ignore
    def backOutOfTarmac(self):
        target = -100
        self.driveTrain.driveToDistance(target)
