#! /usr/bin/env python

import sys
import DataPoint

canopyCenters = []

#taking data from the std input

for line in sys.stdin:
	dp = DataPoint.DataPoint(line.strip())

	if len(canopyCenters) == False:
		canopyCenters.append(dp)

	else:
		insert = True
		for center in canopyCenters:
			if dp.checkT2(center):
				insert = False
				break
		if insert == True:
			canopyCenters.append(dp)

#printing data std output
for canopyCenter in canopyCenters:
	print("1\t" + canopyCenter.toString())