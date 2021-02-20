from error_handler import ErrorHandler


class PidController:
    def __init__(self, kp=7.0, Ti=155.0, Td=0.001):
        self._kp = kp
        self._Ti = Ti
        self._Td = Td
        self.error_handler_inst = ErrorHandler()
        self._control_signal = 0.0

    @property
    def control_signal(self):
        return self._control_signal

    @control_signal.setter
    def control_signal(self, value):
        self._control_signal = value

    def compute_control_signal(self, error, sampling_time):
        self.error_handler_inst.error_writing(error)
        self.error_handler_inst.compute_error_delta()
        control_signal_delta = self._kp * self.error_handler_inst.error_delta + error * sampling_time / self._Ti + self.error_handler_inst.error_delta_2 * self._Td / sampling_time
        self.control_signal = self.control_signal + control_signal_delta
        if self.control_signal > 12:
            self.control_signal = 12
        elif self.control_signal < -12:
            self.control_signal = -12
