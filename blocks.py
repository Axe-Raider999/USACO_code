with open("blocks.in") as read:
	n = int(read.readline())
	fronts = []
	backs = []
	for _ in range(n):
		f, b = read.readline().split()
		fronts.append(f)
		backs.append(b)


letters = [0] * 26

for i in range(n):
	front_counts = [0] * 26
	back_counts = [0] * 26
	for ch in fronts[i]:
		front_counts[ord(ch) - ord("a")] += 1
	for ch in backs[i]:
		back_counts[ord(ch) - ord("a")] += 1
	for c in range(26):
		letters[c] += max(front_counts[c], back_counts[c])

with open("blocks.out", "w") as write:
	for q in range(len(letters)):
		print(letters[q], file = write)
