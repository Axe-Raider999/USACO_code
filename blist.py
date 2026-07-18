with open("blist.in") as read:
    n = int(read.readline())

    start = []
    end = []
    bucket = []

    for _ in range(n):
        s, t, b = map(int, read.readline().split())
        start.append(s)
        end.append(t)
        bucket.append(b)

MAX_TIME = 1001
buckets = 0
curr_buckets = 0

for i in range(MAX_TIME):
    if i in start:
        pos = 0
        for j in range(len(start)):
            if start[j] == i:
                pos = j

        needed = bucket[pos]

        if curr_buckets >= needed:
            curr_buckets -= needed
        else:
            buckets += needed - curr_buckets
            curr_buckets = 0

    elif i in end:
        pos = 0
        for j in range(len(end)):
            if end[j] == i:
                pos = j

        curr_buckets += bucket[pos]

with open("blist.out", "w") as write:
    write.write(str(buckets) + "\n")