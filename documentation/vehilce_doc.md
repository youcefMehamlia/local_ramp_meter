
 
traci._vehicle	index
/home/delphi/gcc/sumo/tools/traci/_vehicle.py
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
warnings

 
Classes
      	 	
builtins.object
StopData
traci._vehicletype.VTypeDomain(traci.domain.Domain)
VehicleDomain

 
class StopData(builtins.object)
   	StopData(lane='', startPos=-1, endPos=-1, stoppingPlaceID='', stopFlags=0, duration=-1, until=-1, intendedArrival=-1, arrival=-1, depart=-1, split='', join='', actType='', tripId='', line='', speed=0)
 

 
 	Methods defined here:
__attr_repr__(self, attrname, default='')
__init__(self, lane='', startPos=-1, endPos=-1, stoppingPlaceID='', stopFlags=0, duration=-1, until=-1, intendedArrival=-1, arrival=-1, depart=-1, split='', join='', actType='', tripId='', line='', speed=0)
Initialize self.  See help(type(self)) for accurate signature.
__repr__(self)
Return repr(self).
Data descriptors defined here:
__dict__
dictionary for instance variables
__weakref__
list of weak references to the object

 
class VehicleDomain(traci._vehicletype.VTypeDomain)
   	 	
Method resolution order:
VehicleDomain
traci._vehicletype.VTypeDomain
traci.domain.Domain
builtins.object
Methods defined here:
__init__(self)
Initialize self.  See help(type(self)) for accurate signature.
add(self, vehID, routeID, typeID='DEFAULT_VEHTYPE', depart='now', departLane='first', departPos='base', departSpeed='0', arrivalLane='current', arrivalPos='max', arrivalSpeed='current', fromTaz='', toTaz='', line='', personCapacity=0, personNumber=0)
Add a new vehicle (new style with all possible parameters)
If routeID is "", the vehicle will be inserted on a random network edge
if route consists of two disconnected edges, the vehicle will be treated
like a <trip> and use the fastest route between the two edges.
addFull = add(self, vehID, routeID, typeID='DEFAULT_VEHTYPE', depart='now', departLane='first', departPos='base', departSpeed='0', arrivalLane='current', arrivalPos='max', arrivalSpeed='current', fromTaz='', toTaz='', line='', personCapacity=0, personNumber=0)
addLegacy(self, vehID, routeID, depart=-3, pos=0, speed=0, lane=-6, typeID='DEFAULT_VEHTYPE')
Add a new vehicle (old style)
addSubscriptionFilterCFManeuver(self, downstreamDist=None, upstreamDist=None)
addSubscriptionFilterCFManeuver() -> None
 
Restricts vehicles returned by the last modified vehicle context subscription to leader and follower of the ego.
downstreamDist and upstreamDist specify the range of the search for leader and follower along the road net.
addSubscriptionFilterDownstreamDistance(self, dist)
addSubscriptionFilterDownstreamDist(float) -> None
 
Sets the downstream distance along the network for vehicles to be returned by the last modified
vehicle context subscription (call it just after subscribing).
addSubscriptionFilterFieldOfVision(self, openingAngle)
addSubscriptionFilterFieldOfVision(float) -> None
 
Restricts vehicles returned by the last modified vehicle context subscription
to vehicles within field of vision with given opening angle
addSubscriptionFilterLCManeuver(self, direction=None, noOpposite=False, downstreamDist=None, upstreamDist=None)
addSubscriptionFilterLCManeuver(int) -> None
 
Restricts vehicles returned by the last modified vehicle context subscription to neighbor and ego-lane leader
and follower of the ego.
direction - lane change direction (in {-1=right, 1=left})
noOpposite specifies whether vehicles on opposite direction lanes shall be returned
downstreamDist and upstreamDist specify the range of the search for leader and follower along the road net.
Combine with: distance filters; vClass/vType filter.
addSubscriptionFilterLanes(self, lanes, noOpposite=False, downstreamDist=None, upstreamDist=None)
addSubscriptionFilterLanes(list(integer), bool, double, double) -> None
 
Adds a lane-filter to the last modified vehicle context subscription (call it just after subscribing).
lanes is a list of relative lane indices (-1 -> right neighboring lane of the ego, 0 -> ego lane, etc.)
noOpposite specifies whether vehicles on opposite direction lanes shall be returned
downstreamDist and upstreamDist specify the range of the search for surrounding vehicles along the road net.
addSubscriptionFilterLateralDistance(self, lateralDist, downstreamDist=None, upstreamDist=None)
addSubscriptionFilterLateralDist(double, double, double) -> None
 
Adds a lateral distance filter to the last modified vehicle context subscription
(call it just after subscribing).
downstreamDist and upstreamDist specify the longitudinal range of the search
for surrounding vehicles along the ego vehicle's route.
addSubscriptionFilterLeadFollow(self, lanes)
addSubscriptionFilterLCManeuver(lanes) -> None
 
Restricts vehicles returned by the last modified vehicle context subscription to neighbor and ego-lane leader
and follower of the ego.
Combine with: lanes-filter to restrict to one direction; distance filters; vClass/vType filter.
addSubscriptionFilterNoOpposite(self)
addSubscriptionFilterNoOpposite() -> None
 
Omits vehicles on other edges than the ego's for the last modified vehicle context subscription
(call it just after subscribing).
addSubscriptionFilterTurn(self, downstreamDist=None, foeDistToJunction=None)
addSubscriptionFilterTurn(double, double) -> None
 
Restricts vehicles returned by the last modified vehicle context subscription to foes on upcoming junctions
addSubscriptionFilterUpstreamDistance(self, dist)
addSubscriptionFilterUpstreamDist(float) -> None
 
Sets the upstream distance along the network for vehicles to be returned by the last modified
vehicle context subscription (call it just after subscribing).
addSubscriptionFilterVClass(self, vClasses)
addSubscriptionFilterVClass(list(String)) -> None
 
Restricts vehicles returned by the last modified vehicle context subscription to vehicles of the given classes
addSubscriptionFilterVType(self, vTypes)
addSubscriptionFilterVType(list(String)) -> None
 
