from components.driveTrain import DriveTrain
from components.dropperComponents import DropperComponents
from components.transportComponents import TransportComponents

from magicbot.state_machine import AutonomousStateMachine, timed_state, state


class DriveForwardDepositDriveBackward(AutonomousStateMachine):

    MODE_NAME = "Deposit and drive backward"
    DEFAULT = True

    driveTrain: DriveTrain
    dropperComponents: DropperComponents
    transportComponents: TransportComponents

    @state(first=True)  # type:ignore
    def driveToHub(self):
        target = -100
        self.driveTrain.driveToDistance(target)
        self.dropperComponents.drop()

        if self.driveTrain.atDistancePIDSetPoint():
            self.next_state("depositBall")  # type: ignore

    @timed_state(duration=1.5, next_state="backOutOfTarmac")  # type:ignore
    def depositBall(self):
        self.transportComponents.setIntakeSpeed(0.2)

    @state()  # type:ignore
    def backOutOfTarmac(self):
        target = -100
        self.driveTrain.driveToDistance(target)
        self.dropperComponents.unDrop()
