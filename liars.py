n = int(input())

g = []
l = []

for _ in range(n):
	line = input().split()
	if line[0] == "G":
		g.append(int(line[1]))
	else:
		l.append(int(line[1]))

liars = 0

while True:
	maxg = 0
	for i in range(len(g)):
		if g[i] > maxg:
			maxg = g[i]

	minl = 10 ** 9
	for i in range(len(l)):
		if l[i] < minl:
			minl = l[i]

	if maxg <= minl:
		print(liars)
		break

	if len(g) == 1 or len(l) == 1:
		liars += 1
		print(liars)
		break
	else:
		secondmaxg = 0
		for i in range(len(g)):
			if g[i] > secondmaxg and g[i] < maxg:
				secondmaxg = g[i]

		secondminl = 10 ** 9
		for i in range(len(l)):
			if l[i] < secondminl and l[i] > minl:
				secondminl = l[i]

		if maxg - secondmaxg > secondminl - minl:
			while maxg in g:
				g.remove(maxg)
				liars += 1
		else:
			while minl in l:
				l.remove(minl)
				liars += 1
