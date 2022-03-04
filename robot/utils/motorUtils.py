import rev

# Global Settings
kTicksPerRev = 4096
kCANSparkMaxBrushless = rev.CANSparkMaxLowLevel.MotorType.kBrushless
kCANSparkMaxBrushed = rev.CANSparkMaxLowLevel.MotorType.kBrushed

# CAN IDs
kFrontLeftMotorID = 3
kFrontRightMotorID = 2
kBackLeftMotorID = 4
kBackRightMotorID = 1

kIntakeMotorID = 5

kDropperMotorID = 6

kLeadScrewMotorID = 7
kPulleyMotorID = 8

# Motor Directions
isFrontLeftMotorReversed = False
isFrontRightMotorReversed = True
isBackLeftMotorReversed = False
isBackRightMotorReversed = True

isIntakeMotorReversed = False

isDropperMotorReversed = False

isLeadScrewMotorReversed = False
isPulleyMotorReversed = False
