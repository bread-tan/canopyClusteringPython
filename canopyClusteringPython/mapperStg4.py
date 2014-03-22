#! /usr/bin/env python

import sys
from DataPoint import DataPoint

import sys

if len(sys.argv) < 2:
	print("ERROR: Insufficent arguments")
	sys.exit(-1)

file = open(sys.argv[1],"r")

kCentroids = []

for line in file:
	(key, value) = line.strip().split("\t")
	kCentroid = DataPoint(value)
	kCentroids.append(kCentroid)

file.close()

"""
for dataPoint in dataPoints:
	print dataPoint.toString()
"""


for line in sys.stdin:
	dataPoint = DataPoint(line.strip())
	
	minDistance = dataPoint.complexDistance(kCentroids[0])
	pos = 0
	for i in range (1, len(kCentroids)):
		distance = dataPoint.complexDistance(kCentroids[i])
		if distance < minDistance:
			minDistance = distance
			pos = i
	print(kCentroids[pos].toString()+"\t"+dataPoint.toString())
