from Vehicle import Vehicle


class AirVehicle(Vehicle):
    def __init__(self, brand="", passengers=0, wheels=0, price=0, productionyear=0, color="", speed=0):
        super().__init__(brand, passengers, wheels, price, productionyear, color, speed)

    def __IsOnLand__(self,flag):
        if flag:
            super().__stoped__()
        if not flag:
            print("Air vehicle cannot stop in the sky")



