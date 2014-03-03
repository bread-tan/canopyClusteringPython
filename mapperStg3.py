#! /usr/bin/env python

import sys
import DataPoint


file = open("canopyCenters.txt","r")

kCentroids = []
canopyCenters = []
centroidList = []
canopyCenterKCentroidsDict = {}

### Setup for the mapper in Cluster Centroid Assignment Stage:

## Reading k-centroids (gen.py) and canopyCenters (mapperStg2.py) into lists:
for line in file:
	dp = DataPoint.DataPoint(line.strip())
	canopyCenters.append(dp)
#canopyCenters.append(dp)

file.close()
file = open("kCentroids.txt","r")

for line in file:
	dp = DataPoint.DataPoint(line.strip())
	kCentroids.append(dp)
kCentroids.append(dp)

file.close()


## Adding the k-centroids and canopyCenters to a dictionary:
# outer loop canopy centers

for canopyCenter in canopyCenters:
	insert = True
	for kCentroid in kCentroids:
		insert = canopyCenter.checkT1(kCentroid)
		if insert == False:
			continue
		if insert == True:
			canopyCenterKCentroidsDict = {canopyCenter:centroids}



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
for c in canopyCenters:
	print (c.toString())

for k in kCentroids:
	print (k.toString())

"""