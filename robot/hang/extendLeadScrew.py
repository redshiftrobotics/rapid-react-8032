from magicbot.state_machine import StateMachine, state
from components.hangComponents import HangComponents


class ExtendLeadScrew(StateMachine):
    hangComponents: HangComponents

    def extendLeadScrew(self):
        self.engage()  # type:ignore

    @state(first=True)  # type:ignore
    def startExtendLeadScrew(self):

        # the motor speed defaults back to zero unless otherwise called.
        if self.hangComponents.getTopLeadScrewSensor():
            #Changed 1.0 to 0.1 for testing
            self.hangComponents.setLeadScrewMotorSpeed(0.1)
