#this file is not used in the run dimulation, it was just to test the logic behind alinea

import traci
import traci.constants as tc
import csv
from utils import helpers








def run():
    # Parameters
    CYCLE_LENGTH, SATURATION_FLOW = 20, 1700
    CRITICAL_OCCUPANCY, CRITICAL_FLOW, KR = 20, 3300, 70
    SIMULATION_STEP, SIMULATION_TIME = 1, 7200
    MIN_R, MAX_R = 10, SATURATION_FLOW
    
    # Edge Definitions
    UPSTREAM_EDGE, MERGING_EDGE, DOWNSTREAM_EDGE, ON_RAMP_EDGE = "main_road", "acceleration_area", "end_main_road", "on_ramp"
    RAMP_ID = "ramp_meter"
    min_green, max_green = 5, CYCLE_LENGTH - 5
    
    
   
    

    traci.start(["sumo", "-c", "ramp.sumocfg", "--seed", "42"])


    bottleneck_loops = helpers.get_inductive_loops_of_edge(MERGING_EDGE)[:4]
    
    r = MIN_R # Initial value for r

    # Initialize phase durations
    green_time = 15
    yellow_time = 3
    red_time = CYCLE_LENGTH - green_time - yellow_time


    with open('alinea_ramp_metering_data_downsteam.csv', 'w', newline='') as csvfile:
        fieldnames = ['Step', 'Upstream Flow', 'Bottleneck Occupancy', 'Downstream Occupancy',
                    'Queue Length', 'Metering Rate', 'Green Time', 'Yellow Time', 'Red Time']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for step in range(SIMULATION_TIME):
            traci.simulationStep()

            if step % CYCLE_LENGTH == 0:  # Update every CYCLE_LENGTH steps (20 seconds)
                upstream_flow = helpers.get_edge_flow(UPSTREAM_EDGE)
                bottleneck_occupancy = helpers.get_loops_occupancy(bottleneck_loops)
                downstream_occupancy = helpers.get_edge_occupancy(DOWNSTREAM_EDGE)
                queue_length = helpers.get_queue_length(ON_RAMP_EDGE)

                occupancy_diff = CRITICAL_OCCUPANCY - downstream_occupancy
                r = r + KR * occupancy_diff
                r = max(MIN_R, min(r, MAX_R))  # Clamp metering rate

                green_time = int(max(min_green, min((r / SATURATION_FLOW) * CYCLE_LENGTH, max_green)))
                yellow_time = 3
                red_time = CYCLE_LENGTH - green_time - yellow_time

                # Writing inside the 'with' block
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

            
            
            # print(f"Step {step}: Bottleneck Occupancy={bottleneck_occupancy:.2f}, Metering Rate={r:.2f}, Green={green_time}, Yellow={yellow_time}, Red={red_time}")  # Print statement

        # Determine the traffic light phase based on the step within the cycle
        if step % CYCLE_LENGTH < green_time:
            # Green Phase
            traci.trafficlight.setRedYellowGreenState(RAMP_ID, "G")
        elif step % CYCLE_LENGTH < green_time + yellow_time:
            # Yellow Phase
            traci.trafficlight.setRedYellowGreenState(RAMP_ID, "y")
        else:
            # Red Phase
            traci.trafficlight.setRedYellowGreenState(RAMP_ID, "r")

    traci.close()


if __name__ == "__main__":
    run()