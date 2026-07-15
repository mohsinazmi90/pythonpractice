class Animal:
    def __init__(self, type: str, name: str, age: int, noise: str):
        self.type = type
        self.name = name
        self.age = age
        self.noise = noise

    def get_animal_type(self):
        return f'{self.name} is a {self.type} and makes "{self.noise}" sounds'.title()


max = Animal("Dog", "Max", 2, "Woof")
twix = Animal("Cat", "Twix", 7, "Meow")

print(max.get_animal_type())
print(twix.get_animal_type())
