INF = 10**9

with open("traffic.in") as read:
    n = int(read.readline())
    segments = []
    for _ in range(n):
        ramp, a, b = read.readline().split()
        segments.append((ramp, int(a), int(b)))


def clamp(lo, hi):
    return max(lo, 0), hi


lo, hi = 0, INF
for ramp, a, b in reversed(segments):
    if ramp == "none":
        lo, hi = max(lo, a), min(hi, b)
    elif ramp == "on":
        lo, hi = clamp(lo - b, hi - a)
    else:
        lo, hi = clamp(lo + a, hi + b)
before = (lo, hi)

lo, hi = 0, INF
for ramp, a, b in segments:
    if ramp == "none":
        lo, hi = max(lo, a), min(hi, b)
    elif ramp == "on":
        lo, hi = clamp(lo + a, hi + b)
    else:
        lo, hi = clamp(lo - b, hi - a)
after = (lo, hi)

with open("traffic.out", "w") as write:
    print(before[0], before[1], file=write)
    print(after[0], after[1], file=write)
