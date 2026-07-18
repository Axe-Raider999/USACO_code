def factorial(n:int):
	x = 1
	while n > 1:
		x *= n
		n -= 1
	return x
print(factorial(4))