with open("circlecross.in") as read:
    stuff = read.readline()
    letters = list(stuff)
    if letters[len(letters)-1] == '\n':
        letters.pop()

end = 1000
answer = 0

for i in range(len(letters)):
    start = i
    x = end
    for j in range(len(letters)-1, i, -1):
        if letters[j] == letters[i]:
            end = j
    if x == end:
        continue

    in_between = []

    for j in range(start+1, end):
        in_between.append(letters[j])

    repeats = []
    
    for k in range(len(in_between)):
        if in_between[k] not in repeats:
            repeats.append(in_between[k])
            answer += 1
        elif in_between[k] in repeats:
            answer -= 1

answer = int(answer / 2)


with open("circlecross.out", "w") as write:
    print(answer, file = write)
