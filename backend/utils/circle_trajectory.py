import math
import numpy as np


def compute_phi_delta(circle_period):
    return 2 * math.pi / circle_period


def compute_phi(phi_delta, time):
    return time * phi_delta


def compute_x(r, phi):
    return r * math.cos(phi) - r


def compute_vx(r, phi_delta, phi):
    return -r * phi_delta * math.sin(phi)


def compute_ax(r, phi_delta, phi):
    return -r * math.pow(phi_delta, 2) * math.cos(phi)


def compute_y(r, phi):
    return r * math.sin(phi)


def compute_vy(r, phi_delta, phi):
    return r * phi_delta * math.cos(phi)


def compute_ay(r, phi_delta, phi):
    return -r * math.pow(phi_delta, 2) * math.sin(phi)


def compute_v(r, phi, phi_delta):
    return math.sqrt(math.pow(compute_vx(r, phi_delta, phi), 2) + math.pow(compute_vy(r, phi_delta, phi), 2))


def compute_vphi(ay, ax, vy, vx, v):
    return (ay * vx - ax * vy) / (math.pow(v, 2))


def generate_trajectory(time, circle_radius=0.4, circle_period=10):
    phi_delta = compute_phi_delta(circle_period)
    phi = compute_phi(phi_delta, time)

    x = compute_x(circle_radius, phi)
    vx = compute_vx(circle_radius, phi_delta, phi)
    ax = compute_ax(circle_radius, phi_delta, phi)

    y = compute_y(circle_radius, phi)
    vy = compute_vy(circle_radius, phi_delta, phi)
    ay = compute_ay(circle_radius, phi_delta, phi)

    v = compute_v(circle_radius, phi, phi_delta)
    vphi = compute_vphi(ay, ax, vy, vx, v)

    return [np.array([x, y, phi]), np.array([v, vphi])]
