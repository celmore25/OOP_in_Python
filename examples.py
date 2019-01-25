# lets create a simple data structure
data = [0,5,1,-2,7]
print('Data before function =',data)

# now create a function to perform an action on the data
# in this case we will just add a certain number
def add_to_data(data,num):
	for ind,val in enumerate(data):
		data[ind] += num
	return data

# now lets manipulate the data
data = add_to_data(data,3)
print('Data after function =',data)

