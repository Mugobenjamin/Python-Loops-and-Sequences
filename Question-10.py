# Write a function that takes a list of tuples as input from the user,
# where each tuple contains two elements: a string and an integer (e.g., ("apple", 5)).
# The function should return a dictionary where the strings are the keys and the integers are the values.

def tuples_to_dict(tuples_list):
    """
    Convert a list of tuples into a dictionary.
    
    Parameters:
    tuples_list (list): A list of tuples, where each tuple contains a string and an integer.
    
    Returns:
    dict: A dictionary with strings as keys and integers as values.
    """
    return {key: value for key, value in tuples_list}

input_tuples = [("apple", 5), ("banana", 3), ("orange", 4)]
result_dict = tuples_to_dict(input_tuples)
print(result_dict)
