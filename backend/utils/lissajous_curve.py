import math
import numpy as np


def compute_phi_delta(circle_period):
    return 2 * math.pi / circle_period


def compute_phi(phi_delta, time):
    return time * phi_delta


def compute_x(r, phi, delta, a):
    return -r * math.sin(a * phi + delta) + r


def compute_vx(r, phi_delta, phi, delta, a):
    return -r * a * phi_delta * math.cos(a * phi + delta)


def compute_ax(r, phi_delta, phi, delta, a):
    return r * math.pow(a * phi_delta, 2) * math.sin(a * phi + delta)


def compute_y(r, phi, b):
    return r * math.sin(b * phi)


def compute_vy(r, phi_delta, phi, b):
    return r * b * phi_delta * math.cos(b * phi)


def compute_ay(r, phi_delta, phi, b):
    return -r * math.pow(b * phi_delta, 2) * math.sin(b * phi)


def compute_v(r, phi, phi_delta, delta, a, b):
    return math.sqrt(
        math.pow(compute_vx(r, phi_delta, phi, delta, a), 2) + math.pow(compute_vy(r, phi_delta, phi, b), 2))


def compute_vphi(ay, ax, vy, vx, v):
    return (ay * vx - ax * vy) / (math.pow(v, 2))


def generate_trajectory(time, circle_radius=0.20, circle_period=10, a_coefficient=1, b_coefficient=2, delta=math.pi / 2):
    phi_delta = compute_phi_delta(circle_period)
    phi = compute_phi(phi_delta, time)

    x = compute_x(circle_radius, phi, delta, a_coefficient)
    vx = compute_vx(circle_radius, phi_delta, phi, delta, a_coefficient)
    ax = compute_ax(circle_radius, phi_delta, phi, delta, a_coefficient)

    y = compute_y(circle_radius, phi, b_coefficient)
    vy = compute_vy(circle_radius, phi_delta, phi, b_coefficient)
    ay = compute_ay(circle_radius, phi_delta, phi, b_coefficient)

    v = compute_v(circle_radius, phi, phi_delta, delta, a_coefficient, b_coefficient)
    vphi = compute_vphi(ay, ax, vy, vx, v)

    return [np.array([x, y, phi]), np.array([v, vphi])]
