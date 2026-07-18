# USACO 2019 February Bronze - Problem 3: Measuring Traffic
#
# Traffic flows mile 1 -> N. Each segment transforms the flow:
#   none [a,b] : flow on the main highway here, so it must lie in [a,b]
#   on   [a,b] : an on-ramp adds between a and b cars  -> after = before + [a,b]
#   off  [a,b] : an off-ramp removes between a and b   -> after = before - [a,b]
#
# We carry a [lo, hi] range and squeeze it as we pass each segment.

INF = 10**9

with open("traffic.in") as read:
    n = int(read.readline())
    segments = []
    for _ in range(n):
        ramp, a, b = read.readline().split()
        segments.append((ramp, int(a), int(b)))


def clamp(lo, hi):
    # traffic can never be negative
    return max(lo, 0), hi


# --- Range BEFORE mile 1: start unknown after mile N, walk backwards ---
lo, hi = 0, INF
for ramp, a, b in reversed(segments):
    if ramp == "none":
        lo, hi = max(lo, a), min(hi, b)      # flow here equals the reading
    elif ramp == "on":
        lo, hi = clamp(lo - b, hi - a)       # before = after - added
    else:  # off
        lo, hi = clamp(lo + a, hi + b)       # before = after + removed
before = (lo, hi)

# --- Range AFTER mile N: start unknown before mile 1, walk forwards ---
lo, hi = 0, INF
for ramp, a, b in segments:
    if ramp == "none":
        lo, hi = max(lo, a), min(hi, b)
    elif ramp == "on":
        lo, hi = clamp(lo + a, hi + b)       # after = before + added
    else:  # off
        lo, hi = clamp(lo - b, hi - a)       # after = before - removed
after = (lo, hi)

with open("traffic.out", "w") as write:
    print(before[0], before[1], file=write)
    print(after[0], after[1], file=write)
