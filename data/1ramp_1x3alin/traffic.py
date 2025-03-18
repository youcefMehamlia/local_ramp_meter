# utils/traffic_metrics.py
import traci

def get_edge_density(edge_id):
    """Calculates the density (vehicles/km) on a given edge."""
    lane_ids = traci.edge.getLaneIDs(edge_id)
    total_length = sum(traci.lane.getLength(lane_id) for lane_id in lane_ids)
    vehicle_count = traci.edge.getLastStepVehicleNumber(edge_id)

    if total_length > 0:
        density = (vehicle_count / total_length) * 1000  # Vehicles per km
    else:
        density = 0
    return density

def get_edge_flow(edge_id):
    """Calculates the flow (vehicles/hour) on a given edge."""
    return traci.edge.getLastStepVehicleNumber(edge_id) * (3600 / traci.simulation.getDeltaT())

def get_edge_occupancy(edge_id):
    """Calculates the occupancy on a given edge (ratio)."""
    return traci.edge.getLastStepOccupancy(edge_id)

def get_lane_occupancy(lane_id):
    """Calculates the occupancy on a given lane (ratio)."""
    return traci.lane.getLastStepOccupancy(lane_id)

def get_lane_mean_speed(lane_id):
  """Gets the mean speed on the lane"""
  return traci.lane.getLastStepMeanSpeed(lane_id)


def enforce_metering_rate(traffic_light_id, r_k, saturation_flow, cycle_length):
    """Calculates and sets the green time for the on-ramp traffic light."""

    green_time = (r_k / saturation_flow) * cycle_length

    # Enforce minimum and maximum green times (important for safety)
    min_green = 5 # seconds
    max_green = cycle_length - 5 # seconds (leave some time for red)
    green_time = max(min_green, min(green_time, max_green))

    # Assuming a fixed phase structure (Green-Yellow-Red)
    yellow_time = 3  # seconds
    red_time = cycle_length - green_time - yellow_time

    # Check all phase have a positive value
    if red_time < 0:
        red_time = 0
        green_time = cycle_length - yellow_time - red_time

    # Create the new phase string (SUMO requires all phases at once)
    new_phase = "G" + "y" + "r"  # Example: Green-Yellow-Red for the on-ramp

    traci.trafficlight.setRedYellowGreenState(traffic_light_id, new_phase)
