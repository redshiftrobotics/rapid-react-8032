import time
import wpilib

def remap(
    value: float, inputLow: float, inputHigh: float, outputLow: float, outputHigh: float
):
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
        speed = 0

    return speed

class AccelerationLimiter():
    def __init__(self, max_acceleration: float):
        self.max_acceleration = max_acceleration
        
        self.prev_time = time.time()
        self.prev_pos = 0
        self.prev_vel = 0
    
    def calculate(self, target_pos: float):
        # Calculate the current velocity and acceleration
        new_time = time.time()
        time_diff = new_time - self.prev_time

        wpilib.SmartDashboard.putNumber("target_pos", time_diff)

        if (time_diff > 0):
            curr_vel = (target_pos - self.prev_pos) / time_diff
            curr_accel = (curr_vel - self.prev_vel) / time_diff

            wpilib.SmartDashboard.putNumber("target_pos", target_pos)
            wpilib.SmartDashboard.putNumber("curr_vel", curr_vel)
            wpilib.SmartDashboard.putNumber("curr_accel", curr_accel)
            
            new_accel = clamp(curr_accel, self.max_acceleration, -self.max_acceleration)
            new_vel = new_accel * time_diff
            new_pos = new_vel * time_diff

            wpilib.SmartDashboard.putBoolean("accel_too_large", curr_accel != new_accel)
            
            wpilib.SmartDashboard.putNumber("new_accel", new_accel)
            wpilib.SmartDashboard.putNumber("new_vel", new_vel)
            wpilib.SmartDashboard.putNumber("new_pos", new_pos)

            # Store the calculated values for the next loop iteration
            self.prev_pos = new_pos
            self.prev_vel = new_vel
            self.prev_time = new_time

            return new_pos
        else:
            return target_pos