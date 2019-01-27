# lets create a simple data structure
data = [0,5,1,-2,7]
# print('Data before function =',data)

# now create a function to perform an action on the data
# in this case we will just add a certain number
def add_to_data(data,num):
	for ind,val in enumerate(data):
		data[ind] += num
	return data

# now lets manipulate the data
data = add_to_data(data,3)
# print('Data after function =',data)

# now lets create a class to do the same thing as before
class data:

	# initalize the data
	def __init__(self):
		self.vector = [0,5,1,-2,7]

	# create a function to perform the same task
	def add_to_vec(self,num):
		for ind,val in enumerate(self.vector):
			self.vector[ind] += num

# create the object
obj = data()
print('Vector upon initalization: ',obj.vector)

# manipulate the data
obj.add_to_vec(3)
print('Vector after manipulatation: ',obj.vector)


