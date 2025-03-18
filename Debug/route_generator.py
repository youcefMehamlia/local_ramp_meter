import xml.etree.ElementTree as ET
import xml.dom.minidom
import sumolib  # Import sumolib

def prettify_xml(elem):
    """Return a pretty-printed XML string for the Element."""
    rough_string = ET.tostring(elem, encoding='utf-8', method='xml')
    reparsed = xml.dom.minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="    ")

def get_start_end_edges(net):
    """
    Identifies start and end edges based on dead-end junctions.
    """
    nodes = net.getNodes()
    dead_end_nodes = [node.getID() for node in nodes if node.getType() == "dead_end"]
    start_edges = [edge.getID() for edge in net.getEdges() if edge.getFromNode().getID() in dead_end_nodes]
    end_edges = [edge.getID() for edge in net.getEdges() if edge.getToNode().getID() in dead_end_nodes]

    return start_edges, end_edges

def generate_all_paths(net_file, output_file):
    """
    Generates all possible paths in a SUMO network using sumolib and Dijkstra,
    considering permissible connections, and creates a .rou.xml file with
    <route> definitions. Only creates routes between start and end edges.

    Args:
        net_file (str): Path to the SUMO .net.xml network file.
        output_file (str): Path to the output .rou.xml file.
    """

    # 1. Load the Network with sumolib
    try:
        net = sumolib.net.readNet(net_file)
    except FileNotFoundError:
        print(f"Error: Network file not found: {net_file}")
        return
    except Exception as e:
        print(f"Error: Failed to read network file with sumolib: {net_file}. {e}")
        return

    # 2. Build Adjacency List for Dijkstra (using sumolib's edges and connections)
    graph = {}  # {node_id: [(neighbor_node_id, edge_id), ...]}
    for node in net.getNodes():
        graph[node.getID()] = []

    for edge in net.getEdges():
        from_node = edge.getFromNode().getID()
        to_node = edge.getToNode().getID()
        graph[from_node].append((to_node, edge.getID()))

    # 3. Dijkstra's Algorithm (Basic Implementation - Can be Optimized)
    def dijkstra(start, end):
        """Finds the shortest path from start to end using Dijkstra's algorithm.
           Returns (distance, path_edges) or (float('inf'), []) if no path exists.
        """
        distances = {node: float('inf') for node in graph}
        paths = {node: [] for node in graph}
        distances[start] = 0
        unvisited = set(graph)

        while unvisited:
            current = min(unvisited, key=distances.get)
            if distances[current] == float('inf'): # no path exists
                break
            unvisited.remove(current)

            for neighbor, edge_id in graph[current]:
                new_distance = distances[current] + 1  # Assuming each edge has a cost of 1
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    paths[neighbor] = paths[current] + [edge_id] # Accumulate edge IDs

        return distances[end], paths[end]


    # 4. Identify Start and End Edges
    start_edges, end_edges = get_start_end_edges(net)

    # 5. Generate Routes
    routes_xml = ET.Element("routes")
    route_count = 0

    # Iterate over only permissible start and end edges
    for start_edge_id in start_edges:
        start_edge = net.getEdge(start_edge_id)
        start_node = start_edge.getFromNode().getID()

        for end_edge_id in end_edges:
            end_edge = net.getEdge(end_edge_id)
            end_node = end_edge.getToNode().getID()

            # Find shortest path with Dijkstra
            distance, edge_path = dijkstra(start_node, end_node)

            # Exclude routes that start and end at the same edge and contain the edge
            # and Only create routes for valid paths
            if (distance != float('inf') and
                edge_path and
                not (start_edge_id == end_edge_id and len(edge_path) == 1 and edge_path[0] == start_edge_id)): #Avoid routes made of itself
                route_name = f"{start_edge_id}_to_{end_edge_id}"
                edges_str = " ".join(edge_path)
                route = ET.SubElement(routes_xml, "route", id=route_name, edges=edges_str)
                route_count += 1

    # 6. Write .rou.xml File
    pretty_xml = prettify_xml(routes_xml)

    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(pretty_xml)

        print(f"Successfully generated {output_file} with {route_count} routes.")
    except Exception as e:
        print(f"Error: Failed to write to route file: {output_file}. {e}")


# Example Usage (Replace with your actual file paths)
if __name__ == "__main__":
    network_file = "ramp.net.xml"
    routes_file = "all_routes.rou.xml"
    generate_all_paths(network_file, routes_file)