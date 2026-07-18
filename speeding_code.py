with open("speeding.in") as read:
    number_segments, number_drove_segments = map(int, read.readline().split())
    limits = []
    for _ in range(number_segments):
        length, speed = map(int, read.readline().split())
        limits.extend([speed] * length)
    driven = []
    for _ in range(number_drove_segments):
        length, speed = map(int, read.readline().split())
        driven.extend([speed] * length)
worst = 0
for i in range(len(limits)):
    if driven[i] > limits[i]:
        worst = max(worst, driven[i] - limits[i])
with open("speeding.out", "w") as write:
    print(worst, file=write)