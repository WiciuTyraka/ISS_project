class ErrorHandler:
    def __init__(self):
        self._error_memory = [0.0, 0.0, 0.0]
        self._error_delta = 0.0
        self._error_delta_2 = 0.0


    @property
    def error_delta(self):
        return self._error_delta

    @error_delta.setter
    def error_delta(self, value):
        self._error_delta = value

    @property
    def error_delta_2(self):
        return self._error_delta_2

    @error_delta_2.setter
    def error_delta_2(self, value):
        self._error_delta_2 = value

    def error_writing(self,error):
        self._error_memory[0] = self._error_memory[1]
        self._error_memory[1] = self._error_memory[2]
        self._error_memory[2] = error

    def compute_error_delta(self):
        self.error_delta = self._error_memory[2] - self._error_memory[1]
        self.error_delta_2 = self._error_memory[2] - 2 * self._error_memory[1] + self._error_memory[0]


