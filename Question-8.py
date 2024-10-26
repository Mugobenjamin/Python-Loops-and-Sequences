# Write a function that takes a dictionary and an integer n as input
# and returns a list of keys from the dictionary where the value is greater than n.
# For example, for the dictionary {'a': 5, 'b': 12, 'c': 3} and n = 4, the function should return ['a', 'b'].

def keys_with_values_greater_than(d, n):
    keys_list = [key for key, value in d.items() if value > n]
    return keys_list

sample_dict = {'a': 5, 'b': 12, 'c': 3}
n = 4
print(keys_with_values_greater_than(sample_dict, n))
