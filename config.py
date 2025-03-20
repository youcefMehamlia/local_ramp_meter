# config.py
import os

#SUMO configuration
MAX_STEP = 7200
SUMO_BINARY = "sumo-gui"  # Use "sumo" for command-line only
# SUMO_BINARY = "sumo"  # Use "sumo" for command-line only
SUMO_CONFIG_FILE = {"data/1ramp_1x3/ramp.sumocfg",
                    "data/1ramp_2x1x3/ramp.sumocfg",
                    "data/1ramp_2x2x3/ramp.sumocfg"}
DEFAULT_SUMO_CONFIG_FILE = "data/1ramp_1x3/ramp.sumocfg"

SIMULATION_SPEED = 80
SIMULATION_MODE = "real world"

# Edge Definitions 
UPSTREAM_EDGE, MERGING_EDGE, DOWNSTREAM_EDGE, ON_RAMP_EDGE = "main_road", "acceleration_area", "end_main_road", "on_ramp"
RAMP_ID = "ramp_meter"

# Sensor and traffic light IDs (replace with your actual IDs)
DOWNSTREAM_EDGE_ID = "acceleration_area"  # Mainstream edge after the merge
RAMP_METER_ID = "ramp_meter"
UPSTREAM_EDGE_ID = "main_road" # Example upstream edge
ONRAMP_LANE_ID_0 = "on_ramp_0" # Example onramp lane



# Thresholds for turning the traffic light off (example)
DENSITY_THRESHOLD = 20
FLOW_THRESHOLD = 500



# ALINEA parameters (example)
CYCLE_LENGTH, SATURATION_FLOW = 20, 1700
CRITICAL_OCCUPANCY, KR, KI = 20, 70, 4
MIN_RATE, MAX_RATE = 10, SATURATION_FLOW



if "SUMO_HOME" in os.environ:
    SUMO_TOOLS = os.path.join(os.environ['SUMO_HOME'], 'tools')
else:
    SUMO_TOOLS = None # Or raise an exception if SUMO_HOME is essential