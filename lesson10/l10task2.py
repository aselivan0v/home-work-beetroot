# Doggy age
# Create a class Dog with class attribute `age_factor` equals to 7. Make __init__() which takes values for a dog’s age.
# Then create a method `human_age` which returns the dog’s age in human equivalent.


class Dog:
    age_factor = 7
    def __init__(self, dogs_age):
        self.dogs_age = dogs_age

    def Humen_age(self):
        return (f'Humen age = {self.dogs_age * Dog.age_factor}')

test = Dog(3)
print(test.Humen_age())

test2 = Dog(9)
print(test2.Humen_age())