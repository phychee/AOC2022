from curses.ascii import isalpha


h = open("/Users/reddik/Documents/AOC2022/day2/input.txt", 'r')
content = h.readlines()

round = []
result = 0
score = 0
count = 0
for line in content:
    for elem in line:
        if isalpha(elem):
            round.append(elem)
    opp = round[0]
    end = round[1]

    if end == 'X':
        score = 0
    elif end == 'Y':
        score = 3
    elif end == 'Z':
        score = 6

    result += score
    if score == 0:
        if opp == 'A':
            result += 3
        if opp == 'B':
            result += 1
        if opp == 'C':
            result += 2
    elif score == 3:
        if opp == 'A':
            result += 1
        if opp == 'B':
            result += 2
        if opp == 'C':
            result += 3
    elif score == 6:
        if opp == 'A':
            result += 2
        if opp == 'B':
            result += 3
        if opp == 'C':
            result += 1

    # if (opp == 'A') and (me == 'X'):
    #     result += 3 + score
    # elif (opp == 'B') and (me == 'Y'):
    #     result += 3 + score
    # elif (opp == 'C') and (me == 'Z'):
    #     result += 3 + score
    # elif (opp == 'A') and (me == 'Y'):
    #     result += 6 + score
    # elif (opp == 'A') and (me == 'Z'):
    #     result += score
    # elif (opp == 'B') and (me == 'X'):
    #     result += score
    # elif (opp == 'B') and (me == 'Z'):
    #     result += 6 + score
    # elif (opp == 'C') and (me == 'X'):
    #     result += 6 + score
    # elif (opp == 'C') and (me == 'Y'):
    #     result += score
    round = []

print(result)



