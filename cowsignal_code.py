with open("cowsignal.in") as read:
	rows, columns, scale = map(int, read.readline().split())
	signal = [read.readline() for x in range(rows)]
with open("cowsignal.out", "w") as write:
	for i in range(rows * scale):
		for j in range(columns * scale):
			print(signal[i // scale][j // scale], end = "")
		print()