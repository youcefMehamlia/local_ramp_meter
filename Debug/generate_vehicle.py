import xml.etree.ElementTree as ET
import xml.dom.minidom

"""

**SUMO VehicleAttributes**

| Attribute Name  | Value Type                                                                                                                      | Description                                                                                                                                                                                                                                                             |
| :-------------- | :------------------------------------------------------------------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`            | `id` (string)                                                                                                                 | The name of the vehicle.                                                                                                                                                                                                                                            |
| `type`          | `id`                                                                                                                          | The id of the vehicle type to use for this vehicle.                                                                                                                                                                                                                     |
| `route`         | `id`                                                                                                                          | The id of the route the vehicle shall drive along.                                                                                                                                                                                                                      |
| `color`         | `color`                                                                                                                       | This vehicle's color.                                                                                                                                                                                                                                                 |
| `depart`        | `float (s)` or human-readable-time or one of `triggered`, `containerTriggered`, `begin`                                       | The time step at which the vehicle shall enter the network (seconds or a time string). Alternatively, the vehicle departs once a person enters or a container is loaded                                                                                                   |
| `departLane`    | `int/string` (≥0, `"random"`, `"free"`, `"allowed"`, `"best"`, `"first"`, `"best_prob"`)                                       | The lane on which the vehicle shall be inserted. `first` by default.                                                                                                                                                                                                   |
| `departPos`     | `float(m)/string` (`"random"`, `"free"`, `"random_free"`, `"base"`, `"last"`, `"stop"`, `"splitFront"`)                       | The position at which the vehicle shall enter the net. `base` by default.                                                                                                                                                                                                  |
| `departSpeed`   | `float(m/s)/string` (≥0, `"random"`, `"max"`, `"desired"`, `"speedLimit"`, `"last"`, `"avg"`)                                | The speed with which the vehicle shall enter the network. `0` by default.                                                                                                                                                                                                |
| `departEdge`    | `int` (index from `[0, routeLength[` or `"random"`                                                                            | The initial edge along the route where the vehicle should enter the network (only supported if a complete route is defined). `0` by default.                                                                                                                            |
| `arrivalLane`   | `int/string` (≥0,`"current"`)                                                                                               | The lane at which the vehicle shall leave the network. `current` by default.                                                                                                                                                                                              |
| `arrivalPos`    | `float(m)/string` (≥0(1), `"random"`, `"max"`)                                                                                 | The position at which the vehicle shall leave the network. `max` by default.                                                                                                                                                                                              |
| `arrivalSpeed`  | `float(m/s)/string` (≥0,`"current"`)                                                                                         | The speed with which the vehicle shall leave the network. `current` by default.                                                                                                                                                                                          |
| `arrivalEdge`   | `int` (index from `[0, routeLength[` or `"random"`                                                                            | The final edge along the route where the vehicle should leave the network (only supported if a complete route is defined).                                                                                                                                             |
| `line`          | `string`                                                                                                                      | A string specifying the id of a public transport line which can be used when specifying person rides.                                                                                                                                                                      |
| `personNumber`  | `int` (in `[0,personCapacity]`)                                                                                             | The number of occupied seats when the vehicle is inserted. `0` by default.                                                                                                                                                                                              |
| `containerNumber` | `int` (in `[0,containerCapacity]`)                                                                                           | The number of occupied container places when the vehicle is inserted. `0` by default.                                                                                                                                                                                          |
| `reroute`       | `bool`                                                                                                                        | Whether the vehicle should be equipped with a rerouting device (setting this to false does not take precedence over other assignment options).                                                                                                                              |
| `via`           | `id list`                                                                                                                     | List of intermediate edges that shall be passed on rerouting. Note: when `via` is not set, any `<stop>` elements that belong to this route will automatically be used as intermediate edges. Otherwise, `via` takes precedence.                                     |
| `departPosLat`  | `float(m)/string` (`"random"`, `"free"`, `"random_free"`, `"left"`, `"right"`, `"center"`)                                     | The lateral position on the departure lane at which the vehicle shall enter the net; see Simulation/SublaneModel. `center` by default.                                                                                                                                     |
| `arrivalPosLat` | `float(m)/string` (`"default"`, `"left"`, `"right"`, `"center"`)                                                                | The lateral position on the arrival lane at which the vehicle shall arrive; see Simulation/SublaneModel. By default, the vehicle does not care about lateral arrival position.                                                                                             |
| `speedFactor`   | `float > 0`                                                                                                                   | Sets custom speedFactor (factor on road speed limit) and overrides the speedFactor distribution of the vehicle type.                                                                                                                                                        |
| `insertionChecks` | `string list`                                                                                                                | Sets the list of safety checks to perform during vehicle insertion. Possible values are: `all`, `none`, `collision`, `leaderGap`, `followerGap`, `junction`, `stop`, `arrivalSpeed`, `oncomingTrain`, `speedLimit`, `pedestrian`. `all` by default.                      |
| `parkingBadges` | `string list`                                                                                                                | List of keywords to access restricted parking areas (the default empty list will still allow access to unrestricted parking areas).                                                                                                                                      |


"""


