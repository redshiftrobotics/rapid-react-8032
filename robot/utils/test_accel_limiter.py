import time
from util import AccelerationLimiter

limiter = AccelerationLimiter(10000)

joystick_values = [0.0]*10 + [x / 20 for x in range(-1, -20, -1)] + [-1.0]*10

for value in joystick_values:
    limiter.calculate(value)

    time.sleep(0.02)
