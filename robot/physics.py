# type: ignore
import wpilib.simulation

from pyfrc.physics.core import PhysicsInterface
from pyfrc.physics import motor_cfgs, tankmodel
from pyfrc.physics.units import units

from networktables import NetworkTables


class PhysicsEngine:
    """
    Simulates a motor moving something that strikes two limit switches,
    one on each end of the track. Obviously, this is not particularly
    realistic, but it's good enough to illustrate the point
    """

    def __init__(self, physics_controller: PhysicsInterface, robot):

        self.physics_controller = physics_controller
        self.robot = robot

        # NetworkTables.initialize()
        self.nt = NetworkTables.getTable("sim")

        # Motors
        # self.fl_motor = wpilib.simulation.SimDeviceSim("SPARK MAX [3]")
        # self.fr_motor = wpilib.simulation.SimDeviceSim("SPARK MAX [2]")
        # self.bl_motor = wpilib.simulation.SimDeviceSim("SPARK MAX [4]")
        # self.br_motor = wpilib.simulation.SimDeviceSim("SPARK MAX [1]")

        # print("devices:", wpilib.simulation.SimDeviceSim.enumerateDevices())

        # self.l_speed = self.fl_motor.getDouble("Applied Output")
        # self.r_speed = self.fr_motor.getDouble("Applied Output")

        # self.dio1 = wpilib.simulation.DIOSim(1)
        # self.dio2 = wpilib.simulation.DIOSim(2)
        # self.ain2 = wpilib.simulation.AnalogInputSim(2)

        # self.motor = wpilib.simulation.PWMSim(4)

        # # Gyro
        # self.gyro = wpilib.simulation.AnalogGyroSim(1)
        self.navx = wpilib.simulation.SimDeviceSim("navX-Sensor[4]")
        self.navx_yaw = self.navx.getDouble("Yaw")

        # self.position = 0

        # Change these parameters to fit your robot!
        bumper_width = 3.25 * units.inch

        # fmt: off
        self.drivetrain = tankmodel.TankModel.theory(
            motor_cfgs.MOTOR_CFG_NEO_550,       # motor configuration
            110 * units.lbs,                    # robot mass
            10.71,                              # drivetrain gear ratio
            2,                                  # motors per side
            22 * units.inch,                    # robot wheelbase
            23 * units.inch + bumper_width * 2, # robot width
            32 * units.inch + bumper_width * 2, # robot length
            6 * units.inch,                     # wheel diameter
        )
        # fmt: on

    def update_sim(self, now: float, tm_diff: float) -> None:
        """
        Called when the simulation parameters for the program need to be
        updated.
        :param now: The current time as a float
        :param tm_diff: The amount of time that has passed since the last
        time that this function was called
        """

        # Simulate the drivetrain
        # l_speed = self.l_speed.get()
        # r_speed = self.r_speed.get()

        # print("motor current:", l_mc, r_mc)
        # v = sm.getDouble("Motor Current")
        # v.value = 42
        # print("Motor current is", m.getOutputCurrent())

        transform = self.drivetrain.calculate(
            self.nt.getNumber("drivetrain.leftSpeed", 0),
            self.nt.getNumber("drivetrain.rightSpeed", 0),
            tm_diff,
        )
        pose = self.physics_controller.move_robot(transform)

        # Update the gyro simulation
        # -> FRC gyros are positive clockwise, but the returned pose is positive
        #    counter-clockwise
        # self.gyro.setAngle(-pose.rotation().degrees())
        self.navx_yaw.value = -pose.rotation().degrees()

        # # update position (use tm_diff so the rate is constant)
        # self.position += self.motor.getSpeed() * tm_diff * 3

        # # update limit switches based on position
        # if self.position <= 0:
        #     switch1 = True
        #     switch2 = False

        # elif self.position > 10:
        #     switch1 = False
        #     switch2 = True

        # else:
        #     switch1 = False
        #     switch2 = False

        # # set values here
        # self.dio1.setValue(switch1)
        # self.dio2.setValue(switch2)
        # self.ain2.setVoltage(self.position)
