# USACO 2025 February Contest, Bronze - Problem 1: Reflection

# --- N input section ---------------------------------------------------
# Read everything up front: input() only moves forward, and group r needs
# row r AND row n-1-r, which sit at opposite ends of the input.
n, u = map(int, input().split())
grid = [input() for _ in range(n)]

half = n // 2


def scan():
    total = 0

    # --- line up the mirror groups -------------------------------------
    # n//2 iterations, so each group is visited exactly once.
    for r in range(half):
        top = grid[r]
        bot = grid[n - 1 - r]

        # Reversing the right halves makes index c line up with column n-1-c,
        # so position c of all four strings is one set of mirror partners.
        top_left = top[:half]
        top_right = top[half:][::-1]
        bot_left = bot[:half]
        bot_right = bot[half:][::-1]

        for c in range(half):
            tl = top_left[c]    # row r,     col c
            tr = top_right[c]   # row r,     col n-1-c
            bl = bot_left[c]    # row n-1-r, col c
            br = bot_right[c]   # row n-1-r, col n-1-c

            hashes = [tl, tr, bl, br].count("#")

            if hashes == 1 or hashes == 3:
                total += 1
            elif hashes == 2:
                total += 2

    return total


# --- U section ----------------------------------------------------------
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
