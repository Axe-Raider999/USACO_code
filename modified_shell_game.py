with open("shell.in") as read:
	turns = int(read.readline())
	counter = [0, 0, 0]
	shell_at_pos = [0, 1, 2]
	for i in range(turns):
		a, b ,g = [int(x) - 1 for x in read.readline().split()]
		shell_at_pos[a], shell_at_pos[b] = shell_at_pos[b], shell_at_pos[a]
		counter[shell_at_pos[g]] += 1
with open("shell.out", "w") as written:
	print(max(counter), file=written)