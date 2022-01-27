from magicbot import AutonomousStateMachine, timed_state, state
import wpilib

from components.driveTrain import DriveTrain

class default_auto(AutonomousStateMachine):

    MODE_NAME = "Default Auto"
    DEFAULT = True

    driveTrain: DriveTrain

    @state(first = True)
    def zero_motor(self):
        self.driveTrain.leftMotorSpeed=0
        self.driveTrain.rightMotorSpeed=0