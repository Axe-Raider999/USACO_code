n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

pos = {}
for i in range(n):
    pos[b[i]] = i

targets = []
for i in range(n):
    targets.append(pos[a[i]])

safe = 0
best = -1
for value in targets:
    if value > best:
        best = value
        safe += 1

print(n - safe)
