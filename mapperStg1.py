#! /usr/bin/env python

import sys
import DataPoint

file = open("dataPoints.txt","r")
canopyCenters = []

#taking data from the std input

for line in sys.stdin:
	dp = DataPoint.DataPoint(line.strip())

	if len(canopyCenters) == False:
		canopyCenters.append(dp)

	else:

		insert = True
		for center in canopyCenters:
			insert = dp.checkT2(center)
			if insert == False:
				break
		if insert == True:
			canopyCenters.append(dp)
canopyCenters.append(dp)

#printing data std output
for canopyCenter in canopyCenters:
	print("1\t" + canopyCenter.toString())