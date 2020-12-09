# The greatest number
# Write a Python program to get the largest number from a list of random numbers with the length of 10
# Constraints: use only while loop and random module to generate numbers
import random

list_of_numbers = []
while len(list_of_numbers) < 10:
    number = random.randint(0, 10000)
    list_of_numbers.append(number)
print(list_of_numbers)
print(max(list_of_numbers))