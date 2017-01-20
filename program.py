#developed by Ben Chapman using python 2.7.6
#i/o test

#this function will return the type of the variable in the argument
def get_type(variable):
	#store variable type into a string, cut off the brackets and quotes
	var_type = str(type(variable))
	var_type = var_type[7:len(var_type) - 2]
	return var_type

#this function will return true when the string argument can be an int
def is_int(my_string):
	#iterate through each element of the string but the first
	for i in my_string[1:len(my_string)]:
		if (i > '9') or (i < '0'):
			#return false when there's a non-number value
			return False
	#check if the first character is a - or a number
	if (my_string[0] != '-') and ((my_string[0] > '9') or (my_string[0] < '0')):
		#return false when it's neither
		return False
	#return true if none of the false-returns have triggered
	return True

#PROGRAM STARTS HERE

#get input from the user
user_string = raw_input('Give me some data: ')
print 'you just said: ' + user_string

#print the variable type (should just be string at this point)
print 'variable type: ' + get_type(user_string)

#let's try changing the variable type

#let's check if this can actually be turned into an int
if is_int(user_string):
	#if it can, we turn it into an int
	user_string = int(user_string)
	print 'now it\'s an ' + get_type(user_string)
