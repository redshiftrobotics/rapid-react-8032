from magicbot.state_machine import StateMachine, state
from components.hangComponents import HangComponents


class RetractPulley(StateMachine):
    hangComponents: HangComponents

    def retractPulley(self):
        self.engage()  # type:ignore

    @state(first=True)  # type:ignore
    def startRetractPulley(self):
        if self.hangComponents.getBottomPulleySensor():
            self.hangComponents.setPulleyMotorSpeed(-0.1)
