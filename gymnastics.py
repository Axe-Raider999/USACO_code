with open("gymnastics.in") as read:
	k, n = map(int, read.readline().split())

	rounds = []

	for i in range(k):
		x = read.readline()
		rounds.append(str(x))


x = k
pairs = []
saved = []
consistent_pairs = 0

for _ in range(k):
	cur_round = []
	cur_round.extend(list(map(int, rounds[x-1].split())))
	saved = []
	for i in range(n):
		for j in range(i+1, n):
			if x == k:
				pairs.append([cur_round[i], cur_round[j]])
			elif x < k:
				if [cur_round[i], cur_round[j]] in pairs:
					saved.append(pairs.index([cur_round[i], cur_round[j]]))
	if x < k:
		for l in range(len(pairs)-1, -1, -1):
			if l in saved:
				continue
			else:
				pairs.pop(l)
	x -= 1
	rounds.pop()

consistent_pairs = len(pairs)

with open("gymnastics.out", "w") as write:
	write.write(str(consistent_pairs) + "\n")
