# with open("lostcow.in") as read:
# 	x, y = map(int, read.readline().split())
# multiplier = 1
# total_feet = 0
# direction = 0
# foundcow = False
# while True:
# 	if direction == 0:
# 		for _ in range(1, multiplier + 1):
# 			x += 1
# 			total_feet += 1
# 			if x == y:
# 				foundcow = True
# 				break
# 		multiplier *= 2
# 		direction += 1
# 	elif direction == 1:
# 		for _ in range(1, multiplier + 1):
# 			x -= 1
# 			total_feet += 1
# 			if x == y:
# 				foundcow = True
# 				break
# 		multiplier *= 2
# 		direction -= 1
# 	if foundcow:
# 		break
# with open("lostcow.out", "w") as written:
# 	written.write(str(total_feet))
with open("lostcow.in") as read:
	x, y = map(int, read.readline().split())
current_pos = x
multiplier = 1
total_feet = 0
direction = 0
foundcow = False
while not foundcow:
	if direction == 0:
		target_pos = x + multiplier
	elif direction == 1:
		target_pos = x - multiplier
	if current_pos == y:
		foundcow = True
		break
	for _ in range(abs(target_pos - current_pos)):
		if direction == 0:
			current_pos += 1
		if direction == 1:
			current_pos -= 1
		total_feet += 1
		if current_pos == y:
			foundcow = True
			break
	if direction == 0:
		direction += 1
	elif direction == 1:
		direction -= 1
	multiplier *= 2
with open("lostcow.out", "w") as written:
	written.write(str(total_feet))