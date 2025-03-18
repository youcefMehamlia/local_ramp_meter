TARGET_OCCUPANCY = 0.2 # Occupancy as a ratio (0.0 - 1.0)
REGULATION_PARAMETER = 30  # Adjust for desired responsiveness
CYCLE_TIME = 20  # seconds

# Sensor and traffic light IDs (replace with your actual IDs)
DOWNSTREAM_EDGE_ID = "acceleration_area"  # Mainstream edge after the merge
RAMP_METER_ID = "ramp_meter"
GREEN_PHASE_INDEX = 0  # Index of the green phase in your traffic light program
RED_PHASE_INDEX = 1    # Index of the red phase
# Function to get the maximum speed of the traffic light

def alinea_control(target_occupancy, regulation_parameter, cycle_time, downstream_edge_id, ramp_meter_id, green_phase_index, red_phase_index):
    """Implements the ALINEA ramp metering algorithm."""

    current_occupancy = traci.edge.getLastStepOccupancy(downstream_edge_id)
    print(f"DEBUG: current_occupancy: {current_occupancy:.2f}")


    current_green_duration = traci.trafficlight.getPhaseDuration(ramp_meter_id) #get the phase duration


    # Calculate new green duration.  Clamp to valid range.
    delta_green = regulation_parameter * (target_occupancy - current_occupancy)
    new_green_duration =  current_green_duration + delta_green

    new_green_duration = max(2, min(new_green_duration, cycle_time - 2))

    # Set phase duration
    phases = traci.trafficlight.getProgram(ramp_meter_id) #Get the program

    programs = ["one_veh_per_green", "mult_veh_per_green", "alinea"] #define programs

    current_state = traci.trafficlight.getPhaseName(ramp_meter_id) #get the current phase
    print(f"DEBUG: current_state: {current_state}")
    traci.trafficlight.setPhaseDuration(ramp_meter_id, new_green_duration) #change the current state duration, which should be the same as the one of the duration of phase

    print(f"DEBUG: new_green_duration : {new_green_duration:.2f}")
