>>> m=3
>>> n=4
>>> def ack(m, n):
	if(m == 0):
		return n+1
	elif(n == 0):
		return ack(m-1, 1)
	else:
		return ack(m-1, ack(m, n-1))

	
>>> ack(m, n)
125
>>> m=5
>>> n=6
>>> def ack(m, n):
	if(m == 0):
		return n+1
	elif(n == 0):
		return ack(m-1, 1)
	else:
		return ack(m-1, ack(m, n-1))

	
>>> ack(m, n)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    ack(m, n)
  File "<pyshell#8>", line 7, in ack
    return ack(m-1, ack(m, n-1))
  File "<pyshell#8>", line 7, in ack
    return ack(m-1, ack(m, n-1))
  File "<pyshell#8>", line 7, in ack
    return ack(m-1, ack(m, n-1))
  [Previous line repeated 3 more times]
  File "<pyshell#8>", line 5, in ack
    return ack(m-1, 1)
  File "<pyshell#8>", line 7, in ack
    return ack(m-1, ack(m, n-1))
  File "<pyshell#8>", line 7, in ack
    return ack(m-1, ack(m, n-1))
  File "<pyshell#8>", line 7, in ack
    return ack(m-1, ack(m, n-1))
  [Previous line repeated 1013 more times]
  File "<pyshell#8>", line 5, in ack
    return ack(m-1, 1)
  File "<pyshell#8>", line 2, in ack
    if(m == 0):
RecursionError: maximum recursion depth exceeded in comparison
>>> 