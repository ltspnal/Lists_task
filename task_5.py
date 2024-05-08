# 5 Write a function that takes a list of numbers as an argument and returns the sum of all numbers in the list.

numbers = [int (x) for x in input("Enter numbers separated by spaces: ").split()]
total = sum(numbers)
print("Summary:", total)