from dataclasses import dataclass
import numpy as np
import math


@dataclass
class SimulationData:
    time_of_simulation: int = 10
    sampling_time: int = 0.0001
    trajectory_number: int = 1

    time_vector = np.arange(0, time_of_simulation, sampling_time)
    steps = int(time_of_simulation / sampling_time)
    trajectory_circle_radius: float = 0.20
    trajectory_circle_period: float = 10
    trajectory_a_coefficient: int = 1
    trajectory_b_coefficient: int = 2
    trajectory_delta: float = math.pi / 2
