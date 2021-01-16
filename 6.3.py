>>> def is_between(x, y, z):
	if x <= y <= z:
		return True
	else:
		return False

	
>>> is_between(10, 20, 30)
True
>>> is_between(30, 10, 20)
False
>>> 