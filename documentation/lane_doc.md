
 
traci._lane	index
/home/delphi/gcc/sumo/tools/traci/_lane.py
# -*- coding: utf-8 -*-
# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.dev/sumo
# Copyright (C) 2011-2025 German Aerospace Center (DLR) and others.
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License 2.0 which is available at
# https://www.eclipse.org/legal/epl-2.0/
# This Source Code may also be made available under the following Secondary
# Licenses when the conditions for such availability set forth in the Eclipse
# Public License 2.0 are satisfied: GNU General Public License, version 2
# or later which is available at
# https://www.gnu.org/licenses/old-licenses/gpl-2.0-standalone.html
# SPDX-License-Identifier: EPL-2.0 OR GPL-2.0-or-later


 
Modules
      	 	
traci.constants

 
Classes
      	 	
traci.domain.Domain(builtins.object)
LaneDomain

 
class LaneDomain(traci.domain.Domain)
   	 	
Method resolution order:
LaneDomain
traci.domain.Domain
builtins.object
Methods defined here:
__init__(self)
Initialize self.  See help(type(self)) for accurate signature.
getAllowed(self, laneID)
getAllowed(string) -> list(string)
 
Returns a list of allowed vehicle classes. An empty list means all vehicles are allowed.
getAngle(self, laneID, relativePosition=-1073741824.0)
getAngle(string, double) -> double
Returns the heading of the straight line segment formed by the lane at the given position.
If the given position equals TraCI constant INVALID_DOUBLE_VALUE, it returns the total angle
formed by the lane, from its start point to its end point.
getBidiLane(self, laneID)
getBidiLane(string) -> string
 
Returns the id of the bidi lane or ""
getCO2Emission(self, laneID)
getCO2Emission(string) -> double
 
Returns the CO2 emission in mg/s for the last time step on the given lane.
Multiply by the step length to get the value for one step.
getCOEmission(self, laneID)
getCOEmission(string) -> double
 
Returns the CO emission in mg/s for the last time step on the given lane.
Multiply by the step length to get the value for one step.
getChangePermissions(self, laneID, direction)
getChangePermissions(string, int) -> list(string)
 
Returns a list of vehicle classesa allowed to change to the neighbor lane indicated by the direction
(left=0, right=1).
getDisallowed(self, laneID)
getDisallowed(string) -> list(string)
 
Returns a list of disallowed vehicle classes.
getEdgeID(self, laneID)
getEdgeID(string) -> string
 
Returns the id of the edge the lane belongs to.
getElectricityConsumption(self, laneID)
getElectricityConsumption(string) -> double
 
Returns the electricity consumption in Wh/s for the last time step.
Multiply by the step length to get the value for one step.
getFoes(self, laneID, toLaneID)
getFoes(string, string) -> list(string)
Returns the ids of incoming lanes that have right of way over the connection from laneID to toLaneID.
getFriction(self, laneID)
getFriction(string) -> double
 
Returns the friction on the lane.
getFuelConsumption(self, laneID)
getFuelConsumption(string) -> double
 
Returns the fuel consumption in mg/s for the last time step on the given lane.
Multiply by the step length to get the value for one step.
getHCEmission(self, laneID)
getHCEmission(string) -> double
 
Returns the HC emission in mg/s for the last time step on the given lane.
Multiply by the step length to get the value for one step.
getInternalFoes(self, laneID)
getFoes(string) -> list(string)
Returns the ids of internal lanes that are in conflict with the given internal lane id.
getLastStepHaltingNumber(self, laneID)
getLastStepHaltingNumber(string) -> integer
 
Returns the total number of halting vehicles for the last time step on the given lane.
A speed of less than 0.1 m/s is considered a halt.
getLastStepLength(self, laneID)
getLastStepLength(string) -> double
 
Returns the mean vehicle length in m for the last time step on the given lane.
getLastStepMeanSpeed(self, laneID)
getLastStepMeanSpeed(string) -> double
 
Returns the average speed in m/s for the last time step on the given lane.
getLastStepOccupancy(self, laneID)
getLastStepOccupancy(string) -> double
 
Returns the occupancy in % for the last time step on the given lane.
getLastStepVehicleIDs(self, laneID)
getLastStepVehicleIDs(string) -> list(string)
 
Returns the ids of the vehicles for the last time step on the given lane.
getLastStepVehicleNumber(self, laneID)
getLastStepVehicleNumber(string) -> integer
 
Returns the total number of vehicles for the last time step on the given lane.
getLength(self, laneID)
getLength(string) -> double
 
Returns the length in m.
getLinkNumber(self, laneID)
getLinkNumber(string) -> integer
 
Returns the number of connections to successive lanes.
getLinks(self, laneID, extended=True)
getLinks(string) -> list((string, bool, bool, bool))
A list containing id of successor lane together with priority, open and foe
for each link.
if extended=True, each result tuple contains
(string approachedLane, bool hasPrio, bool isOpen, bool hasFoe,
string approachedInternal, string state, string direction, float length)
 
