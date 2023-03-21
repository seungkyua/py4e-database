import re

# handle = open('regex_sum_42.txt')
handle = open('regex_sum_1745051.txt')
# data = handle.read()
# # print(data)
#
# nums = re.findall('([0-9]+)', data)
# # print(nums)
# sum = 0
# for num in nums:
#     sum += int(num)
# print(sum)

print(sum([int(num) for num in re.findall('([0-9]+)', handle.read())]))
