# Write a Python function that accepts a list of integers and a target sum.
# The function should return True if there are two distinct numbers in the list that add up to the target sum,
# and False otherwise.

def has_pair_with_sum(lst, target):
    seen = set()
    for num in lst:
        complement = target - num
        if complement in seen:
            return True
        seen.add(num)
    return False


numbers = [10, 13, 15, 19]
target_sum = 29
print(has_pair_with_sum(numbers, target_sum))
