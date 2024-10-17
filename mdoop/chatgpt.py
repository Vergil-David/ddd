# я юзнув його 
from abc import ABC, abstractmethod

class Vehicle:
    def __init__(self):
        self.make = None
        self.model = None
        self.year = None

    def show_info(self):
        print(f"Vehicle Make: {self.make}")
        print(f"Vehicle Model: {self.model}")
        print(f"Vehicle Year: {self.year}")

class VehicleBuilder(ABC):
    def __init__(self):
        self._vehicle = Vehicle()

    def create_vehicle(self):
        self._vehicle = Vehicle()

    @abstractmethod
    def set_make(self):
        pass

    @abstractmethod
    def set_model(self):
        pass

    @abstractmethod
    def set_year(self):
        pass

    def get_vehicle(self):
        return self._vehicle

class FordExplorerBuilder(VehicleBuilder):
    def set_make(self):
        self._vehicle.make = "Ford"

    def set_model(self):
        self._vehicle.model = "Explorer"

    def set_year(self):
        self._vehicle.year = 2024

class LincolnAviatorBuilder(VehicleBuilder):
    def set_make(self):
        self._vehicle.make = "Lincoln"

    def set_model(self):
        self._vehicle.model = "Aviator"

    def set_year(self):
        self._vehicle.year = 2024

class VehicleCreator:
    def __init__(self, builder: VehicleBuilder):
        self._builder = builder

    def create_vehicle(self):
        self._builder.create_vehicle()
        self._builder.set_make()
        self._builder.set_model()
        self._builder.set_year()

    def get_vehicle(self):
        return self._builder.get_vehicle()

if __name__ == "__main__":
    ford_builder = FordExplorerBuilder()
    creator = VehicleCreator(ford_builder)
    creator.create_vehicle()
    ford_explorer = creator.get_vehicle()
    ford_explorer.show_info()

    print()

    lincoln_builder = LincolnAviatorBuilder()
    creator = VehicleCreator(lincoln_builder)
    creator.create_vehicle()
    lincoln_aviator = creator.get_vehicle()
    lincoln_aviator.show_info()
