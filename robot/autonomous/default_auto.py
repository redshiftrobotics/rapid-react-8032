from magicbot import AutonomousStateMachine, timed_state, state
import wpilib

from components.driveTrain import DriveTrain


class DefaultAuto(AutonomousStateMachine):

    MODE_NAME = "Default Auto"
    DEFAULT = True

    driveTrain: DriveTrain

    # potentially change this to default state
    @state(first=True)
    def zeroMotor(self):
        self.driveTrain.leftMotorSpeed = 0
        self.driveTrain.rightMotorSpeed = 0
