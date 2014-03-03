#! /usr/bin/env python

import random
file = open("dataPoints.txt","w+")

#write to a file
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

#std output
"""for i in range(100000):
	year = random.randint(0, 99)
	if year < 10:
		year = "190" + str(year)
	else:
		year = "19" + str(year)
	temp = random.randint(5, 60)
	print(year + "," + str(temp))
print(year + "," + str(temp)+"\n")"""
