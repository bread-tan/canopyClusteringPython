#! /usr/bin/env python

import sys
import DataPoint


rfile = open("canopyCenters.txt","r")

kCentroids = []
canopyCenters = []
centroidList = []
canopyCenterKCentroidsDict = {}

### Setup for the mapper in Cluster Centroid Assignment Stage:

## Reading k-centroids (gen.py) and canopyCenters (mapperStg2.py) into lists:


wfile = open("kCentroids.txt","r")

for line in wfile:
	kp = DataPoint.DataPoint(line.strip())
	kCentroids.append(kp)


for line in rfile:
	cp = DataPoint.DataPoint(line.strip())
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
#	print ("canopyCenter:"+canopyCenter.toString())
	kCentroidsList = []
	for kCentroid in kCentroids:
#		print("kCentroid:"+kCentroid.toString())
		if (canopyCenter.checkT1(kCentroid)):
			kCentroidsList.append(kCentroid.toString())
#	for center in kCentroidsList:
#		print ("kCentroidsList:"+(center.toString()))
	if len(kCentroidsList)>0:
		canopyCenterKCentroidsDict = {canopyCenter.toString():kCentroidsList}

print("CanopyCenter\t: K Centroid")

for item in canopyCenterKCentroidsDict:
	for item2 in canopyCenterKCentroidsDict[item]:
		print (item + "\t\t:" + item2)

"""

canopyCenters = []
dataPoints = []

for line in sys.stdin:
	(kev,value) = line.split("\t")
	cc = DataPoint.DataPoint(key.strip())
	dp = DataPoint.DataPoint(value.strip())
	canopyCenters.append(cc)
	dataPoints.append(dp)


cenroids = []

for canopyCentersList, centroidList in canopyCenterKCentroidsDict:
	centroids = centroidList

dist = []


for key, value in centroids:
	
	dist = int(key)


	if dist < minDistance:
		minDistance = dist
		offset = key

	print(key, )
	




"""