#Task 3
#Extracting numbers.
#Make a list that contains all integers from 1 to 100,
#then find all integers from the list that are divisible by 7 but not a multiple of 5,
#and store them in a separate list. Finally, print the list.
#Constraint: use only while loop for iteration

my_list = list(range(1, 101))
final_list = []
x = 0
while x < len(my_list):
    if not my_list[x] % 7 and my_list[x] % 5:
        final_list.append(my_list[x])
    x += 1

print(final_list)