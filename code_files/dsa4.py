# Find Odd's From The Given List.

list_nums = [3, 2, 5, 2, 1, 54, 16, 34, 89, 5, 7, 4]
res = []

for i in range(len(list_nums)):
    if list_nums[i] % 2 != 0:
        res.append(list_nums[i])

print(res)
