import traci


def get_lanes_of_edge(edge_id):
    """
    Get all lane IDs for a given edge.
    :param edge_id: The ID of the edge.
    :return: List of lane IDs.
    """
    lanes = [lane for lane in traci.lane.getIDList() if traci.lane.getEdgeID(lane) == edge_id]
    print(f"Lanes for edge {edge_id}: {lanes}")
    return lanes


def get_inductive_loops_of_edge(edge_id):
    """
    Get all inductive loop IDs on a given edge.
    :param edge_id: The ID of the edge.
    :return: List of loop detector IDs.
    """
    lanes = get_lanes_of_edge(edge_id)
    loops = [loop_id for loop_id in traci.inductionloop.getIDList() if traci.inductionloop.getLaneID(loop_id) in lanes]
    print(f"Inductive loops for edge {edge_id}: {loops}")
    return loops


def get_interval_edge_flow(edge_id):
    """
    Calculate the total vehicle flow rate (veh/hour) for a given edge using interval data.
    :param edge_id: The ID of the edge.
    :return: Total vehicle flow rate (veh/hour).
    """
    loops = get_inductive_loops_of_edge(edge_id)
    if len(loops) > 4:
        loops = loops[:4]
    
    total_flow_per_interval = sum(traci.inductionloop.getIntervalVehicleNumber(loop) for loop in loops)
    flow_rate_per_hour = total_flow_per_interval   # Convert vehicles/interval to vehicles/hour
    print(f"Interval flow rate calculation using loops {loops}: {flow_rate_per_hour} veh/hour")
    return flow_rate_per_hour


def get_ls_edge_flow(edge_id):
    """
    Calculate an approximate instantaneous flow rate (veh/hour) for a given edge using last step data.
    :param edge_id: The ID of the edge.
    :return: Approximate instantaneous vehicle flow rate (veh/hour).
    """
    loops = get_inductive_loops_of_edge(edge_id)
    if len(loops) > 4:
        loops = loops[:4]
    
    total_vehicles_last_step = sum(traci.inductionloop.getLastStepVehicleNumber(loop) for loop in loops)
    step_length = traci.simulation.getDeltaT()  # Get the simulation step length in seconds

    # Approximate flow rate: (vehicles in last step) / (step length in hours)
    flow_rate_per_hour = (total_vehicles_last_step / step_length) * 3600 if step_length > 0 else 0
    print(f"Last step flow rate calculation using loops {loops}: {flow_rate_per_hour} veh/hour")
    return flow_rate_per_hour

def get_ls_occup(edge_id):
    """
    Calculate the average occupancy for a given edge using last step data.
    :param edge_id: The ID of the edge.
    :return: Average occupancy percentage.
    """
    loops = get_inductive_loops_of_edge(edge_id)
    num_loops = len(loops)
    print(f"Number of loops before filtering: {num_loops}")
    if len(loops) > 4:
        loops = loops[:4]  # Keep only the first four loops
        print(f"Filtered loops to: {loops}")
    
    total_occupancy = sum(traci.inductionloop.getLastStepOccupancy(loop) for loop in loops)
    num_loops_used = len(loops)
    average_occupancy = total_occupancy / max(num_loops_used, 1)
    print(f"Last step occupancy calculation using loops {loops}: total occupancy = {total_occupancy}, average occupancy = {average_occupancy}")
    return average_occupancy


def get_edge_critical_occupancy(edge_id):
    """
    Calculate the average occupancy for a given edge using interval data.
    :param edge_id: The ID of the edge.
    :return: Average occupancy percentage.
    """
    loops = get_inductive_loops_of_edge(edge_id)
    num_loops = len(loops)
    print(f"Number of loops before filtering: {num_loops}")
    if len(loops) > 4:
        loops = loops[:4]  # Keep only the first four loops
        print(f"Filtered loops to: {loops}")
    total_occupancy = sum(traci.inductionloop.getIntervalOccupancy(loop) for loop in loops)
    num_loops_used = len(loops)
    average_occupancy = total_occupancy / max(num_loops_used, 1)
    print(f"Interval occupancy calculation using loops {loops}: total occupancy = {total_occupancy}, average occupancy = {average_occupancy}")
    return average_occupancy







vehicle_data = {}  # Dictionary to store data for each vehicle

mainline_edges = ["off_ramp_up_stream", "main_road", "acceleration_area", "end_main_road"]
vehicle_types = None  # Track all vehicle types
data_collection_interval = 1200  # Every simulation step
step_length = 1.0  # Assuming 1 second step length (check your .sumocfg file)


def calculate_mainline_travel_time():
    """Calculates the average mainline travel time for vehicles."""
    global vehicle_data
    total_travel_time = 0.0
    num_vehicles_completed = 0

    for veh_id, data in vehicle_data.items():
        if data["has_entered"] and data["has_exited"]:
            travel_time = data["exit_time"] - data["entry_time"]
            total_travel_time += travel_time
            num_vehicles_completed += 1
            del vehicle_data[veh_id]  # Remove completed vehicle

    if num_vehicles_completed > 0:
        average_travel_time = total_travel_time / num_vehicles_completed
        return average_travel_time
    else:
        return None  # No vehicles completed the route


if __name__ == "__main__":
    try:
        traci.start(["sumo", "-c", "ramp.sumocfg"])  # Replace "ramp.sumocfg"
        simulation_time = 1200  # seconds (2 hours)
        travel_times = []  #collect all the travel times

        for step in range(simulation_time):
            traci.simulationStep()

            if step % data_collection_interval == 0:
                # 1. Handle departing vehicles
                departed_vehicles = traci.simulation.getDepartedIDList()
                for veh_id in departed_vehicles:
                    vehicle_data[veh_id] = {
                        "entry_time": None,
                        "exit_time": None,
                        "has_entered": False,
                        "has_exited": False,
                    }

                # 2. Track vehicles on the mainline
                for veh_id in list(vehicle_data.keys()):  # Iterate over a copy
                    if veh_id in traci.vehicle.getIDList():  #Check if vehicle still exists
                        current_edge = traci.vehicle.getRoadID(veh_id)

                        # Check for entry to the mainline
                        if (
                            not vehicle_data[veh_id]["has_entered"]
                            and current_edge == mainline_edges[0]
                        ):
                            vehicle_data[veh_id]["entry_time"] = traci.simulation.getTime()
                            vehicle_data[veh_id]["has_entered"] = True

                        # Check for exit from the mainline
                        if vehicle_data[veh_id]["has_entered"] and current_edge not in mainline_edges:
                            vehicle_data[veh_id]["exit_time"] = traci.simulation.getTime()
                            vehicle_data[veh_id]["has_exited"] = True

                            #Calculate and print the travel time.
                            travel_time = vehicle_data[veh_id]["exit_time"] - vehicle_data[veh_id]["entry_time"]
                            travel_times.append(travel_time)
                            # print(travel_time)
                            # print(travel_times)

                        #Remove the old ones from ram
                        if vehicle_data[veh_id]["has_exited"]:
                            del vehicle_data[veh_id]
        #post analysis
        if travel_times:
            average_travel_time = sum(travel_times) / len(travel_times)
            print("Average Mainline Travel Time: {:.2f} seconds".format(average_travel_time))
        else:
            print("No vehicles completed the mainline route during the simulation.")

    except traci.exceptions.TraCIException as e:
        print(f"TraCI Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        try:
            traci.close()
        except:
            pass