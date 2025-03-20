# utils/traffic_metrics.py
import traci
import csv

def get_lane_mean_speed(lane_id):
  """Gets the mean speed on the lane"""
  return traci.lane.getLastStepMeanSpeed(lane_id)


def get_lanes_of_edge(edge_id):
    """Get all lane IDs for a given edge."""
    return [lane for lane in traci.lane.getIDList() if traci.lane.getEdgeID(lane) == edge_id]


def get_edge_induction_loops(edge_id):
    """Get all inductive loop IDs on a given edge."""
    lanes = get_lanes_of_edge(edge_id)
    return [loop_id for loop_id in traci.inductionloop.getIDList() if traci.inductionloop.getLaneID(loop_id) in lanes]



def get_loops_flow(loops, interval):
    """Calculate total vehicle flow in an iterval for a given edge."""
    #flow is in veh/h
    return (sum(traci.inductionloop.getIntervalVehicleNumber(loop) for loop in loops)*3600)/interval

def get_edge_flow_from_loops(edge_id, interval):
    """Calculate total vehicle flow in an iterval for a given edge."""
    loops = get_edge_induction_loops(edge_id)
    return (sum(traci.inductionloop.getIntervalVehicleNumber(loop) for loop in loops)*3600)/interval






def get_ls_edge_occupancy(edge_id):
    """Calculate average occupancy for a given edge."""

    return traci.edge.getLastStepOccupancy(edgeID=edge_id)  # Avoid division by zero

def get_edge_li_occupancy_from_loops(edge_id):
    """Calculate average occupancy for a given edge."""
    loops = get_edge_induction_loops(edge_id)

    if not loops:
        return 0  # Handle case where there are no loops on the edge
    else:
         total_occupancy = sum(traci.inductionloop.getLastIntervalOccupancy(loop) for loop in loops)
    return total_occupancy / max(len(loops), 1)  # Avoid division by zero

def get_edge_ls_occupancy_from_loops(edge_id):
    """Calculate average occupancy for a given edge."""
    loops = get_edge_induction_loops(edge_id)

    if not loops:
        return 0  # Handle case where there are no loops on the edge
    else:
         total_occupancy = sum(traci.inductionloop.getLastStepOccupancy(loop) for loop in loops)
    return total_occupancy / max(len(loops), 1)  # Avoid division by zero

def get_loops_li_occupancy(loops):
    """Calculate average occupancy for a given edge."""
    if not loops:
        return 0  # Handle case where there are no loops on the edge
    else:
        total_occupancy = sum(traci.inductionloop.getLastIntervalOccupancy(loop) for loop in loops)
    return total_occupancy / max(len(loops), 1)  # Avoid division by zero

def get_loops_ls_occupancy(loops):
    """Calculate average occupancy for a given edge."""
    if not loops:
        return 0  # Handle case where there are no loops on the edge
    else:
        total_occupancy = sum(traci.inductionloop.getLastStepOccupancy(loop) for loop in loops)
    return total_occupancy / max(len(loops), 1)  # Avoid division by zero




def get_queue_length(edge_id):
    return traci.edge.getLastStepVehicleNumber(edge_id)



#to be reviewed

# #TTS

# def get_n_veh_insersted():
#     return len(traci.vehicle.getIDList())

# def get_n_veh_waiting():
#     return sum(1 for v in traci.vehicle.getIDList() if traci.vehicle.getWaitingTime(v) > 0)

# def get_trip_duration():
#     return sum(traci.vehicle.getAccumulatedWaitingTime(v) for v in traci.vehicle.getIDList())

# def get_depart_delay():
#     return sum(traci.vehicle.getDepartDelay(v) for v in traci.vehicle.getIDList())

# def get_depart_delay_waiting_time():
#     return sum(traci.vehicle.getWaitingTime(v) for v in traci.vehicle.getIDList())

# def get_vehicle_statistics():
#     """Retrieve the necessary statistics from SUMO via TraCI."""
#     inserted = get_n_veh_insersted()  # Number of inserted vehicles
#     waiting =  get_n_veh_waiting()
#     total_duration = get_trip_duration()
#     total_depart_delay = get_depart_delay()
#     total_depart_delay_waiting = get_depart_delay_waiting_time()
    
#     return inserted, waiting, total_duration, total_depart_delay, total_depart_delay_waiting

# def get_total_travel_time_and_delay(inserted, waiting, duration, depart_delay, depart_delay_waiting):
#     return (inserted * (duration + depart_delay)) + (waiting * depart_delay_waiting)



# # TTT
# # Global variables to track vehicle statistics

# vehicle_data = {}  # Dictionary to store data for each vehicle


