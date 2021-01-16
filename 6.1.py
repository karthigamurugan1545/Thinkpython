>>> def compare_fn(x, y):
	if(x>y):
		return 1
	if(x==y):
		return 0
	if(x<y):
		return -1

	
>>> compare_fn(20, 10)
1
>>> compare_fn(20, 20)
0
>>> compare_fn(40, 20)
1
>>> 