h = open('day1_input.txt', 'r')
content = h.readlines()

nums=[]

sum = max = 0
count = 1
top_three = [-3, -2, -1]
first_count = 0
flag = False
for line in content:
    if line == '\n':
        count += 1
        min_num = min(top_three)
        index = top_three.index(min_num)
        if sum > min_num:
            top_three[index] = sum
        sum = 0
    else:
        sum += int(line)
result = 0
for elem in top_three:
    result += elem
print(top_three)
print(result)

# sum = max = 0
# count = 1
# n = len(nums)

# for i in range(n-1):
#     if nums[i] == "":
#         count += 1
#         if sum > max:
#             max = sum
#         sum = 0
#     else:
#         sum += nums[i]

# print(max)

