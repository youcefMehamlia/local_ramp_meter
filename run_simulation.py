import os
import sys
import subprocess
import time
import traci
import config
from controllers import fixed_time_controller
from utils import helpers
import csv
import argparse

def main(tlc_program="OnePerGreen", sumo_config_file=None, seed=None): #Added additional parameters
    """Runs the SUMO simulation with the specified traffic light control program."""

    # ALINEA Parameters 
    CYCLE_LENGTH, SATURATION_FLOW = config.CYCLE_LENGTH, config.SATURATION_FLOW
    CRITICAL_OCCUPANCY, KR, KI = config.CRITICAL_OCCUPANCY, config.KR, config.KI
    MIN_RATE, MAX_R = config.MIN_RATE, config.MAX_RATE

    # Edge Definitions 
    UPSTREAM_EDGE, MERGING_EDGE, DOWNSTREAM_EDGE, ON_RAMP_EDGE = "main_road", "acceleration_area", "end_main_road", "on_ramp"
    RAMP_ID = "ramp_meter"
    min_green, max_green = 5, CYCLE_LENGTH - 5
    V_MAX_SPEED = 35




    if config.SUMO_TOOLS is None:
        sys.exit("PLEASE DECLARE THE ENVIRONMENT VARIABLE 'SUMO_HOME'")

    sys.path.append(config.SUMO_TOOLS)  # Ensure TraCI is in the Python path

    # Select the SUMO config file
    if sumo_config_file is None:
        sumo_config_file = config.DEFAULT_SUMO_CONFIG_FILE  # Use default if not specified

    if sumo_config_file not in config.SUMO_CONFIG_FILE:
        print(f"Error: Configuration file '{sumo_config_file}' is not in the allowed set.")
        print("Allowed files are:", config.SUMO_CONFIG_FILE)
        sys.exit(1)

    # Building the command
    sumo_cmd = [config.SUMO_BINARY, "-c", sumo_config_file] #Added additional parameter

    # Add seed if provided
    if seed is not None:
        sumo_cmd.extend(["--seed", str(seed)])






    # Start SUMO with TraCI
    traci.start(sumo_cmd)



    programs = ["one_veh_per_green", "mult_veh_per_green", "alinea", "deactivated", "pi-alinea"]  # Traffic Light programs

    #ALINEA initialization
    merging_area_loops = helpers.get_edge_induction_loops(MERGING_EDGE)[:4]

    up_stream_area_loops = ['up_stream_sens_0', 'up_stream_sens_00', 'up_stream_sens_1', 
            'up_stream_sens_11', 'up_stream_sens_2', 'up_stream_sens_22']

    # Remove indices 1, 3, and 5 in reverse order
    for index in sorted([1, 3, 5], reverse=True):
        up_stream_area_loops.pop(index)
    
    

   
    
    
    r = MIN_RATE  # Initial value for r
    integral_error = 0
    sum_delay_sq_min = 0
    
    
    
    # Determine the log filename based on the TLC program
    log_filename = f"{tlc_program}_log.csv"

    # Define the CSV fieldnames.  Crucially, metering info is *only* included for ALINEA
    fieldnames = ['Step', 'Upstream Flow', 'Merging Area Flow', 'Downstream Flow', 'Upstream Occupancy', 'Merging Area Occupancy', 'Downstream Occupancy',
                  'Queue Length', 'TTTD', 'Sum Delay Sq', 'Total Waiting Time', 'Total Delay', 'Total Volume']  # Common fields
    if tlc_program in ("alinea", "pi-alinea"):
        fieldnames.extend(['Metering Rate', 'Green Time', 'Red Time'])
        
        
        
        
        
    with open(log_filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        if tlc_program in ("alinea", "pi-alinea"):

            
            for step in range(config.MAX_STEP):
                traci.simulationStep()
                

                
                upstream_ls_flow = helpers.get_loops_flow(up_stream_area_loops, 20)
                downstream_ls_flow = helpers.get_edge_flow_from_loops(DOWNSTREAM_EDGE, 20) #Get the Downstream Flow
                merging_area_ls_flow = helpers.get_loops_flow(merging_area_loops,20) #Get the Downstream Flow
                
                mergin_area_ls_occupancy = helpers.get_loops_ls_occupancy(merging_area_loops)
                downstream_ls_occupancy = helpers.get_edge_ls_occupancy_from_loops(DOWNSTREAM_EDGE)
                upstream_ls_occupancy = helpers.get_edge_ls_occupancy_from_loops(UPSTREAM_EDGE)
              
                queue_length = helpers.get_queue_length(ON_RAMP_EDGE)
                # tttd = 0,
                # sum_delay_sq = helpers.get_sum_delay_sq(RAMP_ID, V_MAX_SPEED)
                # total_waiting_time = helpers.get_total_accumulated_waiting_time(RAMP_ID)
                # total_delay = helpers.get_total_delay(RAMP_ID)
                # total_volume = helpers.get_total_volume(RAMP_ID)
                
                
                # Log every CYCLE_LENGTH steps
                if step % CYCLE_LENGTH == 0:
                    # Get common metrics
                    bottleneck_occupancy = helpers.get_loops_li_occupancy(merging_area_loops)
                    downstream_occupancy = helpers.get_edge_li_occupancy_from_loops(DOWNSTREAM_EDGE)
                    

                    # ALINEA-specific calculations and logging
                    
                    occupancy_diff = CRITICAL_OCCUPANCY - downstream_occupancy

                    if tlc_program == "alinea":
                        r = r + KR * occupancy_diff # ALINEA update
                    elif tlc_program == "pi-alinea":
                        integral_error += occupancy_diff  # Accumulate error

                        #PI controller part
                        r = r + KR * occupancy_diff + KI * integral_error #
                    r = max(MIN_RATE, min(r, MAX_R))  # Clamp metering rate

                    green_time = int(max(min_green, min((r / SATURATION_FLOW) * CYCLE_LENGTH, max_green)))
                    yellow_time = 3
                    red_time = CYCLE_LENGTH - green_time - yellow_time

                # Create the row dictionary
                                # 'Upstream Flow', 'Merging Area Flow', 'Downstream Flow',
                # 'Upstream Occupancy', 'Merging Area Occupancy', 'Downstream Occupancy',
                #   'Queue Length', 'TTTD'
                row = {
                    'Step': step,
                    'Upstream Flow': upstream_ls_flow,
                    'Merging Area Flow' : merging_area_ls_flow,
                    'Downstream Flow': downstream_ls_flow,
                    'Upstream Occupancy' : upstream_ls_occupancy,
                    'Merging Area Occupancy': mergin_area_ls_occupancy,
                    'Downstream Occupancy': downstream_ls_occupancy,
                    'Queue Length': queue_length
                    # 'TTTD': tttd,                     
                    # 'Sum Delay Sq': sum_delay_sq, #Add the Delay
                    # 'Total Waiting Time': total_waiting_time,
                    # 'Total Delay': total_delay,
                    # 'Total Volume': total_volume
                }


                row['Metering Rate'] = r
                row['Green Time'] = green_time
                row['Red Time'] = red_time

                writer.writerow(row)
                #The key here is that the "arrived vehicles" are accounted and resetted
                    

                    
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

                
                # Get common metrics
                upstream_ls_flow = helpers.get_loops_flow(up_stream_area_loops, 20)
                downstream_ls_flow = helpers.get_edge_flow_from_loops(DOWNSTREAM_EDGE, 20) #Get the Downstream Flow
                merging_area_ls_flow = helpers.get_loops_flow(merging_area_loops,20) #Get the Downstream Flow
                
                mergin_area_ls_occupancy = helpers.get_loops_ls_occupancy(merging_area_loops)
                downstream_ls_occupancy = helpers.get_edge_ls_occupancy_from_loops(DOWNSTREAM_EDGE)
                upstream_ls_occupancy = helpers.get_edge_ls_occupancy_from_loops(UPSTREAM_EDGE)
              
                queue_length = helpers.get_queue_length(ON_RAMP_EDGE)
                # tttd = 0
                # # tttd = helpers.get_total_travel_time_and_delay()
                # sum_delay_sq = helpers.get_sum_delay_sq(RAMP_ID, V_MAX_SPEED)
                # total_waiting_time = helpers.get_total_accumulated_waiting_time(RAMP_ID)
                # total_delay = helpers.get_total_delay(RAMP_ID)
                # total_volume = helpers.get_total_volume(RAMP_ID)

                    # Create the row dictionary
                row = {
                    'Step': step,
                    'Upstream Flow': upstream_ls_flow,
                    'Merging Area Flow' : merging_area_ls_flow,
                    'Downstream Flow': downstream_ls_flow,
                    'Upstream Occupancy' : upstream_ls_occupancy,
                    'Merging Area Occupancy': mergin_area_ls_occupancy,
                    'Downstream Occupancy': downstream_ls_occupancy,
                    'Queue Length': queue_length
                #     'TTTD': tttd,
                #     'Sum Delay Sq': sum_delay_sq, 
                #     'Total Waiting Time': total_waiting_time,
                #     'Total Delay': total_delay,
                #     'Total Volume': total_volume
                }



                writer.writerow(row)
                    
                step += 1 #Simulation steps

    traci.close() #Closes the simulation

def parse_arguments():
    parser = argparse.ArgumentParser(description="Run SUMO simulation with customizable parameters.")
    parser.add_argument("-c", "--sumo_config", type=str,
                        help="Path to the SUMO configuration file (.sumocfg). Must be one of: " + str(list(config.SUMO_CONFIG_FILE))) #Added default and help msgs
    parser.add_argument("-s", "--seed", type=int, default=None,
                        help="Random seed for the simulation. If not provided, SUMO will use its default behavior (usually time-based).")
    parser.add_argument("tlc_program", nargs="?", default="alinea", help="Traffic light control program to use (default: alinea)") # Add tlc_program

    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments() #Parse the arguments
    main(args.tlc_program, args.sumo_config, args.seed) #Runs the main function with the specified program
    print("simulation done")