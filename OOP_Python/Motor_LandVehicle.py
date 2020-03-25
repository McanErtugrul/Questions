from LandVehicle import LandVehicle

class Motor_LandVehicle(LandVehicle):
    def __init__(self, brand="", passengers=0, wheels=0, price=0, productionyear=0, color="", speed=0, fueltype=""):
        super().__init__(brand, passengers, wheels, price, productionyear, color, speed)
        self._fueltype=fueltype

        # getter method of Brand
    def get_fueltype(self):
        return self._fueltype
        # setter method of Brand
    def set_fueltype(self, x):
        self._fueltype = x