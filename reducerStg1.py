#! /usr/bin/env python

import sys
from DataPoint import DataPoint

canopyCenters = []

for line in sys.stdin:
	(kev,value) = line.split("\t")
	dp = DataPoint(value.strip())

	if len(canopyCenters) == 0:
		canopyCenters.append(dp)

	else:
		insert = True

		for center in canopyCenters:
			if dp.checkT2(center):
				insert = False
				break

		if insert == True:
			canopyCenters.append(dp)

for canopyCenter in canopyCenters:
	print("1\t" + canopyCenter.toString())