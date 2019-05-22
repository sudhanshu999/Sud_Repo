class Parent:
	def __init__(self):
		self.fname='Anil'
		self.mname='Neelam'
		
	def ghar_address(self):
		self.address="saket Nagar"
		print (self.address)

class Children(Parent):
	def __init__(self):
		self.name='sudhanshu'
		
		super().__init__()

	def getdisplay(self):
		print ("your name is:",self.name)
		self.ghar_address()
		print ("The parent name is ")
		print ("The father name:",self.fname)
		print ("the mother name is:",self.mname)

s1=Children()
s1.getdisplay()
