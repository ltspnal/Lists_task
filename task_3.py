# 3 Write a program that asks the user for a list of numbers and then outputs only the even numbers from that list.

numbers = [int (x) for x in input("Enter a list of numbers separated by space: ").split()]
even_numbers = [num for num in numbers if num % 2 == 0]
print("Even numbers in the list:", even_numbers)
