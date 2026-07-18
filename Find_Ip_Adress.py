with open("number.in") as read:
	num = read.readline()
	array = num.split(".")
def isinteger(number):
	try:
		int(number)
		return True
	except ValueError:
		return False
y = 0
if len(array) == 4:
	for i in range(4):
		x = isinteger(array[i])
		if x == True:
			if int(array[i]) >= 0 and int(array[i]) <= 255:
				y += 1
if y == 4:
	print("That is an IP Adress")
else:
	print("That is not an IP Adress")