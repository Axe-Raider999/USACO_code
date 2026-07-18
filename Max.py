q = input("How many values would you like to enter? Keep in mind that you may only enter positive integers. ")
while q.isnumeric() == False:
	q = input("Invalid input, try again - please enter a positive integer : ")
q = int(q)
s = 0
data = []
while s < q:
	w = input("Enter a value : ")
	while w.isnumeric() == False:
		w = input("Invalid input, try again - Enter a positive integer : ")
	data.append(int(w))
	s += 1
x = data[0]
for num in data:
	if num > x:
		x = num
print("Your largest value is " + str(x))