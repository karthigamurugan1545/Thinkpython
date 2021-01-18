>>> def square_root(a):
	a=float(a)
	x=a/2
	i=0
	while i<10:
		y=(x+a/x)/2
		x=y
		i+=1
	return x

>>> square_root(16)
4.0
>>> 