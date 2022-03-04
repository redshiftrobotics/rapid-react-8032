def remap(
    value: float, inputLow: float, inputHigh: float, outputLow: float, outputHigh: float
):
    ratio = abs(outputHigh - outputLow) / abs(inputHigh - inputLow)

    return (value - inputLow) * ratio + outputLow


def adjustSpeed(speed: float, maxSpeed: float, minSpeed: float):
    if speed > maxSpeed:
        return maxSpeed

    if speed < minSpeed:
        return minSpeed

    if abs(speed) <= 0.01:
        speed = 0
        return speed

    return speed
