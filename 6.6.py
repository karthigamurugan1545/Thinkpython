>>> word='yo'
>>> def first(word):
	return word[0]

>>> def last(word):
	return word[-1]

>>> def middle(word):
	return word[1:-1]

>>> print(middle(word))


>>> print()

>>> 
>>> def is_palindrome(string):
	new_string=str(string)
	if len(new_string)<=1:
		return(True)
	elif first(new_string) == last(new_string):
		return is_palindrome(middle(new_string))
	else:
		return(False)

	
>>> print(is_palindrome('worw'))
False
>>> print(is_palindrome('vikadakavi'))
False
>>> print(is_palindrome('woow'))
True
>>> print(is_palindrome('redivider'))
True
>>> print(is_palindrome('rediveder'))
False
>>> print(is_palindrome('noon'))
True
>>> print(is_palindrome('42'))
False
>>> 