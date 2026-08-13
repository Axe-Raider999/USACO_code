with open("lifeguards.in") as read:
    n = int(read.readline())

    points = []

    for i in range(n):
        start, end = map(int, read.readline().split())
        points.append((start, end))

t = [0] * 1001

for i in range(len(points)):
    start, end = points[i]

    for j in range(start, end):
        t[j] += 1

answer = 0

for i in range(len(points)):
    cur_answer = 0
    t_minuscow = t.copy()

    start, end = points[i]

    for j in range(start, end):
        t_minuscow[j] -= 1

    for j in range(len(t_minuscow)):
        if t_minuscow[j] > 0:
            cur_answer += 1

    answer = max(answer, cur_answer)

with open("lifeguards.out", "w") as write:
    print(answer, file = write)
