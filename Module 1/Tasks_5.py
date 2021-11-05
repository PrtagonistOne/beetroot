# Task 1
from random import randint

nums = []
while len(nums) != 10:
    nums.append(randint(0, 1000))  # generates 10 random integers and add those to nums

print(f'\nLet\'s find the GREATEST number of them all!\nHere is the random list of numbers: {nums}\n'
      f'And the GREATEST NUMBER of them all is {max(nums)}!\nCongratulations!')

# Task 2
nums_1 = []
nums_2 = []
while len(nums_1) != 10:
    nums_1.append(randint(1, 10))  # generates 10 random integers and add those to nums_1 and nums_2
    nums_2.append(randint(1, 10))
# convert 2 lists into sets to remove duplicates and
# use intersection to create a set of common integers and
# convert the set to list, by the task logic
nums_3 = list(set(nums_1).intersection(set(nums_2)))
print(nums_1)

# Task 3
extracting_nums = list(range(1, 101))  # list of integers from 1 to 100 (including 100)
extracted_nums = []
i = 0
while i != len(extracting_nums):  # find all integers that divided by 7 and not divided by 5
    if extracting_nums[i] % 7 == 0 and extracting_nums[i] % 5 != 0:
        extracted_nums.append(extracting_nums[i])  # and store them in a separate list
    i += 1

print("\nHere is a list of all integers from 1 to 100 that not divided by 5 and divided by 7 -", extracted_nums)
