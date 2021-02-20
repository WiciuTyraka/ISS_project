import math


class Motor:

    def __init__(self, motor_axis_radius=0.003, motor_axis_length=0.0409, steel_density=7500, rated_torque=0.002,
                 rated_current=0.3, rated_speed=680.68, inductance=0.002, resistance=3.2):
        self._motor_axis_radius = motor_axis_radius
        self._motor_axis_length = motor_axis_length
        self._steel_density = steel_density
        self._rated_torque = rated_torque
        self._rated_current = rated_current
        self._rated_speed = rated_speed
        self._inductance = inductance
        self._resistance = resistance

        self._axis_volume = math.pi * math.pow(self._motor_axis_radius, 2) * self._motor_axis_length
        self._motor_mass = self._steel_density * self._axis_volume
        self._viscous_friction_coefficient = self._rated_torque / self._rated_speed
        self._rotational_inertia = self._motor_mass * math.pow(self._motor_axis_radius, 2) / 2
        self._mechanical_constant = self._rated_torque / self._rated_current

        self._rotational_speed = 0.0
        self._rotor_current = 0.0

    @property
    def rotational_speed(self):
        return self._rotational_speed

    @rotational_speed.setter
    def rotational_speed(self, value):
        self._rotational_speed = value

    @property
    def rotor_current(self):
        return self._rotor_current

    @rotor_current.setter
    def rotor_current(self, value):
        self._rotor_current = value

    def compute_state(self, control_signal, sampling_time, load_torque=0):
        self.rotational_speed = (sampling_time / self._rotational_inertia) * (
                    self._mechanical_constant * self.rotor_current - self._viscous_friction_coefficient * self.rotational_speed - load_torque) + self.rotational_speed
        self.rotor_current = (sampling_time / self._inductance) * (
                control_signal - self._resistance * self.rotor_current)
