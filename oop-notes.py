# Class is the blueprint
# Instance is an Object that is built from a class
# and contains real data.
# An instance of a class is  no longer a blueprint.
# It's an actual object with actual attributes.
# Many instances can be created from a single class.

##### Example#####

class Dog:
    pass

# Assigning properties to the Dog Objects is done through
# the __init__() method. Everytime a new Dog object is created
# dunder init sets the initial state of the object by assigning
# values of the objeect's properties.
# INIT() initializes each new instance(object) of a class.

# self is the python standard paramater. this allows for new
# attributes to be defined on the object.


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# self.name = name creates an attribute called 'name' and assigns
# to it the value of the name parameter. same for age.
# self.name = name is an instance attribute. these are specific
# to a particular instance of the class.

# All Dog objects have a name and an age.
# However, the values for name and age will vary depending on theh Dog instance(object)


class Dog:

    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

# species is a class attribute. this defines a property that should have the same
# value for every class instance(object).
# Use instance attribute for properties that vary from one instance(object) to another.
