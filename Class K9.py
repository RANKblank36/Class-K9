class K9:

    # class attribute
    species = "dog"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# instantiate the Parrot class
blue = K9("Blue", 11)
woop = K9("Woop", 14)

# access the class attributes
print("Blue is a {}".format(blue.species))
print("Woop is also a {}".format(woop.species))

# access the instance attributes
print("{} is {} years old".format( blue.name, blue.age))
print("{} is {} years old".format( woop.name, woop.age))
