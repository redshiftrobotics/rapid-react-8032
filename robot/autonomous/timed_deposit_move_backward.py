from components.driveTrain import DriveTrain
from components.transportComponents import TransportComponents

from magicbot.state_machine import AutonomousStateMachine, timed_state
import utils.joystickUtils as joystickUtils


class TimedDepositDriveBackward(AutonomousStateMachine):

    MODE_NAME = "Timed, deposit, drive backwards"
    DEFAULT = False

    driveTrain: DriveTrain
    transportComponents: TransportComponents

    @timed_state(duration=3, first=True, next_state="backOutOfTarmac")  # type:ignore
    def depositBall(self):
        self.transportComponents.setTransportSpeed(joystickUtils.kTransportSpeed)
        self.transportComponents.setIntakeShooterSpeed(joystickUtils.kTransportSpeed)
        

    @timed_state(duration=4, first=False)  # type:ignore
    def backOutOfTarmac(self):
        self.driveTrain.setRightMotorSpeed(-0.2)
        self.driveTrain.setLeftMotorSpeed(-0.2)
        pass
