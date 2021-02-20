from dataclasses import dataclass
import math


@dataclass
class ModelParameters:
    motor_axis_radius: float = 0.003
    motor_axis_length: float = 0.0409
    steel_density: float = 7500
    rated_torque: float = 0.002
    rated_current: float = 0.3
    rated_speed: float = 680.68
    inductance: float = 0.002
    resistance: float = 3.2
    rated_voltage: float = 12.0
    kp: float = 7.0
    Ti: float = 155.0
    Td: float = 0.001
    wheel_radius: float = 0.025
    track_of_wheels: float = 0.145



