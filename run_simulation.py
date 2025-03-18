# run_simulation.py
import os
import sys
import subprocess
import time
import traci
import config
from controllers import fixed_time_controller
from utils import helpers
import csv

def main(tlc_program="OnePerGreen"):
    """Runs the SUMO simulation with the specified traffic light control program."""

    # ALINEA Parameters (moved here)
    CYCLE_LENGTH, SATURATION_FLOW = config.CYCLE_LENGTH, config.SATURATION_FLOW
    CRITICAL_OCCUPANCY, KR, KI = config.CRITICAL_OCCUPANCY, config.KR, config.KI
    MIN_R, MAX_R = config.MIN_RATE, config.MAX_RATE

    # Edge Definitions (moved here)
    UPSTREAM_EDGE, MERGING_EDGE, DOWNSTREAM_EDGE, ON_RAMP_EDGE = "main_road", "acceleration_area", "end_main_road", "on_ramp"
    RAMP_ID = "ramp_meter"
    min_green, max_green = 5, CYCLE_LENGTH - 5


    if config.SUMO_TOOLS is None:
        sys.exit("PLEASE DECLARE THE ENVIRONMENT VARIABLE 'SUMO_HOME'")

    sys.path.append(config.SUMO_TOOLS)  # Ensure TraCI is in the Python path

    # Building the command
    sumo_cmd = [config.SUMO_BINARY, "-c", config.SUMO_CONFIG_FILE]

    # Start SUMO with TraCI
    traci.start(sumo_cmd)

    programs = ["one_veh_per_green", "mult_veh_per_green", "alinea", "deactivated", "pi-alinea"]  # Traffic Light programs


    #ALINEA initialization
    bottleneck_loops = helpers.get_inductive_loops_of_edge(MERGING_EDGE)[:4]
    r = MIN_R  # Initial value for r
    integral_error = 0

    if tlc_program in ("alinea", "pi-alinea"):

        with open('alinea_ramp_metering_data_downsteam.csv', 'w', newline='') as csvfile:
            fieldnames = ['Step', 'Upstream Flow', 'Bottleneck Occupancy', 'Downstream Occupancy',
                          'Queue Length', 'Metering Rate', 'Green Time', 'Yellow Time', 'Red Time']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for step in range(config.MAX_STEP):
                traci.simulationStep()

                if step % CYCLE_LENGTH == 0:  # Update every CYCLE_LENGTH steps
                    upstream_flow = helpers.get_edge_flow(UPSTREAM_EDGE)
                    bottleneck_occupancy = helpers.get_loops_occupancy(bottleneck_loops)
                    downstream_occupancy = helpers.get_edge_occupancy(DOWNSTREAM_EDGE)
                    queue_length = helpers.get_queue_length(ON_RAMP_EDGE)

                    occupancy_diff = CRITICAL_OCCUPANCY - downstream_occupancy
                    
                    if tlc_program == "alinea":
                        r = r + KR * occupancy_diff # ALINEA update
                    elif tlc_program == "pi-alinea":
                        integral_error += occupancy_diff  # Accumulate error

                        #PI controller part
                        r = r + KR * occupancy_diff + KI * integral_error #   
                    
                    r = max(MIN_R, min(r, MAX_R))  # Clamp metering rate

                    green_time = int(max(min_green, min((r / SATURATION_FLOW) * CYCLE_LENGTH, max_green)))
                    yellow_time = 3
                    red_time = CYCLE_LENGTH - green_time - yellow_time

                    writer.writerow({
                        'Step': step,
                        'Upstream Flow': upstream_flow,
                        'Bottleneck Occupancy': bottleneck_occupancy,
                        'Downstream Occupancy': downstream_occupancy,
                        'Queue Length': queue_length,
                        'Metering Rate': r,
                        'Green Time': green_time,
                        'Yellow Time': yellow_time,
                        'Red Time': red_time
                    })

                # Determine the traffic light phase based on the step within the cycle
                if step % CYCLE_LENGTH < green_time:
                    # Green Phase
                    traci.trafficlight.setRedYellowGreenState(RAMP_ID, "GG")
                elif step % CYCLE_LENGTH < green_time + 3: #Yellow time equals 3
                    # Yellow Phase
                    traci.trafficlight.setRedYellowGreenState(RAMP_ID, "yy")
                else:
                    # Red Phase
                    traci.trafficlight.setRedYellowGreenState(RAMP_ID, "rr")
                inserted, waiting, duration, depart_delay, depart_delay_waiting = helpers.get_vehicle_statistics()
    
                # Compute total travel time and delay
                tts = helpers.get_total_travel_time_and_delay(inserted, waiting, duration, depart_delay, depart_delay_waiting)
                print("Total Travel Time and Delay:", tts)

    else: #Fixed Time Logic
        if tlc_program in ("OnePerGreen", "MultPerGreen"):
            program_id = ("OnePerGreen", "MultPerGreen").index(tlc_program)
            fixed_time_controller.set_fixed_time_program(config.RAMP_METER_ID, programs[program_id])

        elif tlc_program == "deactivated":
            print("Traffic light is off")
            traci.trafficlight.setProgram(config.RAMP_METER_ID, programs[3]) #set the program to off

        step = 0
        while step < config.MAX_STEP: #run the simulation
            traci.simulationStep() #Steps each time
            
            inserted, waiting, duration, depart_delay, depart_delay_waiting = helpers.get_vehicle_statistics()
    
    # Compute total travel time and delay
            tts = helpers.get_total_travel_time_and_delay(inserted, waiting, duration, depart_delay, depart_delay_waiting)
            print("Total Travel Time and Delay:", tts)
            step += 1 #Simulation steps

    traci.close() #Closes the simulation


if __name__ == "__main__":
    if len(sys.argv) > 1: #If the user specified a parameter
      tlc_program = sys.argv[1] #Tlc is the first one, make it lowercase
    else:
      tlc_program = "alinea" #otherwise it defaults to alinea
    main(tlc_program) #Runs the main function with the specified program
    print("simulation done")