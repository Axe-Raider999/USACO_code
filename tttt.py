with open("tttt.in") as read:
	board = []
	for _ in range(3):
		board += list(read.readline().strip())


singles = []

# rows
if board[0] == board[1] == board[2]:
	if board[0] not in singles:
		singles.append(board[0])
if board[3] == board[4] == board[5]:
	if board[3] not in singles:
		singles.append(board[3])
if board[6] == board[7] == board[8]:
	if board[6] not in singles:
		singles.append(board[6])

# columns
if board[0] == board[3] == board[6]:
	if board[0] not in singles:
		singles.append(board[0])
if board[1] == board[4] == board[7]:
	if board[1] not in singles:
		singles.append(board[1])
if board[2] == board[5] == board[8]:
	if board[2] not in singles:
		singles.append(board[2])

# diagonals
if board[0] == board[4] == board[8]:
	if board[0] not in singles:
		singles.append(board[0])
if board[2] == board[4] == board[6]:
	if board[2] not in singles:
		singles.append(board[2])


teams_a = []
teams_b = []

# row 1
x = ""
y = ""
if board[0] == board[1] and board[0] != board[2]:
	x = board[0]
	y = board[2]
elif board[0] == board[2] and board[0] != board[1]:
	x = board[0]
	y = board[1]
elif board[1] == board[2] and board[1] != board[0]:
	x = board[1]
	y = board[0]
if x != "":
	found = False
	for i in range(len(teams_a)):
		if teams_a[i] == x and teams_b[i] == y:
			found = True
		if teams_a[i] == y and teams_b[i] == x:
			found = True
	if not found:
		teams_a.append(x)
		teams_b.append(y)

# row 2
x = ""
y = ""
if board[3] == board[4] and board[3] != board[5]:
	x = board[3]
	y = board[5]
elif board[3] == board[5] and board[3] != board[4]:
	x = board[3]
	y = board[4]
elif board[4] == board[5] and board[4] != board[3]:
	x = board[4]
	y = board[3]
if x != "":
	found = False
	for i in range(len(teams_a)):
		if teams_a[i] == x and teams_b[i] == y:
			found = True
		if teams_a[i] == y and teams_b[i] == x:
			found = True
	if not found:
		teams_a.append(x)
		teams_b.append(y)

# row 3
x = ""
y = ""
if board[6] == board[7] and board[6] != board[8]:
	x = board[6]
	y = board[8]
elif board[6] == board[8] and board[6] != board[7]:
	x = board[6]
	y = board[7]
elif board[7] == board[8] and board[7] != board[6]:
	x = board[7]
	y = board[6]
if x != "":
	found = False
	for i in range(len(teams_a)):
		if teams_a[i] == x and teams_b[i] == y:
			found = True
		if teams_a[i] == y and teams_b[i] == x:
			found = True
	if not found:
		teams_a.append(x)
		teams_b.append(y)

# column 1
x = ""
y = ""
if board[0] == board[3] and board[0] != board[6]:
	x = board[0]
	y = board[6]
elif board[0] == board[6] and board[0] != board[3]:
	x = board[0]
	y = board[3]
elif board[3] == board[6] and board[3] != board[0]:
	x = board[3]
	y = board[0]
if x != "":
	found = False
	for i in range(len(teams_a)):
		if teams_a[i] == x and teams_b[i] == y:
			found = True
		if teams_a[i] == y and teams_b[i] == x:
			found = True
	if not found:
		teams_a.append(x)
		teams_b.append(y)

# column 2
x = ""
y = ""
if board[1] == board[4] and board[1] != board[7]:
	x = board[1]
	y = board[7]
elif board[1] == board[7] and board[1] != board[4]:
	x = board[1]
	y = board[4]
elif board[4] == board[7] and board[4] != board[1]:
	x = board[4]
	y = board[1]
if x != "":
	found = False
	for i in range(len(teams_a)):
		if teams_a[i] == x and teams_b[i] == y:
			found = True
		if teams_a[i] == y and teams_b[i] == x:
			found = True
	if not found:
		teams_a.append(x)
		teams_b.append(y)

# column 3
x = ""
y = ""
if board[2] == board[5] and board[2] != board[8]:
	x = board[2]
	y = board[8]
elif board[2] == board[8] and board[2] != board[5]:
	x = board[2]
	y = board[5]
elif board[5] == board[8] and board[5] != board[2]:
	x = board[5]
	y = board[2]
if x != "":
	found = False
	for i in range(len(teams_a)):
		if teams_a[i] == x and teams_b[i] == y:
			found = True
		if teams_a[i] == y and teams_b[i] == x:
			found = True
	if not found:
		teams_a.append(x)
		teams_b.append(y)

# diagonal 1
x = ""
y = ""
if board[0] == board[4] and board[0] != board[8]:
	x = board[0]
	y = board[8]
elif board[0] == board[8] and board[0] != board[4]:
	x = board[0]
	y = board[4]
elif board[4] == board[8] and board[4] != board[0]:
	x = board[4]
	y = board[0]
if x != "":
	found = False
	for i in range(len(teams_a)):
		if teams_a[i] == x and teams_b[i] == y:
			found = True
		if teams_a[i] == y and teams_b[i] == x:
			found = True
	if not found:
		teams_a.append(x)
		teams_b.append(y)

# diagonal 2
x = ""
y = ""
if board[2] == board[4] and board[2] != board[6]:
	x = board[2]
	y = board[6]
elif board[2] == board[6] and board[2] != board[4]:
	x = board[2]
	y = board[4]
elif board[4] == board[6] and board[4] != board[2]:
	x = board[4]
	y = board[2]
if x != "":
	found = False
	for i in range(len(teams_a)):
		if teams_a[i] == x and teams_b[i] == y:
			found = True
		if teams_a[i] == y and teams_b[i] == x:
			found = True
	if not found:
		teams_a.append(x)
		teams_b.append(y)


with open("tttt.out", "w") as write:
	print(len(singles), file = write)
	print(len(teams_a), file = write)
