#! /usr/bin/env python

import sys
import DataPoint

file = open("dataPoints.txt","r")
wfile = open("canopyCenters.txt","w+")
canopyCenters = []
canopys = []
DataPoints = []

#taking data from the std input


for line in sys.stdin:
	(kev,value) = line.split("\t")
	dp = DataPoint.DataPoint(value.strip())
	canopyCenters.append(dp)
canopyCenters.append(dp)

for centroid in canopyCenters:
	wfile.write(centroid.toString() + "\n")
wfile.write(centroid.toString())



for line in file:
	
	dp = DataPoint.DataPoint(line.strip())
	DataPoints.append(dp)
DataPoints.append(dp)

"""
for dp in DataPoints:
	print(dp.toString())
for centroid in canopyCenters:
	print(centroid.toString())
"""

insert = True
for dataPoint in DataPoints: 
	for centroid in canopyCenters:	
		insert = dataPoint.checkT1(centroid)
		if insert == False:
			break
	if insert == True:
		print(centroid.toString() + "\t" + dataPoint.toString())	
	print(centroid.toString() + "\t" + dataPoint.toString())
