from Vehicle import Vehicle


class LandVehicle(Vehicle):
    def __init__(self,brand="", passengers=0, wheels=0,price=0,productionyear=0,color="", speed=0):
        super().__init__(brand, passengers, wheels,price,productionyear,color, speed)