Restricts vehicles returned by the last modified vehicle context subscription to vehicles of the given types
changeLane(self, vehID, laneIndex, duration)
changeLane(string, int, double) -> None
Forces a lane change to the lane with the given index; The lane change
will be attempted for the given duration (in s) and if it succeeds,
the vehicle will stay on that lane for the remaining duration.
changeLaneRelative(self, vehID, indexOffset, duration)
changeLaneRelative(string, int, double) -> None
 
Forces a relative lane change; if successful,
the lane will be chosen for the given amount of time (in s).
The indexOffset specifies the target lane relative to the vehicles current lane
changeSublane(self, vehID, latDist)
changeSublane(string, double) -> None
Forces a lateral change by the given amount (negative values indicate changing to the right, positive
to the left). This will override any other lane change motivations but conform to
safety-constraints as configured by laneChangeMode.
changeTarget(self, vehID, edgeID)
changeTarget(string, string) -> None
 
The vehicle's destination edge is set to the given edge id. The route is rebuilt.
couldChangeLane(self, vehID, direction, state=None)
couldChangeLane(string, int) -> bool
Return whether the vehicle could change lanes in the specified direction.
This reflects the state after the last try to change lanes.
If you want to execute changeLane as a result of the evaluation of this function
it is not guaranteed to work because vehicle movements occur first.
deactivateGapControl(self, vehID)
deactivateGapControl(string) -> None
 
Deactivate the vehicle's gap control
dispatchTaxi(self, vehID, reservations)
dispatchTaxi(string, list(string)) -> None
dispatches the taxi with the given id to service the given reservations.
If only a single reservation is given, this implies pickup and drop-off
If multiple reservations are given, each reservation id must occur twice
(once for pickup and once for drop-off) and the list encodes ride
sharing of passengers (in pickup and drop-off order)
getAcceleration(self, vehID)
getAcceleration(string) -> double
 
Returns the acceleration in m/s^2 of the named vehicle within the last step.
getAccumulatedWaitingTime(self, vehID)
getAccumulatedWaitingTime(string) -> double
The accumulated waiting time of a vehicle collects the vehicle's waiting time
over a certain time interval (interval length is set per option '--waiting-time-memory')
getAdaptedTraveltime(self, vehID, time, edgeID)
getAdaptedTraveltime(string, double, string) -> double
 
Returns the information about the travel time of edge "edgeID" valid
for the given time from the vehicle's internal edge weights
container (see setAdaptedTraveltime).
If there is no individual travel time set, INVALID_DOUBLE_VALUE is returned.
getAllowedSpeed(self, vehID)
getAllowedSpeed(string) -> double
 
Returns the maximum allowed speed on the current lane regarding speed factor in m/s for this vehicle.
getAngle(self, vehID)
getAngle(string) -> double
 
Returns the angle in degrees of the named vehicle within the last step.
getBestLanes(self, vehID)
getBestLanes(string) -> tuple(data)
where data is a tuple of (laneID, length, occupation, offset, allowsContinuation, tuple(nextLanes))
 
For each lane of the current edge a data tuple is returned where the
entries have the following meaning:
- laneID: the id of that lane on the current edge
- the length that can be driven without lane change (measured from the start of that lane)
- the occupation on the future lanes (brutto vehicle lengths)
- the offset of that lane from the lane that would be strategically
  preferred (this is the lane that requires the least future lane
  changes or a lane that needs to be used for stopping)
- whether that lane allows continuing the route (for at least one more edge)
- the sequence of lanes that would be driven starting at laneID if no
  lane change were to take place
getCO2Emission(self, vehID)
getCO2Emission(string) -> double
 
Returns the CO2 emission in mg/s for the last time step.
Multiply by the step length to get the value for one step.
getCOEmission(self, vehID)
getCOEmission(string) -> double
 
Returns the CO emission in mg/s for the last time step.
Multiply by the step length to get the value for one step.
getDepartDelay(self, vehID)
getDepartDelay(string) -> double
 
Returns the delay between intended and actual departure in seconds
getDeparture(self, vehID)
getDeparture(string) -> double
 
Returns the actual departure time in seconds
getDistance(self, vehID)
getDistance(string) -> double
 
Returns the distance to the starting point like an odometer.
getDrivingDistance(self, vehID, edgeID, pos, laneIndex=0)
getDrivingDistance(string, string, double, integer) -> double
 
For an edge along the remaining route of vehID, return the distance from the current vehicle position
to the given edge and position along the vehicles route.
Otherwise, return INVALID_DOUBLE_VALUE
getDrivingDistance2D(self, vehID, x, y)
getDrivingDistance2D(string, double, double) -> integer
 
Return the distance to the given network position along the vehicles route.
getEffort(self, vehID, time, edgeID)
getEffort(string, double, string) -> double
 
Returns the information about the effort needed for edge "edgeID" valid
for the given time from the vehicle's internal effort
container (see setEffort).
If there is no individual travel time set, INVALID_DOUBLE_VALUE is returned.
getElectricityConsumption(self, vehID)
getElectricityConsumption(string) -> double
 
Returns the electricity consumption in Wh/s for the last time step.
Multiply by the step length to get the value for one step.
getFollowSpeed(self, vehID, speed, gap, leaderSpeed, leaderMaxDecel, leaderID='')
getFollowSpeed(string, double, double, double, double, string) -> double
Return the follow speed computed by the carFollowModel of vehID
getFollower(self, vehID, dist=0.0)
getFollower(string, double) -> (string, double)
 
Return the following vehicle id together with the distance. The distance
is measured from the front + minGap of the follower to the back of vehID, so it does not include the
minGap of the follower.
The dist parameter defines the minimum lookback, 0 calculates the
lookback distance from the braking distance at 4.5m/s^2 at 2*roadSpeedLimit.
Due to junctions and lane merges, there may be multiple followers.
In this case, the "critical" follower is returned. This is the follower
where the value of (getSecureGap - gap) is maximal.
Note that the returned follower may be further away than the given dist.
getFuelConsumption(self, vehID)
getFuelConsumption(string) -> double
 
