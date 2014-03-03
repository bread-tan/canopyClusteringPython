#! /usr/bin/env python

import sys
import DataPoint

#file = open("dataPoints.txt","r")
canopyCentersFile = open("canopyCenters.txt","r")
canopyCenters = []
canopys = []
#DataPoints = []

#taking data from the std input


for line in canopyCentersFile:
	(key,value) = line.split("\t")
	dp = DataPoint.DataPoint(value.strip())
	canopyCenters.append(dp)
#canopyCenters.append(dp)

#for centroid in canopyCenters:
#	wfile.write(centroid.toString() + "\n")
#wfile.write(centroid.toString())

for line in sys.stdin:
	
	dp = DataPoint.DataPoint(line.strip())
# 	#DataPoints.append(dp)
# 	#DataPoints.append(dp)

# """
# for dp in DataPoints:
# 	print(dp.toString())
# for centroid in canopyCenters:
# 	print(centroid.toString())
# """

	insert = True
#	for dataPoint in DataPoints: 
 	for canopyCenter in canopyCenters:	
 		insert = dp.checkT1(canopyCenter)
 		if insert == False:
 				#break
 				continue
 		if insert == True:
 			print(canopyCenter.toString() + "\t" + dp.toString())	
# 		print(centroid.toString() + "\t" + dataPoint.toString())