n, u = map(int, input().split())
grid = [input() for _ in range(n)]

half = n // 2


def scan():
    total = 0

    for r in range(half):
        top = grid[r]
        bot = grid[n - 1 - r]

        top_left = top[:half]
        top_right = top[half:][::-1]
        bot_left = bot[:half]
        bot_right = bot[half:][::-1]

        for c in range(half):
            tl = top_left[c]
            tr = top_right[c]
            bl = bot_left[c]
            br = bot_right[c]

            hashes = [tl, tr, bl, br].count("#")

            if hashes == 1 or hashes == 3:
                total += 1
            elif hashes == 2:
                total += 2

    return total


print(scan())

for _ in range(u):
    r, c = map(int, input().split())
    r -= 1
    c -= 1

    if grid[r][c] == "#":
        grid[r] = grid[r][:c] + "." + grid[r][c + 1:]
    else:
        grid[r] = grid[r][:c] + "#" + grid[r][c + 1:]

    print(scan())
