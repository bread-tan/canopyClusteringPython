#! /usr/bin/env python

import sys
from DataPoint import DataPoint
wfile = open("map3.txt","w+")

prevKey = None
count = 0
yearSum = 0
tempSum = 0
avgYear = 0
avgTemp = 0

for line in sys.stdin:
	wfile.write(line)
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
		#if(kCentroid.temp == 19):
		#	print (str(yearSum)+ "\t" + str(tempSum) + "\t" + str(count) + " " + kCentroid.toString())
	else:	
		avgYear = yearSum / count
		avgTemp = tempSum / count
		print ("1\t"+str(avgYear)+","+str(avgTemp))
		"""
		print("Year Sum: " + str(yearSum) + "\t\tAvg Year: " + str(avgYear))
		print("Temp Sum: " +str(tempSum) + "\t\tAvg Temp: " + str(avgTemp))
		print("Count: " + str(count))
		print("K Centroid:" + kCentroid.toString()+"\n")"""
		count = 1
		yearSum = dataPoints.year
		tempSum = dataPoints.temp
		prevKey = kCentroid
		
avgYear = yearSum / count
avgTemp = tempSum / count		
print ("1\t"+str(avgYear)+","+str(avgTemp))
"""
print("Year Sum: " + str(yearSum) + "\t\tAvg Year: " + str(avgYear))
print("Temp Sum: " +str(tempSum) + "\t\tAvg Temp: " + str(avgTemp))
print("Count: " + str(count))
print("K Centroid:" + kCentroid.toString()+"\n")"""