from magicbot import AutonomousStateMachine, timed_state, state
import wpilib

from components.driveTrain import DriveTrain

class drive_forward(AutonomousStateMachine):

    MODE_NAME = "Drive Forward"
    DEFAULT = False

    driveTrain: DriveTrain

    @timed_state(duration=3, first = True)
    def drive_forward(self):
        self.driveTrain.arcade_drive(0, 0.1) 
