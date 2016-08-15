
# declare a function that takes a list argument
def check_string(items):
	# declare an empty list where you will append the length for strings
	empty = []
	# loop through the list argument
	for item in items:
		# append the length of strings in the list in empty list
		empty.append(len(item))
	return empty

print check_string(["Beth","Lynn","Monica","Kathure","Martha"])