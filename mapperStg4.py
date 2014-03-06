#! /usr/bin/env python

import sys
from DataPoint import DataPoint

file = open("dataPoints.txt","r")


dataPoints = []
kCentroids = []

for line in file:
	dp = DataPoint(line.strip())
	dataPoints.append(dp)

file.close()

"""
for dataPoint in dataPoints:
	print dataPoint.toString()
"""


for line in sys.stdin:
	(key,value) = line.strip().split("\t")
	kC = DataPoint(value.strip())
	kCentroids.append(dp)

print type(kCentroids)


for dataPoint in dataPoints:
	minDistance = dataPoint.complexDistance(kCentroids[0])
	pos = 0
	for kCentroid in kCentroids:
		distance = dataPoint.complexDistance(kCentroid)
		if distance < minDistance:
			minDistance = distance
			pos = pos + 1
	print(kCentroids[pos].toString()+"\t"+dataPoint.toString())
