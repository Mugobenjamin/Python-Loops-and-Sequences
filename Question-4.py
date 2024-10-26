# Write a function that accepts a list of strings and returns a new list where each string is reversed.
# For example, for the input ["apple", "banana", "cherry"], the function should return ["elppa", "ananab", "yrrehc"].

def reverse_strings(strings):
    reversed_list = [s[::-1] for s in strings]
    return reversed_list

input_list = ["apple", "banana", "cherry"]
print(reverse_strings(input_list))
