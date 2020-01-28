#Physics
#Bio
#Chem
#Engineering
#Tech
#Computer Science
#Agriculture
#English
#Filipino
#Social Science
#Mathematics
#Research

class Teacher:
	def __init__(self):
		self.id = ""
		self.name = ""
		self.toTeach = list()								#Subject[]
		self.prefTime = 0

class Subject:
	def __init__(self):
		self.id = ""
		self.name = ""
		self.preftTime = list()								#int[]

class SubjectPeriod:
	id = 0
	def __init__(self):
		self.specSubject = self.id
		self.teacher = None
		self.blocks = list()	
		self.id+=1							#Block[]

class Block:
	def __init__(self):
		self.id = ""
		self.name = ""
		self.studentSize = 0
		self.toLearn = list()       						#Subject[]

class Classroom:
	def __init__(self):
		self.id = ""
		self.name = ""
		self.seatSize = 0
		self.specSubject = list()							#Subject[]
		self.occupied = [[False]*8 for i in range(4)]

	def __str__(self):
		z = ""
		for x in self.occupied:
			for y in x:
				z += "[" + str(y)[0] + "] "
			z += "\n"
		return z

	def occupy(self, day, period):
		self.occupied[day][period] = True