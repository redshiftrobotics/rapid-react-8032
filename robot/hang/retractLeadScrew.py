from magicbot.state_machine import StateMachine, state
from components.hangComponents import HangComponents


class RetractLeadScrew(StateMachine):
    hangComponents: HangComponents

    def retractLeadScrew(self):
        self.engage()  # type:ignore

    @state(first=True)  # type:ignore
    def startRetractLeadScrew(self):

        #Magnet Sensor is True when away from magnet and False when close to magnet
        if self.hangComponents.getBottomLeadScrewSensor():
            self.hangComponents.setLeadScrewMotorSpeed(-1.0)
