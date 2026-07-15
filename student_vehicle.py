from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model
        self.__fuel = 100

    def get_fuel(self):
        return f"Fuel Level: {self.__fuel}%"

    @abstractmethod
    def move(self):
        pass


class Car(Vehicle):
    def __init__(self, make: str, model: str, doors: int):
        super().__init__(make, model)
        self.doors = doors

    def move(self):
        return f"The {self.make} {self.model} drives forward on 4 wheels."


class Boat(Vehicle):
    def move(self):
        return f"The {self.make} {self.model} moves forward using propellers."


class Airplane(Vehicle):
    def __init__(self, make: str, model: str, size: str):
        super().__init__(make, model)
        self.size = size

    def move(self):
        return f"The {self.make} {self.model} moves forward using jet engines."


if __name__ == "__main__":
    my_car = Car("Tesla", "Model 3", 4)
    my_boat = Boat("Yamaha", "212x")
    my_plane = Airplane("Airbus", "A380", "Jumbojet")

    garage = [my_car, my_boat, my_plane]

    for vehicle in garage:
        print(vehicle.move())
        print(vehicle.get_fuel())
        print("-" * 40)
