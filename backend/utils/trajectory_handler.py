from utils import circle_trajectory
from utils import lissajous_curve
import math


def generate_trajectory(time, trajectory_number, circle_radius, circle_period, a_coefficient, b_coefficient, delta):
    if trajectory_number == 1:
        return circle_trajectory.generate_trajectory(time, circle_radius, circle_period)
    elif trajectory_number == 2:
        return lissajous_curve.generate_trajectory(time, circle_radius, circle_period, a_coefficient, b_coefficient,
                                                   delta)


class ComputeActualTrajectory:

    def __init__(self):
        self._x = 0
        self._y = 0
        self._phi = math.pi / 2

    def compute_trajectory(self, v, w, sampling_time):
        self._x = v * math.cos(self._phi) * sampling_time + self._x
        self._y = v * math.sin(self._phi) * sampling_time + self._y
        self._phi = w * sampling_time + self._phi

        return [self._x, self._y, self._phi]
