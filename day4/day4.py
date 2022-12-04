from curses.ascii import isdigit


h = open("/Users/reddik/Documents/AOC2022/day4/input.txt", 'r')
content = h.readlines()

# arr1 = []
# arr2 = []
# string = ""
# flag = False
# result = 0
# for line in content:
#     for char in line:
#         if char == '-':
#             if flag == True:
#                 arr2.append(int(string))
#                 string = ""
#             else:
#                 arr1.append(int(string))
#                 string = ""
#         elif char == ',':
#             flag = True
#             arr1.append(int(string))
#             string = ""
#         elif char == '\n':
#             arr2.append(int(string))
#             string = ""
#         else:
#             string += char
#     if ((arr1[0] <= arr2[0]) and (arr1[1] >= arr2[1]) or 
#     (arr2[0] <= arr1[0]) and (arr2[1] >= arr1[1])):
#         result += 1
#     arr1 = []
#     arr2 = []
#     flag = False

# print(result)

result = 0
arr = []
string = ""
for line in content:
    arr = []
    for char in line:
        if char == '-' or char == ',':
            arr.append(int(string))
            string = ""
        elif char == '\n':
            arr.append(int(string))
            string = ""
        else:
            string += char
    minarr = min(arr)
    maxarr = max(arr)
    diff1 = maxarr - minarr
    diff2 = (arr[1] - arr[0]) + (arr[3] - arr[2])
    if diff2 >= diff1:
        result += 1

print(result)