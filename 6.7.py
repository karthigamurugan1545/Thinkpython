>>> def is_power(a,b):
	if(a%b !=0):
		return False
	elif(a/b == 1):
		return True
	else:
		return is_power(a/b,b)

	
>>> is_power(10,5)
False
>>> is_power(10, 10)
True
>>> 