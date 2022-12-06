h = open("/Users/reddik/Documents/AOC2022/day6/input.txt", 'r')
content = h.readlines()

def has_duplicate(window):
    if len(window) == len(set(window)):
        return False
    else:
        return True

nums = []
p1 = 0
p2 = 14
result = 14
for line in content:
    for char in line:
        nums.append(char)

print(nums[p1:p2])
n = len(nums)
while p2 <= n:
    if has_duplicate(nums[p1:p2]):
        result += 1
    else:
        #result += 1
        break
    p1 += 1
    p2 += 1

print(result)
    
