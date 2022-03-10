from magicbot.state_machine import StateMachine, state
import wpilib
from components.hangComponents import HangComponents
import utils.joystickUtils as joystickUtils


class ExtendPulley(StateMachine):
    hangComponents: HangComponents

    def extendPulley(self):
        self.engage()  # type:ignore

    @state(first=True)  # type:ignore
    def startExtendPulley(self):

        wpilib.SmartDashboard.putBoolean(
            "pulleyMotorSensor", self.hangComponents.getTopPulleySensor()
        )
        if self.hangComponents.getTopPulleySensor():
            self.hangComponents.setPulleyMotorSpeed(joystickUtils.kPulleySpeed)
