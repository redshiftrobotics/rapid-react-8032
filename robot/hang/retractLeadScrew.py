from magicbot.state_machine import StateMachine, state
from components.hangComponents import HangComponents
import utils.joystickUtils as joystickUtils


class RetractLeadScrew(StateMachine):
    hangComponents: HangComponents

    def retractLeadScrew(self):
        self.engage()  # type:ignore

    @state(first=True)  # type:ignore
    def startRetractLeadScrew(self):
        if self.hangComponents.getBottomLeadScrewSensor():
            self.hangComponents.setLeadScrewMotorSpeed(-joystickUtils.kLeadScrewSpeed)
