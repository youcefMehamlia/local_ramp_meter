import traci


def get_lanes_of_edge(edge_id):
    """
    Get all lane IDs for a given edge.
    :param edge_id: The ID of the edge.
    :return: List of lane IDs.
    """
    return [lane for lane in traci.lane.getIDList() if traci.lane.getEdgeID(lane) == edge_id]


def get_inductive_loops_of_edge(edge_id):
    """
    Get all inductive loop IDs on a given edge.
    :param edge_id: The ID of the edge.
    :return: List of loop detector IDs.
    """
    lanes = get_lanes_of_edge(edge_id)
    return [loop_id for loop_id in traci.inductionloop.getIDList() if traci.inductionloop.getLaneID(loop_id) in lanes]


def get_interval_edge_flow(edge_id):
    """
    Calculate the total vehicle flow for a given edge.
    :param edge_id: The ID of the edge.
    :return: Total vehicle flow.
    """
    loops = get_inductive_loops_of_edge(edge_id)
    if len(loops) > 4:
        loops.pop(4)  # Remove the fifth loop (index 4) if it exists
    return sum(traci.inductionloop.getIntervalVehicleNumber(loop) for loop in loops)

def get_ls_edge_flow(edge_id):
    """
    Calculate the total vehicle flow for a given edge.
    :param edge_id: The ID of the edge.
    :return: Total vehicle flow.
    """
    loops = get_inductive_loops_of_edge(edge_id)
    if len(loops) > 4:
        loops.pop(4)  # Remove the fifth loop (index 4) if it exists
    return sum(traci.inductionloop.getLastStepVehicleNumber(loop) for loop in loops)

def get_ls_occup(edge_id):
    loops = get_inductive_loops_of_edge(edge_id)
    if len(loops) > 4:
        loops.pop(4)  # Remove the fifth loop (index 4) if it exists
    total_occupancy = sum(traci.inductionloop.getLastStepOccupancy(loop) for loop in loops)
    return total_occupancy / max(len(loops), 1)
    
def get_edge_critical_occupancy(edge_id):
    """
    Calculate the critical occupancy for a given edge.
    :param edge_id: The ID of the edge.
    :return: Average critical occupancy percentage.
    """
    loops = get_inductive_loops_of_edge(edge_id)
    if len(loops) > 4:
        loops.pop(4)  # Remove the fifth loop (index 4) if it exists
    total_occupancy = sum(traci.inductionloop.getIntervalOccupancy(loop) for loop in loops)
    return total_occupancy / max(len(loops), 1)  # Avoid division by zero


if __name__ == "__main__":
    try:
        traci.start(["sumo", "-c", "ramp.sumocfg"])
        simulation_time = 3599  # seconds
        BOTTLENECK_EDGE = "acceleration_area"

        for step in range(simulation_time):
            traci.simulationStep()

        int_flow = get_interval_edge_flow(BOTTLENECK_EDGE)
        inst_flow = get_ls_edge_flow(BOTTLENECK_EDGE)
        int_occupancy = get_edge_critical_occupancy(BOTTLENECK_EDGE)
        inst_occupancy = get_ls_occup(BOTTLENECK_EDGE)
        print()
        print(f"{BOTTLENECK_EDGE} Interval Saturation Flow Rate: {int_flow:.2f} veh/hour")
        print(f"{BOTTLENECK_EDGE} Inst Saturation Flow Rate: {inst_flow:.2f} veh/hour")
        print()
        print(f"{BOTTLENECK_EDGE} Ingerval Critical occupancy: {int_occupancy:.2f} %")
        print(f"{BOTTLENECK_EDGE} Instant Critical occupancy: {inst_occupancy:.2f} %")
    
    except traci.exceptions.TraCIException as e:
        print(f"TraCI Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        try:
            traci.close()
        except:
            pass