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

kTransportMotorID = 10
kIntakeShooterMotorID = 9

kLeadScrewMotorID = 8

# Motor Directions
isFrontLeftMotorReversed = False
isFrontRightMotorReversed = True
isBackLeftMotorReversed = False
isBackRightMotorReversed = True

isTransportMotorReversed = False
isIntakeShooterMotor = True

isLeadScrewMotorReversed = False
