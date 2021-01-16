Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
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