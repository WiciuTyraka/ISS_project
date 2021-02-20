import numpy as np

from control_system import ControlSystem
from utils.compute_velocities import compute_wheels_velocities, compute_robot_velocities
from utils.trajectory_handler import ComputeActualTrajectory, generate_trajectory


class Simulator:

    def __init__(self, simulation_data, model_parameters):
        self._control_system_left = ControlSystem(model_parameters)
        self._control_system_right = ControlSystem(model_parameters)
        self._trajectory_computer = ComputeActualTrajectory()

        self.speed_left = np.zeros(simulation_data.steps)
        self.current_left = np.zeros(simulation_data.steps)
        self.speed_right = np.zeros(simulation_data.steps)
        self.current_right = np.zeros(simulation_data.steps)

        self.x = np.zeros(simulation_data.steps)
        self.y = np.zeros(simulation_data.steps)
        self.phi = np.zeros(simulation_data.steps)

        self.v = np.zeros(simulation_data.steps)
        self.omega = np.zeros(simulation_data.steps)

        self.qr = np.zeros([simulation_data.steps, 3])
        self.ur = np.zeros([simulation_data.steps, 2])
        self.omega_l = np.zeros(simulation_data.steps)
        self.omega_p = np.zeros(simulation_data.steps)
        self.control_signal_debug = np.zeros(simulation_data.steps)

        self._simulation_data = simulation_data

    def perform_simulation(self):
        n = 0
        while n < self._simulation_data.steps:
            [self.qr[n, :], self.ur[n, :]] = generate_trajectory(time=self._simulation_data.time_vector[n],
                                                                 trajectory_number=self._simulation_data.trajectory_number,
                                                                 circle_radius=self._simulation_data.trajectory_circle_radius,
                                                                 circle_period=self._simulation_data.trajectory_circle_period,
                                                                 a_coefficient=self._simulation_data.trajectory_a_coefficient,
                                                                 b_coefficient=self._simulation_data.trajectory_b_coefficient,
                                                                 delta=self._simulation_data.trajectory_delta)
            [self.omega_l[n], self.omega_p[n]] = compute_wheels_velocities(u=self.ur[n, :])

            self._control_system_left.compute_speed_and_current(input_speed=self.omega_l[n],
                                                                sampling_time=self._simulation_data.sampling_time)
            self.speed_left[n] = self._control_system_left.rotational_speed
            self.current_left[n] = self._control_system_left.rotor_current
            self.control_signal_debug[n] = self._control_system_left.pid_controller.control_signal

            self._control_system_right.compute_speed_and_current(input_speed=self.omega_p[n],
                                                                 sampling_time=self._simulation_data.sampling_time)
            self.speed_right[n] = self._control_system_right.rotational_speed
            self.current_right[n] = self._control_system_right.rotor_current

            [v, omega] = compute_robot_velocities(omega_l=self.speed_left[n], omega_p=self.speed_right[n])

            [self.x[n], self.y[n], self.phi[n]] = self._trajectory_computer.compute_trajectory(v=v, w=omega,
                                                                                               sampling_time=self._simulation_data.sampling_time)

            n = n + 1