Returns the fuel consumption in mg/s for the last time step.
Multiply by the step length to get the value for one step.
getHCEmission(self, vehID)
getHCEmission(string) -> double
 
Returns the HC emission in mg/s for the last time step.
Multiply by the step length to get the value for one step.
getJunctionFoes(self, vehID, dist=0.0)
getJunctionFoes(string, double) -> complex
 
Return list of junction foes [(foeId, egoDist, foeDist, egoExitDist, foeExitDist,
egoLane, foeLane, egoResponse, foeResponse), ...] within the given distance to the given vehicle.
getLaneChangeMode(self, vehID)
getLaneChangeMode(string) -> integer
 
Gets the vehicle's lane change mode as a bitset.
getLaneChangeState(self, vehID, direction)
getLaneChangeState(string, int) -> (int, int)
Return the lane change state for the vehicle. The first value returns
the state as computed by the lane change model and the second value
returns the state after incorporation TraCI requests.
See getLaneChangeStatePretty for an interpretation of the integer/bitset
results
getLaneChangeStatePretty(self, vehID, direction)
getLaneChangeStatePretty(string, int) -> ([string, ...], [string, ...])
Return the lane change state for the vehicle as two lists of string
constants. The first list returns the state as computed by the lane change
model and the second list returns the state after incorporation TraCI requests.
getLaneID(self, vehID)
getLaneID(string) -> string
 
Returns the id of the lane the named vehicle was at within the last step.
getLaneIndex(self, vehID)
getLaneIndex(string) -> integer
 
Returns the index of the lane the named vehicle was at within the last step.
getLanePosition(self, vehID)
getLanePosition(string) -> double
 
The position of the vehicle along the lane measured in m.
getLastActionTime(self, vehID)
getLastActionTime(string) -> double
 
Returns the time in s of last action point for this vehicle.
getLateralLanePosition(self, vehID)
getLateralLanePosition(string) -> double
 
Returns the lateral position of the vehicle on its current lane measured in m.
getLateralSpeed(self, vehID)
getLateralSpeed(string) -> double
 
Returns the lateral speed in m/s of the named vehicle within the last step.
getLeader(self, vehID, dist=100.0)
getLeader(string, double) -> (string, double)
 
Return the leading vehicle id together with the distance. The distance
is measured from the front + minGap to the back of the leader, so it does not include the
minGap of the vehicle.
The dist parameter defines the minimum lookahead, 0 calculates a lookahead from the brake gap.
Note that the returned leader may be further away than the given dist and that the vehicle
will only look on its current best lanes and not look beyond the end of its final route edge.
 
In the case where no leader is found, the function returns 'None'.
This special case is deprecated. The future behavior is to return the
pair ("", -1) when no leader is found.
The function 'traci.setLegacyGetLeader(bool) can be used to switch
between both behaviors.
getLeftFollowers(self, vehID, blockingOnly=False)
getLeftFollowers(string, bool) -> list(pair(string, double))
Convenience method, see getNeighbors()
getLeftLeaders(self, vehID, blockingOnly=False)
getLeftLeaders(string, bool) -> list(pair(string, double))
Convenience method, see getNeighbors()
getLine(self, vehID)
getLine(string) -> string
 
Returns the line information of this vehicle.
getLoadedIDList(self)
getLoadedIDList() -> list(string)
returns all loaded vehicles that have not yet left the simulation
getNOxEmission(self, vehID)
getNOxEmission(string) -> double
 
Returns the NOx emission in mg/s for the last time step.
Multiply by the step length to get the value for one step.
getNeighbors(self, vehID, mode)
getNeighbors(string, byte) -> list(pair(string, double))
 
The parameter mode is a bitset (UBYTE), specifying the following:
bit 1: query lateral direction (left:0, right:1)
bit 2: query longitudinal direction (followers:0, leaders:1)
bit 3: blocking (return all:0, return only blockers:1)
 
The returned list contains pairs (ID, dist) for all lane change relevant neighboring leaders, resp. followers,
along with their longitudinal distance to the ego vehicle (egoFront - egoMinGap to leaderBack, resp.
followerFront - followerMinGap to egoBack. The value can be negative for overlapping neighs).
For the non-sublane case, the lists will contain at most one entry.
 
Note: The exact set of blockers in case blocking==1 is not determined for the sublane model,
but either all neighboring vehicles are returned (in case LCA_BLOCKED) or
none is returned (in case !LCA_BLOCKED).
getNextLinks(self, vehID)
getNextLinks(string) -> [(string, string, bool, bool, bool, string, string, double), ...]
 
Return list of upcoming links along the route [(lane, via, priority, opened, foe,
 state, direction, length), ...]
getNextStops(self, vehID)
getNextStops(string) -> [(string, double, string, int, double, double), ...]
 
Return list of upcoming stops [(lane, endPos, stoppingPlaceID, stopFlags, duration, until), ...]
where integer stopFlag is defined as:
       1 * stopped +
       2 * parking +
       4 * personTriggered +
       8 * containerTriggered +
      16 * isBusStop +
      32 * isContainerStop +
      64 * chargingStation +
     128 * parkingarea
with each of these flags defined as 0 or 1.
getNextTLS(self, vehID)
getNextTLS(string) ->
 
Return list of upcoming traffic lights [(tlsID, tlsIndex, distance, state), ...]
getNoiseEmission(self, vehID)
getNoiseEmission(string) -> double
 
Returns the noise emission in db for the last time step.
getPMxEmission(self, vehID)
getPMxEmission(string) -> double
 
Returns the particular matter emission in mg/s for the last time step.
Multiply by the step length to get the value for one step.
getPersonIDList(self, vehID)
getPersonIDList(string) -> list(string)
Returns the list of persons who are riding in this vehicle.
getPersonNumber(self, vehID)
getPersonNumber(string) -> integer
Returns the total number of persons which includes those defined
using attribute 'personNumber' as well as <person>-objects who are riding in
this vehicle.
getPosition(self, vehID)
getPosition(string) -> (double, double)
 
