with open("cowtip.in") as read:
    n = int(read.readline())
    rows = [list(map(int, read.readline().strip())) for _ in range(n)]

answer = 0
while any(1 in row for row in rows):
    lowest = 0
    for i in range(n):
        if 1 in rows[i]:
            lowest = i
    rightmost_in_row = 0
    for j in range(n):
        if rows[lowest][j] == 1:
            rightmost_in_row = j

    rightmost = 0
    for j in range(n):
        for i in range(n):
            if rows[i][j] == 1:
                rightmost = j
    lowest_in_col = 0
    for i in range(n):
        if rows[i][rightmost] == 1:
            lowest_in_col = i

    R = lowest
    C = rightmost

    for i in range(R + 1):
        for j in range(C + 1):
            rows[i][j] ^= 1
    answer += 1

with open("cowtip.out", "w") as write:
    write.write(str(answer) + "\n")
