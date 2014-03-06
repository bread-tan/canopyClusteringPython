#! /usr/bin/env python

import sys
import collections
from DataPoint import DataPoint


rfile = open("canopyCenters.txt","r")

kCentroids = []
canopyCenters = []
centroidList = []
canopyCenterKCentroidsDict = {}

### Setup for the mapper in Cluster Centroid Assignment Stage:

## Reading k-centroids (gen.py) and canopyCenters (mapperStg2.py) into lists:


wfile = open("kCentroids.txt","r")

for line in wfile:
	kp = DataPoint(line.strip())
	kCentroids.append(kp)


for line in rfile:
	cp = DataPoint(line.strip().split("\t")[1])
	canopyCenters.append(cp)

"""
for c in canopyCenters:
	print ("CanopyCenters:\t"+c.toString())

for k in kCentroids:
	print ("K Centroids:\t" + k.toString())

"""
## Adding the k-centroids and canopyCenters to a dictionary:
# outer loop canopy centers

for canopyCenter in canopyCenters:
	kCentroidsList = []
	for kCentroid in kCentroids:
		if (canopyCenter.checkT1(kCentroid)):
			#kCentroidsList.append(kCentroid.toString())
			kCentroidsList.append(kCentroid)
	if len(kCentroidsList)>0:
		#canopyCenterKCentroidsDict = {canopyCenter.toString():kCentroidsList}
		canopyCenterKCentroidsDict[canopyCenter] = kCentroidsList
# print(isinstance(canopyCenters[0], collections.Hashable))
# print canopyCenterKCentroidsDict[]


# print canopyCenterKCentroidsDict

"""print("CanopyCenter\t: K Centroid")

for item in canopyCenterKCentroidsDict:
	for item2 in canopyCenterKCentroidsDict[item]:
		print (item.toString() + " : " + item2.toString())
"""


for line in sys.stdin:
	(key,value) = line.strip().split("\t")
	#key = canopy center
	#value = data point

	canopyCenter = DataPoint(key)
	dataPoint = DataPoint(value)

	#print ("P1>\tcanopyCenter: " + canopyCenter.toString() + "\t dataPoint: " + dataPoint.toString())


	if canopyCenter in canopyCenterKCentroidsDict:
		#print ("canopyCenter : " + canopyCenter.toString() + "\t" + "kCentroidsList : " + "\t dataPoint : " + dataPoint.toString())
		kCentroidsList = canopyCenterKCentroidsDict[canopyCenter]	
		if len(kCentroidsList) < 1 :
			continue	
		minDistance = dataPoint.complexDistance(kCentroidsList[0])
		#print("Initial minDistance : " + str(minDistance) + "\tkCentroidsList[0] : " + kCentroidsList[0].toString())	
		pos = 0
		for i in range (1 , len(kCentroidsList)):
			currentDistance = dataPoint.complexDistance(kCentroidsList[i])
		#	print("currentDistance : " + str(currentDistance) + "\tkCentroidsList[i]" + kCentroidsList[i].toString())
			if currentDistance < minDistance:
				minDistance = currentDistance
				pos = 1	
		print (kCentroidsList[pos].toString() + "\t" + dataPoint.toString())