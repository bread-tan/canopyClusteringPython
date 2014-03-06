#! /usr/bin/env python

import sys
from DataPoint import DataPoint

prevKey = None
count = 0
yearSum = 0
tempSum = 0

for line in sys.stdin:
	(key , value) = line.split("\t")
	kCentroid = DataPoint(key.strip())
	dataPoints = DataPoint(value.strip())

	#print("K Centroid: " + kCentroid.toString() + "\t Data Point: " + dataPoints.toString())


	if prevKey is None:
		prevKey = kCentroid
		
		#print prevKey.toString()
		#print kCentroid.toString()

	if prevKey == kCentroid:
		yearSum = yearSum + dataPoints.year
		tempSum = tempSum + dataPoints.temp
		count = count + 1
		continue
		#print (str(yearSum)+ "\t" + str(tempSum) + "\t" + str(count))

	
	if prevKey != kCentroid:
		avgYear = yearSum / count
		avgTemp = tempSum / count
		print ("1\t"+str(avgYear)+","+str(avgTemp)+"\t"+kCentroid.toString())
		count = 1
		yearSum = dataPoints.year
		tempSum = dataPoints.temp
		prevKey = kCentroid
		continue
		
"""
		print("Year Sum: " + str(yearSum) + "\t\tAvg Year: " + str(avgYear))
		print("Temp Sum: " +str(tempSum) + "\t\tAvg Temp: " + str(avgTemp))
		print("Count: " + str(count))
		print("K Centroid:" + kCentroid.toString()+"\n")

"""