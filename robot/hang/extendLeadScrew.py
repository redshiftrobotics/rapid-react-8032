from magicbot import StateMachine, state
import wpilib
from components.hangComponents import HangComponents


class ExtendLeadScrew(StateMachine):
    hangComponents: HangComponents

    def extendLeadScrew(self):
        self.engage()  # type:ignore

    @state(first=True)
    def startExtendLeadScrew(self):

        # the motor speed defaults back to zero unless otherwise called.
        if not self.hangComponents.getTopLeadScrewSensor():
            self.hangComponents.setLeadScrewMotorSpeed(1.0)
