
from curses.ascii import isalpha, isspace


h = open("/Users/reddik/Documents/AOC2022/day5/input.txt", 'r')
content = h.readlines()

flag = False
track = 1
count = 0
for line in content:
    if line != "\n" and not flag:
        x = line.split("\n\n")
        if (isalpha(x[0][track]) or isspace(x[0][track])):
            count += 1
        track += 4
    elif flag:
        y = line.split()
    else:
        flag = True
    
