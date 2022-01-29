
from navx import AHRS
from components.driveTrain import DriveTrain
from magicbot import AutonomousStateMachine, state, default_state

class TurnToAngle(AutonomousStateMachine):

    MODE_NAME = "Turn to angle"
    DEFAULT = False

    driveTrain: DriveTrain
    ahrs: AHRS

    # @default_state()
    # def default (self):
    #     self.driveTrain.leftMotorSpeed = 0
    #     self.driveTrain.rightMotorSpeed = 0
    
    @state(first = True)
    def turn_to_angle(self):

        target = 90

        if self.ahrs.getYaw() != 90:

            current = self.ahrs.getYaw()

            if current > target:
                self.driveTrain.arcade_drive(-0.2,0)

            if current < target:
                self.driveTrain.arcade_drive(0.2,0)



            



