import traci
import sumolib
import sys
from itertools import permutations


if __name__ == "__main__":
    try:
        net = sumolib.net.readNet('ramp.net.xml')
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)  # Exit to prevent errors
    tl_ids = [tl.getID() for tl in net.getTrafficLights()]
    # Print the number of edges
    print(f"Number of edges: {net.getEdges()}\n")

    # Print the type of the first node (if there are nodes)
    nodes = net.getNodes()
    if nodes:
        print(f"Type of first node: {nodes[0].getType()}")

    # Get IDs of dead-end nodes
    dead_end_nodes = [node.getID() for node in nodes if node.getType() == "dead_end"]
    print(f"Dead-end nodes: {dead_end_nodes}")

    # Get all edges and filter those originating from dead-end nodes
    start_edges = [edge.getID() for edge in net.getEdges() if edge.getFromNode().getID() in dead_end_nodes]
    print(f"Start edges from dead-end nodes: {start_edges}")
    
        # Get all edges and filter those ending to dead-end nodes
    end_edges = [edge.getID() for edge in net.getEdges() if edge.getToNode().getID() in dead_end_nodes]
    print(f"End edges from dead-end nodes: {end_edges}")

    # print("*" * 100)
    # route = {"".join(r): r for r in [
    #         [e.getID() for e in net.getShortestPath(oe, de)[0]] for (oe, de) in [
    #             (net.getNode(on).getOutgoing()[0], net.getNode(dn).getIncoming()[0]) for (on, dn) in
    #             list(permutations([n for n in [node.getID() for node in net.getNodes()] if n not in tl_ids], 2))
    #             ]]}
    # print(route)

def get_start_end_edges(net):
    nodes = net.getNodes()
    dead_end_nodes = [node.getID() for node in nodes if node.getType() == "dead_end"]
    start_edges = [edge.getID() for edge in net.getEdges() if edge.getFromNode().getID() in dead_end_nodes]
    end_edges = [edge.getID() for edge in net.getEdges() if edge.getToNode().getID() in dead_end_nodes]
    
    return start_edges, end_edges

