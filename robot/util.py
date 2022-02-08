def remap(value, inputLow, inputHigh, outputLow, outputHigh):
    ratio = abs(outputHigh - outputLow) / abs(inputHigh - inputLow)

    return (value - inputLow) * ratio + outputLow
