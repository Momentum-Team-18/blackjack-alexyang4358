class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"


miles = Dog("Miles", 4)


class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f'A {self.color} car with {self.mileage} miles'


car1 = Car(color="Blue", mileage="20,000")
car2 = Car(color="Red", mileage="30,000")

for car in (car1, car2):
    print(f'The {car.color} car has {car.mileage} miles')