Returns the position of the named vehicle within the last step [m,m].
getPosition3D(self, vehID)
getPosition3D(string) -> (double, double, double)
 
Returns the position of the named vehicle within the last step [m,m,m].
getRightFollowers(self, vehID, blockingOnly=False)
getRightFollowers(string, bool) -> list(tuple(string, double))
Convenience method, see getNeighbors()
getRightLeaders(self, vehID, blockingOnly=False)
getRightLeaders(string, bool) -> list(tuple(string, double))
Convenience method, see getNeighbors()
getRoadID(self, vehID)
getRoadID(string) -> string
 
Returns the id of the edge the named vehicle was at within the last step.
getRoute(self, vehID)
getRoute(string) -> list(string)
 
Returns the ids of the edges the vehicle's route is made of.
getRouteID(self, vehID)
getRouteID(string) -> string
 
Returns the id of the route of the named vehicle.
getRouteIndex(self, vehID)
getRouteIndex(string) -> int
 
Returns the index of the current edge within the vehicles route or -1 if the
vehicle has not yet departed
getRoutingMode(self, vehID)
getRoutingMode(string)
returns the current routing mode:
tc.ROUTING_MODE_DEFAULT    : use weight storages and fall-back to edge speeds (default)
tc.ROUTING_MODE_AGGREGATED : use global smoothed travel times from device.rerouting
getSecureGap(self, vehID, speed, leaderSpeed, leaderMaxDecel, leaderID='')
getSecureGap(string, double, double, double, string) -> double
Return the secure gap computed by the carFollowModel of vehID
getSegmentID(self, vehID)
getSegmentID(string) -> string
 
Returns the id of the segment the named vehicle was at within the last step (mesosim).
getSegmentIndex(self, vehID)
getSegmentIndex(string) -> integer
 
Returns the index of the segment the named vehicle was at within the last step (mesosim).
getSignals(self, vehID)
getSignals(string) -> integer
 
Returns an integer encoding the state of a vehicle's signals.
getSlope(self, vehID)
getSlope(string) -> double
The slope at the current position of the vehicle in degrees
getSpeed(self, vehID)
getSpeed(string) -> double
 
Returns the (longitudinal) speed in m/s of the named vehicle within the last step.
getSpeedMode(self, vehID)
getSpeedMode(string) -> int
The speed mode of a vehicle
getSpeedWithoutTraCI(self, vehID)
getSpeedWithoutTraCI(string) -> double
Returns the speed that the vehicle would drive if no speed-influencing
command such as setSpeed or slowDown was given.
getStopArrivalDelay(self, vehID)
getStopArrivalDelay(string) -> double
Returns the expected arrival delay at the next stop (if that stop defines the
arrival-attribute) in seconds. The returned value may be negative to
indicate early arrival.  Returns INVALID_DOUBLE if the next stop is not applicable
getStopDelay(self, vehID)
getStopDelay(string) -> double
Returns the expected depart delay at the next stop (if that stop defines the
until-attribute) in seconds. Returns -1 if the next stop is not applicable
getStopParameter(self, vehID, nextStopIndex, param, customParam=False)
getStopParameter(string, int, string) -> string
Gets the value of the given parameter for the stop at the given index
Negative indices permit access to past stops.
Supported params correspond to all legal stop xml-attributes
If customParam is set to True, the user defined stop parameter with the
specified param name will be returned instead (or "" if undefined)
getStopSpeed(self, vehID, speed, gap)
getStopSpeed(string, double, double) -> double
Return the speed for stopping at gap computed by the carFollowModel of vehID
getStopState(self, vehID)
getStopState(string) -> integer
 
Returns information in regard to stopping:
The returned integer is defined as 1 * stopped + 2 * parking
+ 4 * personTriggered + 8 * containerTriggered + 16 * isBusStop
+ 32 * isContainerStop
with each of these flags defined as 0 or 1
getStops(self, vehID, limit=0)
getStops(string, int) -> [StopData, ...],
 
Return a list of StopData object. The flags are the same as for setStop and
replaceStop (and different from getNextStops(!) for backward compatibility):
       1 * parking +
       2 * personTriggered +
       4 * containerTriggered +
       8 * isBusStop +
      16 * isContainerStop +
      32 * chargingStation +
      64 * parkingarea
with each of these flags defined as 0 or 1.
 
The optional argument limit can be used to limit the returned stops to
the next INT number (i.e. limit=1 if only the next stop is required).
Setting a negative limit returns up to 'limit' previous stops (or fewer
if the vehicle stopped fewer times previously)
getTaxiFleet(self, taxiState=0)
getTaxiFleet(int) -> list(string)
Return the list of all taxis with the given taxiState:
0 : empty
1 : pickup
2 : occupied
getTeleportingIDList(self)
getTeleportingIDList() -> list(string)
returns all teleporting or jumping vehicles
getTimeLoss(self, vehID)
getTimeLoss(string) -> double
Returns the time loss since departure
getTypeID(self, vehID)
getTypeID(string) -> string
 
Returns the id of the type of the named vehicle.
getVia(self, vehID)
getVia(string) -> list(string)
 
Returns the ids of via edges for this vehicle
getWaitingTime(self, vehID)
getWaitingTime(string) -> double
The waiting time of a vehicle is defined as the time (in seconds) spent with a
speed below 0.1m/s since the last time it was faster than 0.1m/s.
(basically, the waiting time of a vehicle is reset to 0 every time it moves).
A vehicle that is stopping intentionally with a <stop> does not accumulate waiting time.
highlight(self, vehID, color=(255, 0, 0, 255), size=-1, alphaMax=-1, duration=-1, type=0)
highlight(string, color, float, ubyte, float, ubyte) -> None
Adds a circle of the given color tracking the vehicle.
If a positive size [in m] is given the size of the highlight is chosen accordingly,
otherwise the length of the vehicle is used as reference.
If alphaMax and duration are positive, the circle fades in and out within the given duration,
otherwise it permanently follows the vehicle.
insertStop(self, vehID, nextStopIndex, edgeID, pos=1.0, laneIndex=0, duration=-1073741824.0, flags=0, startPos=-1073741824.0, until=-1073741824.0, teleport=0)
insertStop(string, int, string, double, integer, double, integer, double, double) -> None
 
