n = int(input())

statements = []
for _ in range(n):
	c, p = input().split()
	statements.append((c, int(p)))

best = n

for _, x in statements:
	liars = 0
	for c, p in statements:
		if c == "G" and x < p:
			liars += 1
		elif c == "L" and x > p:
			liars += 1
	if liars < best:
		best = liars

print(best)
