with open("mowing.in") as read:
    n = int(read.readline())
    directions = []
    magnitudes = []
    for _ in range(n):
        d, s = read.readline().split()
        directions.append(d)
        magnitudes.append(int(s))

position = (0, 0)
coordinates = [(0, 0)]
t = 0
answer = float('inf')

for i in range(n):
    for _ in range(magnitudes[i]):
        if directions[i] == "N":
            position = (position[0], position[1] + 1)
        elif directions[i] == "S":
            position = (position[0], position[1] - 1)
        elif directions[i] == "E":
            position = (position[0] + 1, position[1])
        else:
            position = (position[0] - 1, position[1])
        t += 1
        for j in range(len(coordinates) - 1, -1, -1):
            if coordinates[j] == position:
                answer = min(answer, t - j)
                break
        coordinates.append(position)

if answer == float('inf'):
    answer = -1

with open("mowing.out", "w") as write:
    print(answer, file=write)
