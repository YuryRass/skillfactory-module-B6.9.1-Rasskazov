class Cat:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
    def print_info(self):
        print ("Имя: ", self.name)
        print ("Пол: ", self.gender)
        print ("Возраст: ", self.age)
        print("-" * 10)

from math import pi
class Circle:
    def __init__(self, R):
        self.R = R
    def get_squary(self):
        return pi * self.R ** 2
    