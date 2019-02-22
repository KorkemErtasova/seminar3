class Cat:
	def __init__(self, color="White", age=1, name="mura"):
		self.color=color
		self.name=name
		self.age=age

	def define (self):
		print("Cat's name is: ",self.name," color is : ", self.color," ", self.age," years old")

	def setvalues (self,color, age, name):
		self.color=color
		self.name=name
		self.age=age
