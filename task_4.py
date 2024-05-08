'''
4 Write a program that asks the user for a list of numbers and then outputs only even numbersCreate two lists of numbers and merge them into one new list. 
Then sort this new list in ascending order.a from this list.
'''

my_list1 = [2, 4, 1, 3, 5]
my_list2 = [6, 7, 8, 9, 10]
my_list3 = my_list1 + my_list2
my_list3.sort()
print(my_list3)