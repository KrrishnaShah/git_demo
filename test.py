class elex:
	x = 5
	def __init__(self, name, roll):
		self.name = name
		self.roll = roll

	def name_stud(self):
		print('Name of student: ' + self.name)

c1 = elex('Student1', 1)
print('Value: ' + str(c1.x))
c1.name_stud()
print('Roll no: ' + str(c1.roll))
# del c1.roll
# print('Roll no: ' + str(c1.roll))