Insert stop at the given index (within the list of all existing stops).
Automatically modifies the route if the new stop is not along the route between the preceeding
and succeeding stops (or start / end).
For edgeID a stopping place id may be given if the flag marks this
stop as stopping on busStop, parkingArea, containerStop etc.
If teleport is set to 1, the route to the new stop will be
disconnected (forcing a teleport).
If stopIndex is 0 the gap will be between the current
edge and the new stop. Otherwise the gap will be between the stop edge for
nextStopIndex - 1 and the new stop.
isAtBusStop(self, vehID)
isAtBusStop(string) -> bool
Return whether the vehicle is stopped at a bus stop
isAtContainerStop(self, vehID)
isAtContainerStop(string) -> bool
Return whether the vehicle is stopped at a container stop
isRouteValid(self, vehID)
isRouteValid(string) -> bool
Returns whether the current vehicle route is connected for the vehicle
class of the given vehicle.
isStopped(self, vehID)
isStopped(string) -> bool
Return whether the vehicle is stopped
isStoppedParking(self, vehID)
isStoppedParking(string) -> bool
Return whether the vehicle is parking (implies stopped)
isStoppedTriggered(self, vehID)
isStoppedTriggered(string) -> bool
Return whether the vehicle is stopped and waiting for a person or container
moveTo(self, vehID, laneID, pos, reason=0)
moveTo(string, string, double, integer) -> None
 
Move a vehicle to a new position along its current route.
moveToXY(self, vehID, edgeID, laneIndex, x, y, angle=-1073741824.0, keepRoute=1, matchThreshold=100)
Place vehicle at the given x,y coordinates and force its angle to
the given value (for drawing).
If the angle is set to INVALID_DOUBLE_VALUE, the vehicle assumes the
natural angle of the edge on which it is driving.
If keepRoute is set to 1, the closest position
within the existing route is taken. If keepRoute is set to 0, the vehicle may move to
any edge in the network but its route then only consists of that edge.
If keepRoute is set to 2 the vehicle has all the freedom of keepRoute=0
but in addition to that may even move outside the road network.
edgeID and lane are optional placement hints to resolve ambiguities.
The command fails if no suitable target position is found within the
distance given by matchThreshold.
openGap(self, vehID, newTimeHeadway, newSpaceHeadway, duration, changeRate, maxDecel=-1, referenceVehID=None)
openGap(string, double, double, double, double, double, string) -> None
 
Changes the vehicle's desired time headway (cf-parameter tau) smoothly to the given new value
using the given change rate. Similarly, the given space headway is applied gradually
to achieve a minimal spatial gap.
The vehicle is commanded to keep the increased headway for
the given duration once its target value is attained. The maximal value for the
deceleration can be given to prevent harsh braking due to the change of tau. If maxDecel=-1,
the limit determined by the CF model is used.
A vehicle ID for a reference vehicle can optionally be given, otherwise, the gap is created with
respect to the current leader on the ego vehicle's current lane.
Note that this does only affect the following behavior regarding the current leader and does
not influence the gap acceptance during lane change, etc.
remove(self, vehID, reason=3)
Remove vehicle with the given ID for the give reason.
Reasons are defined in module constants and start with REMOVE_
replaceStop(self, vehID, nextStopIndex, edgeID, pos=1.0, laneIndex=0, duration=-1073741824.0, flags=0, startPos=-1073741824.0, until=-1073741824.0, teleport=0)
replaceStop(string, int, string, double, integer, double, integer, double, double) -> None
 
Replaces stop at the given index (within the list of all stops) with a new stop.
Automatically modifies the route if the replacement stop is at another location.
For edgeID a stopping place id may be given if the flag marks this
stop as stopping on busStop, parkingArea, containerStop etc.
If edgeID is "", the stop at the given index will be removed without
replacement and the route will not be modified (unless setting
teleport=2 which will trigger rerouting between the prior and next stop)
If teleport is set to 1, the route to the replacement stop will be
disconnected (forcing a teleport).
If stopIndex is 0 the gap will be between the current
edge and the new stop. Otherwise the gap will be between the stop edge for
nextStopIndex - 1 and the new stop.
requestToC(self, vehID, leadTime)
requestToC(string, double) -> None
 
Interface for triggering a transition of control for a vehicle equipped with a ToC device.
rerouteEffort(self, vehID)
rerouteEffort(string) -> None
Reroutes a vehicle according to the effort values.
rerouteParkingArea(self, vehID, parkingAreaID)
rerouteParkingArea(string, string)
 
Changes the next parking area in parkingAreaID, updates the vehicle route,
and preserve consistency in case of passengers/containers on board.
rerouteTraveltime(self, vehID, currentTravelTimes=True)
rerouteTraveltime(string, bool) -> None
Reroutes a vehicle.
If currentTravelTimes is True (default) and the routing mode is still ROUTING_MODE_DEFAULT
then the ROUTING_MODE_AGGREGATED_CUSTOM gets activated temporarily
and used for rerouting. The various functions and options for
customizing travel times are described at https://sumo.dlr.de/wiki/Simulation/Routing
 
When rerouteTraveltime has been called once with an aggregated routing mode,
edge weight storage and update gets activated which might slow down the simulation.
resume(self, vehID)
resume(string) -> None
 
Resumes the vehicle from the current stop (throws an error if the vehicle is not stopped).
setAcceleration(self, vehID, acceleration, duration)
setAcceleration(string, double, double) -> None
 
Sets the acceleration in m/s^2 for the named vehicle and the given duration.
setAdaptedTraveltime(self, vehID, edgeID, time=None, begTime=None, endTime=None)
setAdaptedTraveltime(string, string, double, double, double) -> None
Inserts the information about the travel time of edge "edgeID" valid
from begin time to end time into the vehicle's internal edge weights
container.
If the time is not specified, any previously set values for that edge
are removed.
If begTime or endTime are not specified the value is set for the whole
simulation duration.
setBusStop(self, vehID, stopID, duration=-1073741824.0, until=-1073741824.0, flags=0)
setBusStop(string, string, double, double, integer) -> None
 
