def sortedarray(numbers):	
	if len(numbers)<=1:
		print("Array sorted")
		return
	return numbers[0] <= numbers[1] and sortedarray(numbers[1:])
sortedarray([10,2,3])