import rev

# Global Settings
kTicksPerRev = 4096
kCANSparkMaxBrushless = rev.CANSparkMaxLowLevel.MotorType.kBrushless
kCANSparkMaxBrushed = rev.CANSparkMaxLowLevel.MotorType.kBrushed

# CAN IDs
kFrontLeftMotorID = 2
kFrontRightMotorID = 6
kBackLeftMotorID = 20
kBackRightMotorID = 5

kIntakeMotorID = 5

kDropperMotorID = 6

kLeadScrewMotorID = 8

# Motor Directions
isFrontLeftMotorReversed = False
isFrontRightMotorReversed = True
isBackLeftMotorReversed = False
isBackRightMotorReversed = True

isIntakeMotorReversed = False

isDropperMotorReversed = False

isLeadScrewMotorReversed = False
isPulleyMotorReversed = False
