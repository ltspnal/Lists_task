# 8 Create a list of numbers and replace all negative numbers with 0.

my_list = [1, 2, -10, -100, 3, -101, -9, 10]
modified_numbers = [num if num >= 0 else 0 for num in my_list]
print(modified_numbers)