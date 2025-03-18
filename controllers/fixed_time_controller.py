# controllers/fixed_time_controller.py
import traci

def set_fixed_time_program(traffic_light_id, program_id):
    """Sets a fixed-time traffic light program."""
    print(f"Changing traffic light {traffic_light_id} to program {program_id}")
    traci.trafficlight.setProgram(traffic_light_id, program_id)