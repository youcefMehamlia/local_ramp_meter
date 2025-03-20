
 
traci._edge	index
/home/delphi/gcc/sumo/tools/traci/_edge.py
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
EdgeDomain

 
class EdgeDomain(traci.domain.Domain)
   	 	
Method resolution order:
EdgeDomain
traci.domain.Domain
builtins.object
Methods defined here:
__init__(self)
Initialize self.  See help(type(self)) for accurate signature.
adaptTraveltime(self, edgeID, time, begin=None, end=None)
adaptTraveltime(string, double, double, double) -> None
 
Adapt the travel time value (in s) used for (re-)routing for the given edge.
 
When setting begin time and end time (in seconds), the changes only
apply to that time range. Otherwise they apply all the time
getAdaptedTraveltime(self, edgeID, time)
getAdaptedTraveltime(string, double) -> double
 
Returns the travel time value (in s) used for (re-)routing
which is valid on the edge at the given time.
getAngle(self, edgeID, relativePosition=-1073741824.0)
getAngle(string, double) -> double
Returns the heading of the straight line segment formed by the first lane of the edge at the given position.
If the given position equals TraCI constant INVALID_DOUBLE_VALUE, it returns the total angle
formed by the edge, from its start point to its end point. If the edge doesn't have any lanes,
then INVALID_DOUBLE_VALUE is returned.
getBidiEdge(self, edgeID)
getBidiEdge(string) -> string
 
Returns the id of the bidi edge or ""
getCO2Emission(self, edgeID)
getCO2Emission(string) -> double
 
Returns the CO2 emission in mg for the last time step on the given edge.
getCOEmission(self, edgeID)
getCOEmission(string) -> double
 
Returns the CO emission in mg for the last time step on the given edge.
getEffort(self, edgeID, time)
getEffort(string, double) -> double
 
Returns the effort value used for (re-)routing
which is valid on the edge at the given time.
getElectricityConsumption(self, edgeID)
getElectricityConsumption(string) -> double
 
Returns the electricity consumption in ml for the last time step.
getFromJunction(self, edgeID)
getFromJunction(string) -> string
 
Returns the id of the junction at the start of this edge
getFuelConsumption(self, edgeID)
getFuelConsumption(string) -> double
 
Returns the fuel consumption in ml for the last time step on the given edge.
getHCEmission(self, edgeID)
getHCEmission(string) -> double
 
Returns the HC emission in mg for the last time step on the given edge.
getLaneNumber(self, edgeID)
getLaneNumber(string) -> int
 
Returns the number of lanes of this edge
getLastStepHaltingNumber(self, edgeID)
getLastStepHaltingNumber(string) -> integer
 
Returns the total number of halting vehicles for the last time step on the given edge.
A speed of less than 0.1 m/s is considered a halt.
getLastStepLength(self, edgeID)
getLastStepLength(string) -> double
 
Returns the mean vehicle length in m for the last time step on the given edge.
getLastStepMeanSpeed(self, edgeID)
getLastStepMeanSpeed(string) -> double
 
Returns the average speed in m/s for the last time step on the given edge.
getLastStepOccupancy(self, edgeID)
getLastStepOccupancy(string) -> double
 
Returns the net occupancy (excluding inter-vehicle gaps) in % for the last time step on the given edge.
getLastStepPersonIDs(self, edgeID)
getLastStepPersonIDs(string) -> list(string)
 
Returns the ids of the persons on the given edge during the last time step.
getLastStepVehicleIDs(self, edgeID)
getLastStepVehicleIDs(string) -> list(string)
 
Returns the ids of the vehicles for the last time step on the given edge.
getLastStepVehicleNumber(self, edgeID)
getLastStepVehicleNumber(string) -> integer
 
Returns the total number of vehicles for the last time step on the given edge.
getMeanFriction(self, edgeID)
getMeanFriction(string) -> double
 
Returns the average friction [0..1] for the last time step over all lanes on the given edge.
getNOxEmission(self, edgeID)
getNOxEmission(string) -> double
 
Returns the NOx emission in mg for the last time step on the given edge.
getNoiseEmission(self, edgeID)
getNoiseEmission(string) -> double
 
Returns the noise emission in db for the last time step on the given edge.
getPMxEmission(self, edgeID)
getPMxEmission(string) -> double
 
Returns the particular matter emission in mg for the last time step on the given edge.
getPendingVehicles(self, edgeID)
getPendingVehicles(string) -> list(string)
Returns a list of all vehicle ids waiting for insertion on this edge (with depart delay)
getStreetName(self, edgeID)
getStreetName(string) -> string
 
Returns the street name of this edge
getToJunction(self, edgeID)
getToJunction(string) -> string
 
Returns the id of the junction at the end of this edge
getTraveltime(self, edgeID)
getTraveltime(string) -> double
 
Returns the estimated travel time in s for the last time step on the given edge.
getWaitingTime(self, edgeID)
getWaitingTime(string) -> double
Returns the sum of the waiting time of all vehicles currently on
that edge (see traci.vehicle.getWaitingTime).
setAllowed(self, edgeID, allowedClasses)
setAllowed(string, list) -> None
 
Sets a list of allowed vehicle classes. Setting an empty list means all vehicles are allowed.
setDisallowed(self, edgeID, disallowedClasses)
setDisallowed(string, list) -> None
 
Sets a list of disallowed vehicle classes.
setEffort(self, edgeID, effort, begin=None, end=None)
setEffort(string, double, double, double) -> None
 
Adapt the effort value used for (re-)routing for the given edge.
 
When setting begin time and end time (in seconds), the changes only
apply to that time range. Otherwise they apply all the time.
setFriction(self, edgeID, friction)
setFriction(string, double) -> None
 
Set a new friction value [0..1] for all lanes of the edge.
setMaxSpeed(self, edgeID, speed)
setMaxSpeed(string, double) -> None
 
Set a new maximum speed (in m/s) for all lanes of the edge.
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