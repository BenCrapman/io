#developed by Ben Chapman using python 2.7.6
#i/o test

import math

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

#this function will return true when a string argument can be a float
def is_float(my_string):
	#we only want a max of 1 decimal point, so we use a boolean to remember if there's a decimal point
	has_decimal = False
	
	#iterate through each element of the string but the first
	for i in my_string[1:len(my_string)]:
		#checks to see if there's a decimal point, and only allows one
		if (i == '.') and (has_decimal == False):
			has_decimal = True
		#if it's not a decimal point, or there's already a decimal point, return false
		elif (i > '9') or (i < '0'):
			return False
	
	#check to see if the first character is a decimal
	if (my_string[0] == '.') and not (has_decimal):
	#if that doesn't resolve, check if the character is another acceptable character
		return True
	elif (my_string[0] != '-') and ((my_string[0] > '9') or (my_string[0] < '0')):
		#if not, return false
		return False
	return True

#PROGRAM STARTS HERE ---------------------------------------------------

#let's define some variables
int_able = False
float_able = False

original = ''

#get input from the user
user_string = raw_input('Give me some data: ')
print 'you just said: ' + user_string

#store user_string in original for safe keeping, as well as some other stuff
original = user_string
int_able = is_int(user_string)
float_able = is_float(user_string)

#print the variable type (should just be string at this point)
print 'variable type: ' + get_type(user_string)

#let's try changing the variable type

#let's check if this can actually be turned into an int
if int_able:
	#if it can, we change it
	user_string = int(user_string)
	print 'now it\'s an ' + get_type(user_string)
	print user_string
else:
	print 'we can\'t turn this data into an int'

#revert back to normal
user_string = original

#now let's check if it can be turned into a float
if float_able:
	#if it can be a float, we make it so
	user_string = float(user_string)
	print 'now it\'s a ' + get_type(user_string)
	print user_string
else:
	print 'we can\'nt turn this data into a float'

#revert back to normal
user_string = original

#let's do some new lines
print '\n\n'

#now let's experiment with math operators
if int_able:
	print 'Ints are weird.'
	print 'They can\'t handle decimals, so division doesn\'t make sense.'
	for i in range(5):
		print user_string + ' / ' + str(i + 1) + ' = ' + str(int(user_string) / (i + 1))
	print 'The decimal is always truncated off, which translates to every division being rounded down'
	#another newline
	print '\n'

#now let's do some float stuff
if float_able:
	print 'Floats are like ints with decimal points.'
	print 'you can divide them by anything (except zero)'
	print 'the results don\'t have to be whole numbers'
	for i in range(5):
		print user_string + ' / ' + str(i + 1) + ' = ' + str(float(user_string) / (i + 1))
	print 'See? With floats, we can have non-whole numbers'
	#another newline
	print '\n'

#now let's mess around with the math library
if float_able:
	print 'Python has a math library.'
	print 'This library has a bunch of mathematical functions we can use.'
	print user_string + ' rounded up: ' + str(math.ceil(float(user_string)))
	print user_string + ' rounded down: ' + str(math.floor(float(user_string)))
	print 'absolute value of ' + user_string + ': ' + str(math.fabs(float(user_string)))
	print 'e^' + user_string + ' = ' + str(math.exp(float(user_string)))
	if int_able:
		print user_string + '! = ' + str(math.factorial(int(user_string)))
