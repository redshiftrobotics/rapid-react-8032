
from navx import AHRS
from components.driveTrain import DriveTrain
from magicbot import AutonomousStateMachine, state, default_state

class TurnToAuto(AutonomousStateMachine):

    MODE_NAME = "Turn to angle"
    DEFAULT = False

    driveTrain: DriveTrain

    # @default_state()
    # def default (self):
    #     self.driveTrain.leftMotorSpeed = 0
    #     self.driveTrain.rightMotorSpeed = 0

    @state(first = True)
    def turn_to_angle(self):
        target = 90
        while self.ahrs.getYaw() != 90:

            current = self.ahrs.getYaw()

            if current > target:
                leftMotorSpeed = -.05
                rightMotorSpeed = 0.05

            if current < target:
                leftMotorSpeed = .05
                rightMotorSpeed = -0.05



            



