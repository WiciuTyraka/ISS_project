from pid_controller import PidController
from motor import Motor


class ControlSystem:
    def __init__(self, model_parameters):
        self.motor = Motor()
        self.pid_controller = PidController(model_parameters.kp, model_parameters.Ti, model_parameters.Td)
        self._rated_voltage = model_parameters.rated_voltage
        self._rated_current = model_parameters.rated_current
        self._rated_speed = model_parameters.rated_speed
        self._resistance = model_parameters.resistance

        self._input_coefficient = self._rated_voltage / self._rated_speed
        self._coil_emf = self._rated_voltage - self._rated_current * self._resistance
        self._electric_coefficient = self._coil_emf / self._rated_speed

        self._voltage_error = 0.0
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

    def compute_voltage_error(self, input_speed):
        self._voltage_error = self._input_coefficient * input_speed - self._electric_coefficient * self.rotational_speed

    def compute_speed_and_current(self, input_speed, sampling_time):
        self.compute_voltage_error(input_speed)
        self.pid_controller.compute_control_signal(error=self._voltage_error, sampling_time=sampling_time)
        self.motor.compute_state(control_signal=self.pid_controller.control_signal, sampling_time=sampling_time)
        self.rotational_speed = self.motor.rotational_speed
        self.rotor_current = self.motor.rotor_current
