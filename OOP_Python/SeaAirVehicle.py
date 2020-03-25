from SeaVehicle import SeaVehicle
from AirVehicle import AirVehicle


class SeaAirVehicle(SeaVehicle,AirVehicle):
    def __init__(self, brand="", passengers=0, wheels=0, price=0, productionyear=0, color=""):
        super().__init__(brand, passengers, wheels, price, productionyear, color)