isOpen: whether a vehicle driving at the speed limit (minimum auf
        incoming and outgoing lane) could safely pass the junction with
        regard to approaching foes if it were to enter it in this step
        (false for red traffic light).
        Foe vehicles that are already on the junction are ignored!
hasPrio: whether the link is the main road at a priority junction or
         currently has green light ('G')
hasFoe: whether any foe vehicles are approaching the junction or on the
        junction that would interfere with passing it in the current time step
getMaxSpeed(self, laneID)
getMaxSpeed(string) -> double
 
Returns the maximum allowed speed on the lane in m/s.
getNOxEmission(self, laneID)
getNOxEmission(string) -> double
 
Returns the NOx emission in mg/s for the last time step on the given lane.
Multiply by the step length to get the value for one step.
getNoiseEmission(self, laneID)
getNoiseEmission(string) -> double
 
Returns the noise emission in db for the last time step on the given lane.
getPMxEmission(self, laneID)
getPMxEmission(string) -> double
 
Returns the particular matter emission in mg/s for the last time step on the given lane.
Multiply by the step length to get the value for one step.
getPendingVehicles(self, laneID)
getPendingVehicles(string) -> list(string)
Returns a list of all vehicle ids waiting for insertion on this lane (with depart delay).
getShape(self, laneID)
getShape(string) -> list((double, double))
 
List of 2D positions (cartesian) describing the geometry.
getTraveltime(self, laneID)
getTraveltime(string) -> double
 
Returns the estimated travel time in s for the last time step on the given lane.
getWaitingTime(self, laneID)
getWaitingTime() -> double
 
.
getWidth(self, laneID)
getWidth(string) -> double
 
Returns the width of the lane in m.
setAllowed(self, laneID, allowedClasses)
setAllowed(string, list) -> None
 
Sets a list of allowed vehicle classes. Setting an empty list means all vehicles are allowed.
setChangePermissions(self, laneID, allowedClasses, direction)
setChangePermissions(string, list, int) -> None
 
Sets a list of vehicle classes allowed to change to the neighbor lane indicated by direction
(left=1, right=-1).
setDisallowed(self, laneID, disallowedClasses)
setDisallowed(string, list) -> None
 
Sets a list of disallowed vehicle classes.
setFriction(self, laneID, friction)
setFriction(string, double) -> None
 
Sets the friction of the lane.
setLength(self, laneID, length)
setLength(string, double) -> None
 
Sets the length of the lane in m.
setMaxSpeed(self, laneID, speed)
setMaxSpeed(string, double) -> None
 
Sets a new maximum allowed speed on the lane in m/s.
Methods inherited from traci.domain.Domain:
getAllContextSubscriptionResults(self)
getAllSubscriptionResults(self)
getAllSubscriptionResults() -> dict(string: dict(integer: <value_type>))
 
Returns the subscription results for the last time step and all objects of the domain.
It is not possible to retrieve older subscription results than the ones
from the last time step.
getContextSubscriptionResults(self, objectID)
getIDCount(self)
getIDCount() -> integer
 
Returns the number of currently loaded objects.
getIDList(self)
getIDList() -> list(string)
 
Returns a list of all objects in the network.
getParameter(self, objectID, key)
getParameter(string, string) -> string
 
Returns the value of the given parameter for the given objectID
getParameterWithKey(self, objectID, key)
getParameterWithKey(string, string) -> (string, string)
 
Returns the (key, value) tuple of the given parameter for the given objectID
getSubscriptionResults(self, objectID)
getSubscriptionResults(string) -> dict(integer: <value_type>)
 
Returns the subscription results for the last time step and the given object.
If the object id is unknown or the subscription did for any reason return no data,
'None' is returned.
It is not possible to retrieve older subscription results than the ones
from the last time step.
setParameter(self, objectID, key, value)
setParameter(string, string, string) -> None
 
Sets the value of the given parameter to value for the given objectID
subscribe(self, objectID, varIDs=None, begin=-1073741824.0, end=-1073741824.0, parameters=None)
subscribe(string, list(integer), double, double, map(string->tuple)) -> None
 
Subscribe to one or more object values for the given interval.
subscribeContext(self, objectID, domain, dist, varIDs=None, begin=-1073741824.0, end=-1073741824.0, parameters=None)
subscribeContext(string, int, double, list(integer), double, double) -> None
 
Subscribe to objects of the given domain (specified as domain=traci.constants.CMD_GET_<DOMAIN>_VARIABLE),
which are closer than dist to the object specified by objectID.
subscribeParameterWithKey(self, objectID, key, begin=-1073741824.0, end=-1073741824.0)
subscribeParameterWithKey(string, string) -> None
 
Subscribe for a generic parameter with the given key.
unsubscribe(self, objectID)
unsubscribe(string) -> None
 
Unsubscribe from receiving object values.
unsubscribeContext(self, objectID, domain, dist)
Data descriptors inherited from traci.domain.Domain:
__dict__
dictionary for instance variables
__weakref__
list of weak references to the object