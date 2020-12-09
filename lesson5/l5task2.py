# Task 2
# Exclusive common numbers.
# Generate 2 lists with the length of 10 with random integers from 1 to 10,
# and make a third list containing the common integers between the 2 initial lists without any duplicates.
# Constraints: use only while loop and random module to generate numbers

import random
x = 0
list_of_numbers = []
list_of_numbers_two = []
list_of_numbers_res = []
while x < 10:
    list_of_numbers.append(random.randint(1, 10))
    list_of_numbers_two.append(random.randint(1,10))
    x += 1

x = 0
while x < 10:
    if list_of_numbers[x] in list_of_numbers_two and not list_of_numbers[x] in list_of_numbers_res:
        list_of_numbers_res.append(list_of_numbers[x])
    x += 1
print(list_of_numbers, list_of_numbers_two, sep='\n')
print('Result =', list_of_numbers_res)