import numpy as np


def compute_wheels_velocities(u, wheel_radius=0.025, track_of_wheels=0.145):
    v = u[0]
    w = u[1]

    omega_p = (v + track_of_wheels / 2 * w) / wheel_radius
    omega_l = (v - track_of_wheels / 2 * w) / wheel_radius

    return [omega_l, omega_p]


def compute_robot_velocities(omega_l, omega_p, wheel_radius=0.025, track_of_wheels=0.145):
    v = (omega_p + omega_l) * wheel_radius / 2
    w = (omega_p - omega_l) * wheel_radius / track_of_wheels

    return [v, w]
