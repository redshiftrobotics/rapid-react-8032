import time
from xmlrpc.client import Boolean
import wpilib


def remap(value: float, inputLow: float, inputHigh: float, outputLow: float, outputHigh: float):
    ratio = abs(outputHigh - outputLow) / abs(inputHigh - inputLow)

    return (value - inputLow) * ratio + outputLow


def clamp(speed: float, maxSpeed: float, minSpeed: float):

    if speed > maxSpeed:
        return maxSpeed

    if speed < minSpeed:
        return minSpeed

    return speed


def deadBand(speed: float, deadband: float):
    if abs(speed) < deadband:
        return 0

    return speed


class AccelerationLimiter:
    def __init__(
        self,
        max_acceleration: float,
        useNoAccelWhenSpeedingDown: Boolean = True,
    ):
        self.max_acceleration = max_acceleration
        self.useNoAccelWhenSpeedingDown = useNoAccelWhenSpeedingDown

        self.prev_time = time.time()
        self.prev_pos = 0

    def calculate(self, target_pos: float):
        if abs(target_pos) < abs(self.prev_pos) and self.useNoAccelWhenSpeedingDown:
            return target_pos

        # Calculate the current velocity and acceleration
        new_time = time.time()
        time_diff = 0.02 # new_time - self.prev_time

        if time_diff > 0:
            curr_vel = (target_pos - self.prev_pos) / time_diff

            wpilib.SmartDashboard.putNumber("target_pos", target_pos)
            wpilib.SmartDashboard.putNumber("curr_vel", curr_vel)

            new_vel = clamp(curr_vel, self.max_acceleration, -self.max_acceleration)
            new_pos = self.prev_pos + (new_vel * time_diff)

            wpilib.SmartDashboard.putNumber("new_vel", new_vel)
            wpilib.SmartDashboard.putNumber("new_pos", new_pos)

            print(
                "target_pos",
                round(target_pos, 2),
                "curr_vel",
                round(curr_vel, 2),
                "new_vel",
                round(new_vel, 2),
                "new_pos",
                round(new_pos, 2),
            )

            # Store the calculated values for the next loop iteration
            self.prev_pos = new_pos
            self.prev_time = new_time

            return new_pos
        else:
            return target_pos
