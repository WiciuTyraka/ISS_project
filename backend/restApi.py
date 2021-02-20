
from flask import request
from flask import Flask
import base64
from io import BytesIO
import json
from flask_cors import CORS, cross_origin
from model_parameters import ModelParameters
from simulation_data import SimulationData
from simulator import Simulator

import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')
import matplotlib.pyplot as plt

app = Flask(__name__)

cors = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/postjson', methods=['POST'])
def postJsonHandler():
    print(request.is_json)
    content = request.get_json()
    print(content)

    model_parameters_inst = ModelParameters(
        motor_axis_radius=content['motorAxisRadius'],
        motor_axis_length=content['motorAxisLength'],
        steel_density=content['steelDensity'],
        rated_torque=content['ratedTorque'],
        rated_speed=content['ratedSpeed'],
        inductance=content['inductance'],
        resistance=content['resistance'],
        rated_voltage=content['ratedVoltage'],
        kp=content['kp'],
        Ti=content['Ti'],
        Td=content['Td'],
        wheel_radius=content['wheelRadius'],
        track_of_wheels=content['trackOfWheel'])

    # simulation_data_inst trzyma parametry symulacji
    simulation_data_inst = SimulationData(
        time_of_simulation=content['timeOfSimulation'],
        sampling_time=content['samplingTime'],
        trajectory_number=content['tracjectory'],
        trajectory_circle_radius=content['trajectoryCircleRadius'],
        trajectory_circle_period=content['trajectoryCirclePeriod'],
        trajectory_a_coefficient=content['trajectoryACoefficient'],
        trajectory_b_coefficient=content['trajectoryBCoefficient'])


    # w perform_simulation jest pętla while która ma simulation_data_inst.steps iteracji
    simulator_inst = Simulator(simulation_data_inst, model_parameters_inst)
    simulator_inst.perform_simulation()

    # --------------------------- first plot 
    plot1 = plt.figure(1)
    plt.plot(simulation_data_inst.time_vector, simulator_inst.speed_left, 'r')
    plt.plot(simulation_data_inst.time_vector, simulator_inst.omega_l, 'b')

    with BytesIO() as output:
        plt.savefig(output, transparent=True, format="PNG")
        contents = output.getvalue()

    plot1_base64 = base64.b64encode(contents)

    plot1.clear()
    plt.close(plot1)

    # --------------------------- secend plot 
    plot2 = plt.figure(2)
    plt.plot(simulation_data_inst.time_vector, simulator_inst.speed_right, 'r')
    plt.plot(simulation_data_inst.time_vector, simulator_inst.omega_p, 'b')

    with BytesIO() as output:
        plt.savefig(output, transparent=True, format="PNG")
        contents = output.getvalue()

    plot2_base64 = base64.b64encode(contents)

    plot2.clear()
    plt.close(plot2)

    # --------------------------- third plot
    plot3 = plt.figure(3)
    plt.plot(simulator_inst.qr[:, 0], simulator_inst.qr[:, 1], 'b')
    plt.plot(simulator_inst.x, simulator_inst.y, 'r')


    with BytesIO() as output:
        plt.savefig(output, transparent=True, format="PNG")
        contents = output.getvalue()

    plot3_base64 = base64.b64encode(contents)

    plot3.clear()
    plt.close(plot3)
    print('good')

    #all pictures parse into json
    # data_dict = {'plot1': str(plot1_base64, 'utf-8'),
    #              'plot2': str(plot2_base64, 'utf-8'),
    #              'plot3': str(plot3_base64, 'utf-8'),
    #              'plot1_js': {
    #                 'timeVector' : {simulation_data_inst.time_vector},
    #                 'speedLeft': {simulator_inst.speed_left},
    #                 'omegaL'     : {simulator_inst.omega_l},
    #              },
    #              'plot2_js':{
    #                 'timeVector' : {simulation_data_inst.time_vector},
    #                 'speedRight': {simulator_inst.speed_right},
    #                 'omegaP'     : {simulator_inst.omega_p},
    #              },
    #              'plot3_js':{
    #                 'qr0'        : {simulator_inst.qr[:, 0]},
    #                 'qr1'        : {simulator_inst.qr[:, 1]},
    #                 'x'          : {simulator_inst.x},
    #                 'y'          : {simulator_inst.y},
    #              },
    #              }

    data_dict = {'plot1': str(plot1_base64, 'utf-8'),
                 'plot2': str(plot2_base64, 'utf-8'),
                 'plot3': str(plot3_base64, 'utf-8')}


    # lists = simulation_data_inst.time_vector.tolist()
    # json_str = json.dumps(lists)
    # print(json_str)
    data_json = json.dumps(data_dict)

    return data_json


app.run(host='0.0.0.0', port=8090)