Adds or modifies a bus stop with the given parameters. The duration and the until attribute are
in seconds.
setChargingStationStop(self, vehID, stopID, duration=-1073741824.0, until=-1073741824.0, flags=0)
setChargingStationStop(string, string, double, double, integer) -> None
 
Adds or modifies a stop at a chargingStation with the given parameters. The duration and the until attribute are
in seconds.
setContainerStop(self, vehID, stopID, duration=-1073741824.0, until=-1073741824.0, flags=0)
setContainerStop(string, string, double, double, integer) -> None
 
Adds or modifies a container stop with the given parameters. The duration and the until attribute are
in seconds.
setEffort(self, vehID, edgeID, effort=None, begTime=None, endTime=None)
setEffort(string, string, double, double, double) -> None
Inserts the information about the effort of edge "edgeID" valid from
begin time to end time into the vehicle's internal edge weights
container.
If the time is not specified, any previously set values for that edge
are removed.
If begTime or endTime are not specified the value is set for the whole
simulation duration.
setLaneChangeMode(self, vehID, laneChangeMode)
setLaneChangeMode(string, integer) -> None
 
Sets the vehicle's lane change mode as a bitset.
setLateralLanePosition(self, vehID, posLat)
setLateralLanePosition(string, double) -> None
 
Sets the lateral vehicle position relative to the center line of the
lane in m (negative values are to the right in right-hand networks).
The vehicle may adapt this position in the same step unless this is
disabled via setLaneChangeMode.
setLine(self, vehID, line)
setLine(string, string) -> None
 
Sets the line information for this vehicle.
setParkingAreaStop(self, vehID, stopID, duration=-1073741824.0, until=-1073741824.0, flags=1)
setParkingAreaStop(string, string, double, double, integer) -> None
 
Adds or modifies a stop at a parkingArea with the given parameters. The duration and the until attribute are
in seconds.
setPreviousSpeed(self, vehID, speed, acceleration=-1073741824.0)
setPreviousSpeed(string, double, double) -> None
 
Sets the previous speed in m/s for the named vehicle wich will be used for
calculations in the current step. Optionally, the acceleration for the
previous step (in m/s^2) can be set as well.
setRoute(self, vehID, edgeList)
setRoute(string, list) ->  None
 
changes the vehicle route to given edges list.
The first edge in the list has to be the one that the vehicle is at at the moment.
 
example usage:
setRoute('1', ['1', '2', '4', '6', '7'])
 
this changes route for vehicle id 1 to edges 1-2-4-6-7
setRouteID(self, vehID, routeID)
setRouteID(string, string) -> None
 
Changes the vehicles route to the route with the given id.
setRoutingMode(self, vehID, routingMode)
setRoutingMode(string, int) -> None
Sets the current routing mode:
tc.ROUTING_MODE_DEFAULT    : use weight storages and fall-back to edge speeds (default)
tc.ROUTING_MODE_AGGREGATED : use global smoothed travel times from device.rerouting
tc.ROUTING_MODE_AGGREGATED_CUSTOM : use weight storages and fall-back to smoothed travel times
setSignals(self, vehID, signals)
setSignals(string, integer) -> None
 
Sets an integer encoding the state of the vehicle's signals.
setSpeed(self, vehID, speed)
setSpeed(string, double) -> None
 
Sets the speed in m/s for the named vehicle within the last step.
Calling with speed=-1 hands the vehicle control back to SUMO.
setSpeedMode(self, vehID, speedMode)
setSpeedMode(string, integer) -> None
 
Sets the vehicle's speed mode as a bitset.
setStop(self, vehID, edgeID, pos=1.0, laneIndex=0, duration=-1073741824.0, flags=0, startPos=-1073741824.0, until=-1073741824.0)
setStop(string, string, double, integer, double, integer, double, double) -> None
 
Adds or modifies a stop with the given parameters. The duration and the until attribute are
in seconds.
setStopParameter(self, vehID, nextStopIndex, param, value, customParam=False)
setStopParameter(string, int, string, string) -> None
Sets the value of the given parameter for the (upcoming) stop at the
given index (within the list of all stops).
Supported params correspond to (almost) all legal stop xml-attributes
and their value semantics
If customParam is set to True, the user defined stop parameter with the
specified param name will be set instead
setType(self, vehID, typeID)
setType(string, string) -> None
 
Sets the id of the type for the named vehicle.
setVia(self, vehID, edgeList)
setVia(string, list) ->  None
 
changes the via edges to the given edges list (to be used during
subsequent rerouting calls).
 
Note: a single edgeId as argument is allowed as shorthand for a list of length 1
slowDown(self, vehID, speed, duration)
slowDown(string, double, double) -> None
 
Changes the speed smoothly to the given value over the given amount
of time in seconds (can also be used to increase speed).
subscribeLeader(self, vehID, dist=0.0, begin=0, end=2147483647)
subscribeLeader(string, double, double, double) -> None
 
