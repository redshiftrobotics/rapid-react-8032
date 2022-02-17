from magicbot.state_machine import StateMachine, state
from components.hangComponents import HangComponents


class ExtendLeadScrew(StateMachine):
    hangComponents: HangComponents

    def extendLeadScrew(self):
        self.engage()  # type:ignore

    @state(first=True)  # type:ignore
    def startExtendLeadScrew(self):

        #Magnet Sensor is True when away from magnet and False when close to magnet
        # the motor speed defaults back to zero unless otherwise called.
        if self.hangComponents.getTopLeadScrewSensor():
            self.hangComponents.setLeadScrewMotorSpeed(1.0)
