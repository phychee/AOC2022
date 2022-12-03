h = open("/Users/reddik/Documents/AOC2022/day3/input.txt", 'r')
content = h.readlines()

alpha = "@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# result = 0
# for line in content:
#     n = (len(line) // 2)
#     seen = ""
#     count1 = 0
#     count2 = n
#     seen += line[:n]
#     while (count2 < len(line)):
#         if (seen.find(line[count2]) != -1):
#             result += alpha.find(line[count2])
#             break
#         count2 += 1

tracker = 0
result = 0
seen2 = ""
for line in content:
    if tracker == 2:
        tracker = 0
        for i in line:
            if (seen2.find(i) != -1):
                result += alpha.find(i)
                break
    elif tracker == 0:
        seen = ""
        seen += line
        tracker += 1
    elif tracker == 1:
        seen2 = ""
        for i in line:
            if (seen.find(i) != -1):
                seen2 += i
        tracker += 1

print(result)
        

