# Write a function called remove_duplicates that takes a list as input and
# returns a new list with all duplicate elements removed.
# You cannot use the set function to solve this problem.

def remove_duplicates(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

input_list = [10, 20, 30, 30, 40, 40, 50, 60, 70]
print(remove_duplicates(input_list))  # Output: [10, 20, 30, 40, 50, 60, 70]
