from magicbot.state_machine import StateMachine, state
from components.hangComponents import HangComponents
import utils.joystickUtils as joystickUtils


class ExtendLeadScrew(StateMachine):
    hangComponents: HangComponents

    def extendLeadScrew(self):
        self.engage()  # type:ignore

    @state(first=True)  # type:ignore
    def startExtendLeadScrew(self):
        if self.hangComponents.getTopLeadScrewSensor():
            self.hangComponents.setLeadScrewMotorSpeed(-joystickUtils.kLeadScrewSpeed)
