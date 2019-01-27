# basic python class
class data:

	# initalize the data
	def __init__(self):
		self.vector = [0,5,1,-2,7]

	# create a function to perform the same task
	def add_to_vec(self,num):
		for ind,val in enumerate(self.vector):
			self.vector[ind] += num