# def reset_vehicle_data():  
#     """Resets the vehicle_data dictionary to start collecting data for a new cycle."""
#     global vehicle_data
#     vehicle_data = {}  # clear vehicle data
#     # print("Vehicle data reset.")



# def get_total_travel_time(cycle_length):  # Add the parameter Cycle Length to be able to calculate it
#     """
#     Calculate the total travel time for vehicles arriving during the last cycle.
#     """
#     global vehicle_data

#     total_travel_time = 0.0
#     num_arrived_vehicles = 0  # Add the number of arrived Vehicles
#     current_time = traci.simulation.getTime()  # gets the time


#     # Collect data for new departed vehicles and record their depart time
#     departed_vehicles = traci.simulation.getDepartedIDList()
#     for veh_id in departed_vehicles:
#         if veh_id not in vehicle_data:  # Check if vehicle is already tracked
#             vehicle_data[veh_id] = {
#                 'depart_time': current_time,
#                 'route_length': 0.0,  # Initialize the Route len
#                 'arrived': False  # To know when the car arrived
#             }

#     # get Arrived vehicles from the last cycle to calculate
#     arrived_vehicles = traci.simulation.getArrivedIDList()
#     for veh_id in arrived_vehicles:
#         if veh_id in vehicle_data:  # If the car is in the Data
#             if not vehicle_data[veh_id]['arrived']:  # Check if already marked as arrived
#                 vehicle_data[veh_id]['arrive_time'] = current_time  # Add the value
#                 vehicle_data[veh_id]['arrived'] = True  # Arrived the value

#                 #Calculate travel time only for vehicles arriving in this cycle.
#                 total_travel_time += (vehicle_data[veh_id]['arrive_time'] - vehicle_data[veh_id]['depart_time'])
#                 num_arrived_vehicles += 1




#     return total_travel_time, num_arrived_vehicles  # returns the time, an returns the number of arrived vehicles







# def get_veh_speed(veh_id):
#     """Return the speed of a vehicle."""
#     return traci.vehicle.getSpeed(veh_id) #Used getSpeed method, for the speed
    
# def get_veh_delay_sq(veh_id, v_max_speed):
#     """Calculate the squared delay for a vehicle."""
#     speed = get_veh_speed(veh_id)
#     return 1 - pow((speed / v_max_speed), 2) #pow calculates power

# def yield_tl_vehs(tl_id): #Changed function name
#     """Yield vehicle IDs approaching a traffic light."""
#     incoming_lanes = get_tl_incoming_lanes(tl_id)
#     for lane_id in incoming_lanes:
#         for veh_id in get_lane_veh_ids(lane_id):
#             yield veh_id

# def get_tl_incoming_lanes(tl_id):
#     """Return a list of incoming lane IDs for a given traffic light."""
#     return traci.trafficlight.getControlledLanes(tl_id) #Used getControlledLanes

# def get_sum_delay_sq(tl_id, v_max_speed):
#     """Calculate the sum of squared delays for vehicles approaching a traffic light."""
#     sum_delay = 0

#     for veh_id in yield_tl_vehs(tl_id):
#         sum_delay += get_veh_delay_sq(veh_id, v_max_speed)

#     return sum_delay

# # New KPI Functions
# def get_total_accumulated_waiting_time(tl_id):
#     """Calculate the total accumulated waiting time for all incoming vehicles to a traffic light."""
#     total_waiting_time = 0
#     for veh_id in yield_tl_vehs(tl_id): #for every car
#         total_waiting_time += traci.vehicle.getAccumulatedWaitingTime(veh_id) #sums all waiting times

#     return total_waiting_time

# def get_total_delay(tl_id):
#     """Calculate the total delay for all incoming vehicles to a traffic light."""
#     total_delay = 0
#     for veh_id in yield_tl_vehs(tl_id): #for every car
#         total_delay += traci.vehicle.getDepartureDelay(veh_id) #Sum every Deperture delay,

#     return total_delay #returns value

# def get_total_queue_length(tl_id):
#     """Calculate the total queue length for all incoming vehicles to a traffic light."""
#     total_queue_length = 0
#     for lane_id in get_tl_incoming_lanes(tl_id): #For every lane
#         total_queue_length += get_queue_length(lane_id) #Adds to queue len

#     return total_queue_length #returns value

# def get_total_volume(tl_id):
#     """Calculate the total volume (number) of incoming vehicles to a traffic light."""
#     total_volume = 0
#     for lane_id in get_tl_incoming_lanes(tl_id): #for every lane
#         total_volume += len(get_lane_veh_ids(lane_id)) #Adds amount to len
#     return total_volume #returns value
