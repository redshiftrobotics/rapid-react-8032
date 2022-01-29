from magicbot import AutonomousStateMachine, timed_state, default_state
import wpilib

from components.driveTrain import DriveTrain

class DriveForward(AutonomousStateMachine):

    MODE_NAME = "Drive Forward"
    DEFAULT = False

    # driveTrain: DriveTrain
    # @default_state()
    # # def default(self):
        

    @timed_state(duration=3, first = True)
    def drive_forward(self):
        self.driveTrain.arcade_drive(0, 0.1) 
