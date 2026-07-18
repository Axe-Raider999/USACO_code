with open("cbarn.in") as read:
    n = int(read.readline())
    r = []
    for _ in range(n):
        r.append(int(read.readline()))

total_steps = float('inf')
for i in range(n):
    this_iteration = 0
    step = 0
    for j in range(i, n):
        this_iteration += r[j] * step
        step += 1
    for k in range(i):
        this_iteration += r[k] * step
        step += 1
    total_steps = min(this_iteration, total_steps)

with open("cbarn.out", "w") as write:
    print(total_steps, file=write)

