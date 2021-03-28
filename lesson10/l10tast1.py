# Task 1
# A Person class
# Make a class called Person. Make the __init__() method take firstname,
# lastname, and age as parameters and add them as attributes.
# Make another method called talk() which makes prints a greeting from the person containing,
# for example like this: “Hello, my name is Carl Johnson and I’m 26 years old”.


class Person:
    def __init__(self, FirstName, LastName, Age):
        self.First_Name = FirstName
        self.Last_Name = LastName
        self.Age = Age

    def Tolk(self):
        print(f"Hello, my name is {self.First_Name} {self.Last_Name} and I’m {self.Age} years old.")

test = Person('Artem', 'Selivanov', '24')
test.Tolk()