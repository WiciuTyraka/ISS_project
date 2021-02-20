import numpy as np
import motor
import matplotlib.pyplot as plt

motor_left = motor.Motor()

steps = 50000
T = 5
Tp = 0.0001
u = 10

time = np.arange(0, 5, Tp)
current = np.zeros(steps)
speed = np.array(steps)

n = 1
while n < steps:
    motor_left.compute_state(control_signal=10, sampling_time=0.0001)
    current = np.append(current, motor_left.rotor_current)
    speed = np.append(speed, motor_left.rotational_speed)
    n = n + 1

plt.plot(time, speed)
plt.show()
