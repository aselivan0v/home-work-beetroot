# Doggy age
# Create a class Dog with class attribute `age_factor` equals to 7. Make __init__() which takes values for a dog’s age.
# Then create a method `human_age` which returns the dog’s age in human equivalent.


class Dog:
    age_factor = 7

    def __init__(self, DogsAge):
        self.Dogs_Age = DogsAge

    def human_age(self):
        return f'Human age = {self.Dogs_Age * Dog.age_factor}'


test = Dog(3)
print(test.human_age())

test2 = Dog(9)
print(test2.human_age())