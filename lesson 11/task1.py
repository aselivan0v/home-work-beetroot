# Task 1
# School
# Make a class structure in python representing people at school.
# Make a base class called Person, a class called Student, and another one called Teacher.
# Try to find as many methods and attributes as you can which belong to different classes,
# and keep in mind which are common and which are not. For example, the name should be a Person attribute,
# while salary should only be available to the teacher.

class Person:
    def __init__(self, age, ferst_name, last_name):
        self.age = age
        self.ferst_name = ferst_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.age}, {self.ferst_name}, {self.last_name}'


class Teacher(Person):
    def __init__(self, age, ferst_name, last_name, experts_in, salary):
        super().__init__(age, ferst_name, last_name)
        self.salary = salary
        self.experts_in = experts_in

    def __str__(self):
        return f'{self.ferst_name} {self.last_name} is specialists in their field of {self.experts_in}. ' \
               f'Salary teacher = {self.salary} grn'


class Student(Teacher):
    def __init__(self, age, ferst_name, last_name, homework, hobby):
        super(Teacher, self).__init__(age, ferst_name, last_name)
        self.homework = homework
        self.hobby = hobby

    def __str__(self):
        return f'{self.ferst_name} {self.last_name}. Home work - {self.homework}. Hobby = {self.hobby}'


human_1 = Person(25, 'Artem', 'Selivanov')
human_2 = Teacher(70, 'Oleg', 'Li', 'Botany', 80000)
human_3 = Student(25, 'Mark', 'Kurt', 'English', 'music')
print(human_1)
print(human_2)
print(human_3)