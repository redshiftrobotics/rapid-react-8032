from magicbot import AutonomousStateMachine, timed_state, default_state
import wpilib
from components.driveTrain import DriveTrain

class DriveForward(AutonomousStateMachine):

    MODE_NAME = "Drive Forward"
    DEFAULT = False

    driveTrain: DriveTrain    

    @timed_state(duration=3, first = True)
    def driveForward(self):
        self.driveTrain.arcadeDrive(0, 0.1) 
