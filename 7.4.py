>>> import math
>>> def eval_loop():
	while True:
		x=input('Enter the expression to evaluate:')
		if x == 'done':
			break
		else:
			y=eval(x)
			print(y)
	print(y)

	
>>> eval_loop()
Enter the expression to evaluate:6*6
36

