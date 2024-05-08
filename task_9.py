# 9 Write a program that accepts two lists and returns a list containing only common elements from both lists.

my_list1 = ["Mama", 1, 8, 9, "Cat", "Car"]
my_list2 = [123, 12, "Python", "Cat", "Audi"]
my_list3 = []
for i in my_list1:
    for k in my_list2:
        if i == k:
            my_list3.append(i)
            break
        
print(my_list3)