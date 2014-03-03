#! /usr/bin/env python


import math

class DataPoint:
	T2 = 5
	T1 = 10

	def __init__(self,inputLine):
		(self.year , self.temp) = inputLine.split(",")
		self.temp = int(self.temp)

	def getTemp(self):
		return str(self.temp)

	def getYear(self):
		return self.year

	def checkT2(self,center):
		if( abs ( self.temp - center.temp) < self.T2):
			return False
		else:
			return True

	def toString(self):
		return self.getYear() + "," + self.getTemp()


	def checkT1(self,point):
		if( abs (self.temp - point.temp) < self.T1):
			return False
		else:
			return True

	def complexDistance(self,point):
		return math.sqrt(abs((self.year - year) * (self.year - year) + (self.temp - temp) * (self.temp - temp)))
		
class Centroid:

	def __init__(self,inputLine):
		(self.year , self.temp) = inputLine.split(",")
		self.temp = int(self.temp)

	