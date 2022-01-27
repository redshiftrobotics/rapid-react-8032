import imp
from unittest.mock import DEFAULT
from magicbot import AutonomousStateMachine, timed_state, state
import wpilib

from components.driveTrain import DriveTrain

class default_auto(AutonomousStateMachine):

    MODE_NAME = "Default Auto"
    DEFAULT = True