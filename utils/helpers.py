# utils/traffic_metrics.py
import traci
import csv


def get_lane_mean_speed(lane_id):
  """Gets the mean speed on the lane"""
  return traci.lane.getLastStepMeanSpeed(lane_id)


def get_lanes_of_edge(edge_id):
    """Get all lane IDs for a given edge."""
    return [lane for lane in traci.lane.getIDList() if traci.lane.getEdgeID(lane) == edge_id]


def get_inductive_loops_of_edge(edge_id):
    """Get all inductive loop IDs on a given edge."""
    lanes = get_lanes_of_edge(edge_id)
    return [loop_id for loop_id in traci.inductionloop.getIDList() if traci.inductionloop.getLaneID(loop_id) in lanes]

def get_edge_flow(edge_id):
    """Calculate total vehicle flow for a given edge."""
    loops = get_inductive_loops_of_edge(edge_id)
    return sum(traci.inductionloop.getIntervalVehicleNumber(loop) for loop in loops)

def get_edge_occupancy(edge_id):
    """Calculate average occupancy for a given edge."""
    loops = get_inductive_loops_of_edge(edge_id)

    if not loops:
        return 0  # Handle case where there are no loops on the edge
    else:
         total_occupancy = sum(traci.inductionloop.getIntervalOccupancy(loop) for loop in loops)
    return total_occupancy / max(len(loops), 1)  # Avoid division by zero


def get_loops_occupancy(loop_list):
    """Calculate average occupancy for a given edge."""


    total_occupancy = sum(traci.inductionloop.getIntervalOccupancy(loop) for loop in loop_list)
    return total_occupancy / max(len(loop_list), 1)  # Avoid division by zero


def get_queue_length(edge_id):
    return traci.edge.getLastStepVehicleNumber(edge_id)


def write_strategy_data_to_csv(filename, data):
    """Writes data to a CSV file."""
    fieldnames = ['Step', 'Upstream Flow', 'Bottleneck Occupancy', 'Downstream Occupancy', 'Queue Length', 'Cycle TTS']  # ADDED Cycle TTS
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data) # Write all rows at once
        
def calculate_tts(depart_times, arrive_times):
    """Calculates the Total Travel Time (TTS) in seconds."""
    total_travel_time = 0
    for veh_id, depart_time in depart_times.items():
        if veh_id in arrive_times:
            total_travel_time += arrive_times[veh_id] - depart_time
    return total_travel_time



#TTS
def get_vehicle_statistics():
    """Retrieve the necessary statistics from SUMO via TraCI."""
    inserted = len(traci.vehicle.getIDList())  # Number of inserted vehicles
    waiting = sum(1 for v in traci.vehicle.getIDList() if traci.vehicle.getWaitingTime(v) > 0)  # Vehicles waiting

    total_duration = sum(traci.vehicle.getAccumulatedWaitingTime(v) for v in traci.vehicle.getIDList())  # Trip duration
    total_depart_delay = sum(traci.vehicle.getDepartDelay(v) for v in traci.vehicle.getIDList())  # Depart delay
    total_depart_delay_waiting = sum(traci.vehicle.getWaitingTime(v) for v in traci.vehicle.getIDList())  # Depart delay for waiting vehicles
    
    return inserted, waiting, total_duration, total_depart_delay, total_depart_delay_waiting

def get_n_veh_insersted():
    return len(traci.vehicle.getIDList())

def get_n_veh_waiting():
    return sum(1 for v in traci.vehicle.getIDList() if traci.vehicle.getWaitingTime(v) > 0)

def get_trip_duration():
    return sum(traci.vehicle.getAccumulatedWaitingTime(v) for v in traci.vehicle.getIDList())

def get_depart_delay():
    return sum(traci.vehicle.getDepartDelay(v) for v in traci.vehicle.getIDList())

def get_depart_delay_waiting_time():
    return sum(traci.vehicle.getWaitingTime(v) for v in traci.vehicle.getIDList())

def get_vehicle_statistics():
    """Retrieve the necessary statistics from SUMO via TraCI."""
    inserted = get_n_veh_insersted()  # Number of inserted vehicles
    waiting =  get_n_veh_waiting()
    total_duration = get_trip_duration()
    total_depart_delay = get_depart_delay()
    total_depart_delay_waiting = get_depart_delay_waiting_time()
    
    return inserted, waiting, total_duration, total_depart_delay, total_depart_delay_waiting

def get_total_travel_time_and_delay(inserted, waiting, duration, depart_delay, depart_delay_waiting):
    return (inserted * (duration + depart_delay)) + (waiting * depart_delay_waiting)
