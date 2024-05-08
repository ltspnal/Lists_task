# 10 Create a list and see if it contains at least one number that is a multiple of 5.

my_list1 = [1, 2, 10, 16, 17, 20, 25, 30]
my_list2 = []

for x in my_list1:
    if x % 5 == 0:
        my_list2.append(x)

print(my_list2)
