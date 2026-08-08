with open("cownomics.in") as read:
    n, m = map(int, read.readline().split())

    spotted = []
    plain = []

    for _ in range(n):
        spotted.append(read.readline().strip())
    for _ in range(n):
        plain.append(read.readline().strip())

poi = 0
repeat = False

for j in range(m):
    cur_spotted_genomes = []
    cur_plain_genomes = []

    for i in range(n):
        cur_spotted_genomes.append(spotted[i][j])
        cur_plain_genomes.append(plain[i][j])

    repeat = False
    for genome in cur_spotted_genomes:
        if genome in cur_plain_genomes:
            repeat = True

    if not repeat:
        poi += 1

with open("cownomics.out", "w") as write:
    write.write(str(poi) + "\n")
