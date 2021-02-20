import matplotlib.pyplot as plt

from model_parameters import ModelParameters
from simulation_data import SimulationData
from simulator import Simulator

# model_parameters_inst trzyma parametry całego ura
model_parameters_inst = ModelParameters()

# simulation_data_inst trzyma parametry symulacji
simulation_data_inst = SimulationData(
    trajectory_number=2, trajectory_a_coefficient=2, trajectory_b_coefficient=4)

# w perform_simulation jest pętla while która ma simulation_data_inst.steps iteracji
simulator_inst = Simulator(simulation_data_inst, model_parameters_inst)
simulator_inst.perform_simulation()

# poniżej tylko sprawdzenie jak ładnie działa
plot1 = plt.figure(1)
plt.subplot(2, 1, 1)
plt.plot(simulation_data_inst.time_vector, simulator_inst.speed_left, 'r')
plt.plot(simulation_data_inst.time_vector, simulator_inst.omega_l, 'b')
plt.subplot(2, 1, 2)
plt.plot(simulation_data_inst.time_vector, simulator_inst.speed_right, 'r')
plt.plot(simulation_data_inst.time_vector, simulator_inst.omega_p, 'b')

plot2 = plt.figure(2)
plt.plot(simulator_inst.qr[:, 0], simulator_inst.qr[:, 1], 'b')
plt.plot(simulator_inst.x, simulator_inst.y, 'r')
plt.show()