Subscribe for the leading vehicle id together with the distance.
The dist parameter defines the maximum lookahead, 0 calculates a lookahead from the brake gap.
updateBestLanes(self, vehID)
updateBestLanes(string) -> None
Triggers an update of the vehicle's bestLanes (structure determining the lane preferences used by LC models)
It may be called after modifying the vClass for instance.
wantsAndCouldChangeLane(self, vehID, direction, state=None)
wantsAndCouldChangeLane(string, int) -> bool
Return whether the vehicle wants to and could change lanes in the specified direction
This reflects the state after the last try to change lanes.
If you want to execute changeLane as a result of the evaluation of this function
it is not guaranteed to work because vehicle movements occur first.
Data and other attributes defined here:
DEPART_CONTAINER_TRIGGERED = -2
DEPART_LANE_ALLOWED_FREE = -4
DEPART_LANE_BEST_FREE = -5
DEPART_LANE_FIRST_ALLOWED = -6
DEPART_LANE_FREE = -3
DEPART_LANE_RANDOM = -2
DEPART_NOW = -3
DEPART_SPEED_MAX = -3
DEPART_SPEED_RANDOM = -2
DEPART_TRIGGERED = -1
LAST_TRAVEL_TIME_UPDATE = -1
STOP_BUS_STOP = 8
STOP_CHARGING_STATION = 32
STOP_CONTAINER_STOP = 16
STOP_CONTAINER_TRIGGERED = 4
STOP_DEFAULT = 0
STOP_PARKING = 1
STOP_PARKING_AREA = 64
STOP_TRIGGERED = 2
Methods inherited from traci._vehicletype.VTypeDomain:
getAccel(self, typeID)
getAccel(string) -> double
 
Returns the maximum acceleration in m/s^2 of this type.
If called in the context of a person or vehicle, it will return the value for their current type.
Use the respective object ID as typeID value in said context.
getActionStepLength(self, typeID)
getActionStepLength(string) -> double
 
Returns the action step length for this type.
If called in the context of a person or vehicle, it will return the value for their current type.
Use the respective object ID as typeID value in said context.
getApparentDecel(self, typeID)
getApparentDecel(string) -> double
 
Returns the apparent deceleration in m/s^2 of this type.
If called in the context of a person or vehicle, it will return the value for their current type.
Use the respective object ID as typeID value in said context.
getBoardingDuration(self, typeID)
getBoardingDuration(string) -> double
 
Returns the boarding duration of this type
getColor(self, typeID)
getColor(string) -> (integer, integer, integer, integer)
 
Returns the color of this type.
If called in the context of a person or vehicle, it will return their specific color if it has been set.
Use the respective object ID as typeID value in said context.
getDecel(self, typeID)
getDecel(string) -> double
 
Returns the maximal comfortable deceleration in m/s^2 of this type.
If called in the context of a person or vehicle, it will return the value for their current type.
Use the respective object ID as typeID value in said context.
getEmergencyDecel(self, typeID)
getEmergencyDecel(string) -> double
 
Returns the maximal physically possible deceleration in m/s^2 of this type.
If called in the context of a person or vehicle, it will return the value for their current type.
Use the respective object ID as typeID value in said context.
getEmissionClass(self, typeID)
getEmissionClass(string) -> string
 
Returns the emission class of this type.
If called in the context of a person or vehicle, it will return the value for their current type.
Use the respective object ID as typeID value in said context.
getHeight(self, typeID)
getHeight(string) -> double
 
Returns the height in m of this type.
If called in the context of a person or vehicle, it will return the value for their current type.
Use the respective object ID as typeID value in said context.
getImpatience(self, typeID)
getImpatience(string) -> double
 
Returns the Impatience of this type
getImperfection(self, typeID)
getImperfection(string) -> double
 
Returns the driver's imperfection for this type.
If called in the context of a person or vehicle, it will return the value for their current type.
Use the respective object ID as typeID value in said context.
getLateralAlignment(self, typeID)
getLateralAlignment(string) -> string
 
Returns The preferred lateral alignment of the type.
If called in the context of a person or vehicle, it will return the value for their current type.
Use the respective object ID as typeID value in said context.
getLength(self, typeID)
getLength(string) -> double
 
Returns the length in m of this type.
If called in the context of a person or vehicle, it will return the value for their current type.
Use the respective object ID as typeID value in said context.
getMass(self, typeID)
getMass(string) -> double
 
Returns the mass in kg of this type.
If called in the context of a person or vehicle, it will return the value for their current type.
Use the respective object ID as typeID value in said context.
getMaxSpeed(self, typeID)
getMaxSpeed(string) -> double
 
Returns the maximum speed in m/s of this type.
If called in the context of a person or vehicle, it will return the value for their current type.
Use the respective object ID as typeID value in said context.
getMaxSpeedLat(self, typeID)
getMaxSpeedLat(string) -> double
 
Returns the maximum lateral speed in m/s of this type.
If called in the context of a person or vehicle, it will return the value for their current type.
Use the respective object ID as typeID value in said context.
getMinGap(self, typeID)
getMinGap(string) -> double
 
Returns the offset (gap to front vehicle if halting) of this type.
If called in the context of a person or vehicle, it will return the value for their current type.
Use the respective object ID as typeID value in said context.
getMinGapLat(self, typeID)
getMinGapLat(string) -> double
 
Returns The desired lateral gap of this type at 50km/h in m
If called in the context of a person or vehicle, it will return the value for their current type.
Use the respective object ID as typeID value in said context.
getPersonCapacity(self, typeID)
getPersonCapacity(string) -> int
 
Returns the person capacity of this type.
If called in the context of a person or vehicle, it will return the value for their current type.
Use the respective object ID as typeID value in said context.
getShapeClass(self, typeID)
getShapeClass(string) -> string
 
Returns the shape class of this type.
If called in the context of a person or vehicle, it will return the value for their current type.
Use the respective object ID as typeID value in said context.
getSpeedDeviation(self, typeID)
getSpeedDeviation(string) -> double
 
Returns the maximum speed deviation of this type.
If called in the context of a person or vehicle, it will return the value for their current type.
Use the respective object ID as typeID value in said context.
getSpeedFactor(self, typeID)
getSpeedFactor(string) -> double
 
Returns the speed factor of this type.
If called in the context of a person or vehicle, it will return the value for their current type.
Use the respective object ID as typeID value in said context.
getTau(self, typeID)
getTau(string) -> double
 
Returns the driver's desired headway in s for this type.
If called in the context of a person or vehicle, it will return the value for their current type.
Use the respective object ID as typeID value in said context.
getVehicleClass(self, typeID)
getVehicleClass(string) -> string
 
Returns the class of this type.
If called in the context of a person or vehicle, it will return the value for their current type.
Use the respective object ID as typeID value in said context.
getWidth(self, typeID)
getWidth(string) -> double
 
