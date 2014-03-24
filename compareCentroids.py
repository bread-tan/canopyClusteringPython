#! /usr/bin/env python

import sys
from DataPoint import DataPoint

#print "Start"

# read sys.argv[1] and sys.argv[2]
# put em in lists

if len(sys.argv)<3:
	print "Error: Insufficient Arguments"
	sys.exit(-1)

oldCentroidsFile = open(sys.argv[1],"r")
newCentroidsFile = open(sys.argv[2],"r")

oldCentroids = []
newCentroids = []

for line in oldCentroidsFile:
	if line.find("\t") != -1:
		(key,value) = line.strip().split("\t")
		oldCentroid = DataPoint(value)
	else:
		oldCentroid = DataPoint(line.strip()) 
	oldCentroids.append(oldCentroid)

for line in newCentroidsFile:
	(key,value) = line.strip().split("\t")
	newCentroids.append(DataPoint(value))


# compare every element with coressponding element in the other list using complex distance of the data points.

for i in range(len(oldCentroids)):
	#print("Distance between " + oldCentroids[i].toString() 
	#	+ " and " + newCentroids[i].toString() + " : " + str(oldCentroids[i].complexDistance(newCentroids[i])))
	if (oldCentroids[i].complexDistance(newCentroids[i])) > DataPoint.THRESHOLD:
		#print "Gonna return 0"
		sys.exit(0)
# if all of the distances ar ewithin the threshold, return 1 or else 0

#print "I'm done"
sys.exit(1)
