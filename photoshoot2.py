n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

moves = 0
for i in range(n):
    if a[i] != b[i]:
        j = a.index(b[i], i)
        val = a.pop(j)
        a.insert(i, val)
        moves += 1

print(moves)