Returns the width in m of this type.
If called in the context of a person or vehicle, it will return the value for their current type.
Use the respective object ID as typeID value in said context.
setAccel(self, typeID, accel)
setAccel(string, double) -> None
 
Sets the maximum acceleration in m/s^2 of this type.
If called in the context of a person or vehicle, it will change the value just for the single instance.
Use the respective object ID as typeID value in said context.
setActionStepLength(self, typeID, actionStepLength, resetActionOffset=True)
setActionStepLength(string, double, bool) -> None
 
Sets the action step length for this type. If resetActionOffset == True (default), the
next action point is scheduled immediately for all vehicles of the type.
If resetActionOffset == False, the interval between the last and the next action point is
updated to match the given value for all vehicles of the type, or if the latter is smaller
than the time since the last action point, the next action follows immediately.
If called in the context of a person or vehicle, it will change the value just for the single instance.
Use the respective object ID as typeID value in said context.
setApparentDecel(self, typeID, decel)
setApparentDecel(string, double) -> None
 
Sets the apparent deceleration in m/s^2 of this type.
If called in the context of a person or vehicle, it will change the value just for the single instance.
Use the respective object ID as typeID value in said context.
setBoardingDuration(self, typeID, boardingDuration)
setBoardingDuration(string, double) -> None
 
Sets the boarding duration of the this type.
If called in the context of a person or vehicle, it will change the value just for the single instance.
Use the respective object ID as typeID value in said context.
setColor(self, typeID, color)
setColor(string, (integer, integer, integer, integer)) -> None
 
Sets the color of this type.
If called in the context of a person or vehicle, it will change the value just for the single instance.
Use the respective object ID as typeID value in said context.
setDecel(self, typeID, decel)
setDecel(string, double) -> None
 
Sets the maximal comfortable deceleration in m/s^2 of this type.
If called in the context of a person or vehicle, it will change the value just for the single instance.
Use the respective object ID as typeID value in said context.
setEmergencyDecel(self, typeID, decel)
setEmergencyDecel(string, double) -> None
 
Sets the maximal physically possible deceleration in m/s^2 of this type.
If called in the context of a person or vehicle, it will change the value just for the single instance.
Use the respective object ID as typeID value in said context.
setEmissionClass(self, typeID, clazz)
setEmissionClass(string, string) -> None
 
Sets the emission class of this type.
If called in the context of a person or vehicle, it will change the value just for the single instance.
Use the respective object ID as typeID value in said context.
setHeight(self, typeID, height)
setHeight(string, double) -> None
 
Sets the height in m of this type.
If called in the context of a person or vehicle, it will change the value just for the single instance.
Use the respective object ID as typeID value in said context.
setImpatience(self, typeID, impatience)
setImpatience(string, double) -> None
 
Sets the impatience of the this type.
If called in the context of a person or vehicle, it will change the value just for the single instance.
Use the respective object ID as typeID value in said context.
setImperfection(self, typeID, imperfection)
setImperfection(string, double) -> None
 
Sets the driver imperfection of this type.
If called in the context of a person or vehicle, it will change the value just for the single instance.
Use the respective object ID as typeID value in said context.
setLateralAlignment(self, typeID, latAlignment)
setLateralAlignment(string, string) -> None
 
Sets the preferred lateral alignment of this type.
If called in the context of a person or vehicle, it will change the value just for the single instance.
Use the respective object ID as typeID value in said context.
setLength(self, typeID, length)
setLength(string, double) -> None
 
Sets the length in m of the this type.
If called in the context of a person or vehicle, it will change the value just for the single instance.
Use the respective object ID as typeID value in said context.
setMass(self, typeID, mass)
setMass(string, double) -> None
 
Sets the mass in kg of this type.
If called in the context of a person or vehicle, it will change the value just for the single instance.
Use the respective object ID as typeID value in said context.
setMaxSpeed(self, typeID, speed)
setMaxSpeed(string, double) -> None
 
Sets the maximum speed in m/s of this type.
If called in the context of a person or vehicle, it will change the value just for the single instance.
Use the respective object ID as typeID value in said context.
setMaxSpeedLat(self, typeID, speed)
setMaxSpeedLat(string, double) -> None
 
Sets the maximum lateral speed of this type.
If called in the context of a person or vehicle, it will change the value just for the single instance.
Use the respective object ID as typeID value in said context.
setMinGap(self, typeID, minGap)
setMinGap(string, double) -> None
 
Sets the offset (gap to front vehicle if halting) of this type.
If called in the context of a person or vehicle, it will change the value just for the single instance.
Use the respective object ID as typeID value in said context.
setMinGapLat(self, typeID, minGapLat)
setMinGapLat(string, double) -> None
 
Sets the minimum lateral gap at 50km/h of this type.
If called in the context of a person or vehicle, it will change the value just for the single instance.
Use the respective object ID as typeID value in said context.
setShapeClass(self, typeID, shapeClass)
setShapeClass(string, string) -> None
 
Sets the shape class of this type.
If called in the context of a person or vehicle, it will change the value just for the single instance.
Use the respective object ID as typeID value in said context.
setSpeedFactor(self, typeID, factor)
setSpeedFactor(string, double) -> None
 
Sets the speed factor of this type.
If called in the context of a person or vehicle, it will change the value just for the single instance.
Use the respective object ID as typeID value in said context.
setTau(self, typeID, tau)
setTau(string, double) -> None
 
Sets the driver's tau-parameter (reaction time or anticipation time depending on the car-following model) in s
for this type.
If called in the context of a person or vehicle, it will change the value just for the single instance.
Use the respective object ID as typeID value in said context.
setVehicleClass(self, typeID, clazz)
setVehicleClass(string, string) -> None
 
Sets the class of this type.
If called in the context of a person or vehicle, it will change the value just for the single instance.
Use the respective object ID as typeID value in said context.
setWidth(self, typeID, width)
setWidth(string, double) -> None
 
Sets the width in m of this type.
If called in the context of a person or vehicle, it will change the value just for the single instance.
Use the respective object ID as typeID value in said context.
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