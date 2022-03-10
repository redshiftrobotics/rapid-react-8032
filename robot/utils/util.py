def remap(
    value: float, inputLow: float, inputHigh: float, outputLow: float, outputHigh: float
):
    ratio = abs(outputHigh - outputLow) / abs(inputHigh - inputLow)

    return (value - inputLow) * ratio + outputLow


def clampSpeed(speed: float, maxSpeed: float, minSpeed: float):

    if speed > maxSpeed:
        return maxSpeed

    if speed < minSpeed:
        return minSpeed

    return speed


def deadBand(speed: float, deadband: float):
    if abs(speed) < deadband:
        speed = 0

    return speed