"""
**SUMO Flow Attributes (Repeated Vehicles)**

| Attribute Name | Value Type                                                                             | Description                                                                                                                                                                                                                                |
| :------------- | :------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `begin`        | `float (s)` or human-readable-time or one of `triggered`, `containerTriggered`        | The first vehicle departure time (in simulation seconds or a time string).                                                                                                                                                               |
| `end`          | `float(s)`                                                                            | End of departure interval (in simulation seconds). If undefined, defaults to 24 hours.                                                                                                                                                   |
| `vehsPerHour`  | `float(#/h)`                                                                          | Number of vehicles per hour, equally spaced (cannot be used together with `period` or `probability`).                                                                                                                                      |
| `period`       | `float(s)` or `"exp(X)"` (where X is float)                                             | If `float` is given, insert equally spaced vehicles at that period (in seconds). If `"exp(X)"` is given, insert vehicles with exponentially distributed time gaps. See also [Simulation/Randomness](Simulation/Randomness). Cannot be used together with `vehsPerHour` or `probability`. |
| `probability`  | `float` (`[0,1]`)                                                                     | Probability for emitting a vehicle each second (cannot be used together with `vehsPerHour` or `period`). See also [Simulation/Randomness](Simulation/Randomness).                                                                        |
| `number`       | `int(#)`                                                                               | Total number of vehicles, equally spaced.                                                                                                                                                                                                  |


"""




def create_route_file_from_dict(output_file, vehicle_types_data, total_vehicles, route_id="default_route", begin_time=0, end_time=3600, depart_lane="random"):
    """
    Creates a SUMO .rou.xml file based on user-defined vehicle types and percentages.

    Args:
        output_file (str): Path to the output .rou.xml file.
        vehicle_types_data (dict): A dictionary defining vehicle types and their percentages.
                                    Example:
                                    {
                                        "car": {"percentage": 80, "maxSpeed": 40, "length": 5, "maxAccel": 2.6, "maxDecel": 4.5, "speedFactor": 1.0, "sigma": 0.5, "guiShape": "passenger"},
                                        "truck": {"percentage": 15, "maxSpeed": 30, "length": 12, "maxAccel": 1.5, "maxDecel": 3.0, "speedFactor": 0.8, "sigma": 0.8, "guiShape": "truck"},
                                        "bus": {"percentage": 5, "maxSpeed": 35, "length": 10, "maxAccel": 1.8, "maxDecel": 3.5, "speedFactor": 0.9, "sigma": 0.6, "guiShape": "bus"},
                                    }
        total_vehicles (int): The total number of vehicles to generate for the simulation.
        route_id (str): The id of the route in the .net file for every vehicle.
        begin_time (int or float): Simulation begin time for every vehicle.
        end_time (int or float): Simulation end time for every vehicle.
        depart_lane (str): The lane assignment method for the vehicles ("random" or a lane number).
    """

    # Validate Input
    if not isinstance(vehicle_types_data, dict):
        raise ValueError("vehicle_types_data must be a dictionary")
    if not all("percentage" in data for data in vehicle_types_data.values()):
        raise ValueError("All vehicle types must have a 'percentage' key")

    # Calculate number of vehicles for each type
    vehicle_counts = {}
    remaining_vehicles = total_vehicles  # Keep track of rounding errors
    for vtype, data in vehicle_types_data.items():
        percentage = data["percentage"] / 100.0  # Convert percentage to decimal
        count = int(total_vehicles * percentage)  # Integer number of vehicles
        vehicle_counts[vtype] = count
        remaining_vehicles -= count

    # Distribute Remaining Vehicles (Handle Rounding Errors)
    if remaining_vehicles > 0:
        # Assign the remaining vehicles to the first vehicle type
        first_vtype = next(iter(vehicle_types_data))  # Get the first key
        vehicle_counts[first_vtype] += remaining_vehicles

    # Create XML Structure
    routes_xml = ET.Element("routes")
    routes_xml.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
    routes_xml.set("xsi:noNamespaceSchemaLocation", "http://sumo.dlr.de/xsd/routes_file.xsd")

    # Add Vehicle Type Definitions
    for vtype, data in vehicle_types_data.items():
        vtype_element = ET.SubElement(routes_xml, "vType", id=vtype)
        for attr, value in data.items():
            if attr != "percentage":  # Don't include percentage in vType definition
                vtype_element.set(attr, str(value))

    # Add the road id for which the defined road will go through
    road_id_element = ET.SubElement(routes_xml, "route", id=route_id, edges="main_road acceleration_area E3")

    # Add Vehicle Flows
    for vtype, count in vehicle_counts.items():
        flow_id = f"{vtype}_flow"
        flow_element = ET.SubElement(routes_xml, "flow", id=flow_id, type=vtype, begin=str(begin_time), end=str(end_time), vehsPerHour=str(count), route=route_id, departLane=depart_lane)

    # Write XML File (using prettify_xml for cross-version compatibility)
    rough_string = ET.tostring(routes_xml, 'utf-8')
    reparsed = xml.dom.minidom.parseString(rough_string)
    pretty_xml = reparsed.toprettyxml(indent="    ")

    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(pretty_xml)
        print(f"Successfully generated {output_file}")
    except Exception as e:
        print(f"Error: Failed to write to route file: {output_file}. {e}")


# Example Usage
if __name__ == "__main__":
    vehicle_types = {
        "car": {"percentage": 80, "maxSpeed": 40, "length": 5, "maxAccel": 2.6, "maxDecel": 4.5, "speedFactor": 1.0, "sigma": 0.5, "guiShape": "passenger"},
        "truck": {"percentage": 15, "maxSpeed": 30, "length": 12, "maxAccel": 1.5, "maxDecel": 3.0, "speedFactor": 0.8, "sigma": 0.8, "guiShape": "truck"},
        "bus": {"percentage": 5, "maxSpeed": 35, "length": 10, "maxAccel": 1.8, "maxDecel": 3.5, "speedFactor": 0.9, "sigma": 0.6, "guiShape": "bus"},
    }
    output_file = "generated_routes.rou.xml"
    create_route_file_from_dict(output_file, vehicle_types, total_vehicles=50000, route_id="test")