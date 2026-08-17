with open("promote.in") as read:
    _ = read.readline()
    starts = []
    ends = []
    for i in range(3):
        start, end = map(int, read.readline().split())
        starts.append(start)
        ends.append(end)

plat = ends[2] - starts[2]
gold = ends[1] - starts[1] + plat
silver = ends[0] - starts[0] + gold

with open("promote.out", "w") as write:
    print(silver, file = write)
    print(gold, file = write)
    print(plat, file = write)
