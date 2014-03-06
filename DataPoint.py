#! /usr/bin/env python


import math

class DataPoint:
	T2 = 5
	T1 = 10
	tempSum = 0
	yearSum = 0
	count = 0 

	def set0(self):
		self.tempSum = 0
		self.yearSum = 0
		self.count = 1


	def __init__(self,inputLine):
		(self.year , self.temp) = inputLine.split(",")
		self.year = int(self.year)
		self.temp = int(self.temp)


	def __hash__(self):
		return hash((self.year, self.temp))

	def __eq__(self, other):
		return (self.year, self.temp) == (other.year, other.temp)

	def getTemp(self):
		return str(self.temp)

	def getYear(self):
		return str(self.year)

	def checkT2(self,center):
		if( abs ( self.temp - center.temp) < self.T2):
			return True
		else:
			return False

	def toString(self):
		return self.getYear() + "," + self.getTemp()


	def checkT1(self,point):
		if( abs (self.temp - point.temp) < self.T1):
			return True
		else:
			return False

	def complexDistance(self,point):
		return math.sqrt(abs((self.year - point.year) * (self.year - point.year) + (self.temp - point.temp) * (self.temp - point.temp)))

	def add(self, point):
		self.temp = self.temp + point.temp
		self.year = self.year + point.year
		return self

	def avg(self,count):
		if count is 0:
			print ("Error: DivideByZero")
			return		
		tempAvg = str(int(self.temp/count))
		yearAvg = str(int(self.year/count))
		print("1\t" + yearAvg + "," + tempAvg)
		return