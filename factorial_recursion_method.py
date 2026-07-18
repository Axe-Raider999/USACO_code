def factorial(n: int):
	if n==0:
		return 1
	if n==1:
		return 1
	return n * factorial(n-1)
output = factorial(5)
print(output)