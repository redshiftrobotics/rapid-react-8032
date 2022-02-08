from magicbot import StateMachine, state
import wpilib
from components.hangComponents import HangComponents


class ExtendPulley(StateMachine):
    hangComponents: HangComponents

    def extendPulley(self):
        self.engage()  # type:ignore

    @state(first=True)
    def startExtendPulley(self):

        if not self.hangComponents.getTopPulleySensor():
            self.hangComponents.setPulleyMotorSpeed(
                0.1
            )  # 0.1 isn't the final speed might need to change
