# ! Sum Fractions
#  todoCreate a function that takes a list containing nested lists as an argument.
#  todo Each sublist has 2 elements. The first element is the numerator and the second element is the denominator.
# todo Return the sum of the fractions rounded to the nearest whole number.

# ! Examples
# * sum_fractions([[18, 13], [4, 5]]) ➞ 2

# * sum_fractions([[36, 4], [22, 60]]) ➞ 9

# * sum_fractions([[11, 2], [3, 4], [5, 4], [21, 11], [12, 6]]) ➞ 11
# ! Notes
# ? Your result should be a number not string.






def sum_fractions(lst):
    sum_ = []
    for item in lst:
        if isinstance(item, list) and len(item) == 2:
             sum_.append(item[0]/item[1])
    return round(sum(sum_ )) # In case no list is found

print(sum_fractions([[11, 2], [3, 4], [5, 4], [21, 11], [12, 6]]))
print(sum_fractions([[18, 13], [4, 5]]))
print(sum_fractions([[36, 4], [22, 60]]))

# ! /////////////////////////////////////////////////////////////////////////////////

def sum_fractions(lst):
    total = 0  # Initialize the total to zero
    for item in lst:
        if isinstance(item, list) and len(item) == 2:
            total += item[0] / item[1]  # Add each fraction directly to the total
    return round(total)

# Test cases
print(sum_fractions([[11, 2], [3, 4], [5, 4], [21, 11], [12, 6]]))  # ➞ 11
print(sum_fractions([[18, 13], [4, 5]]))  # ➞ 2
print(sum_fractions([[36, 4], [22, 60]]))  # ➞ 9


#! /////////////////////////////////////////////////////////////////////////////////

def sum_fractions(lst):
    total = 0
    for fraction in lst:
        numerator, denominator = fraction
        total += numerator / denominator
    return round(total)

# Test cases
print(sum_fractions([[18, 13], [4, 5]]))  # ➞ 2
print(sum_fractions([[36, 4], [22, 60]]))  # ➞ 9
print(sum_fractions([[11, 2], [3, 4], [5, 4], [21, 11], [12, 6]]))  # ➞ 11
