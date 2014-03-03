#! /usr/bin/env python

import random
file = open("dataPoints.txt","w+")

#write data points to a file
for i in range(100000):
	year = random.randint(0, 99)
	if year < 10:
		year = "190" + str(year)
	else:
		year = "19" + str(year)
	temp = random.randint(5, 60)
	file.write(year + "," + str(temp)+"\n")
file.write(year + "," + str(temp)+"\n")
file.close()


file = open("kCentroids.txt","w+")

#write k centroids to a file
for i in range(3):
	year = random.randint(0, 99)
	if year < 10:
		year = "190" + str(year)
	else:
		year = "19" + str(year)
	temp = random.randint(5, 60)
	file.write(year + "," + str(temp)+"\n")
file.write(year + "," + str(temp)+"\n")
file.close()
