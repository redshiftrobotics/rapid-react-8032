from magicbot import StateMachine, state
import wpilib
from components.hangComponents import HangComponents


class DescendLeadScrew(StateMachine):
    hangComponents: HangComponents

    def descendLeadScrew(self):
        self.engage()  # type:ignore

    @state(first=True)
    def startDescendLeadScrew(self):

        if not self.hangComponents.getBottomLeadScrewSensor():
            self.hangComponents.setLeadScrewMotorSpeed(-1.0)
