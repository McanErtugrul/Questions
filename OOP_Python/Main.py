from Motor_LandVehicle import Motor_LandVehicle
from AirVehicle import AirVehicle
from SeaAirVehicle import SeaAirVehicle
from SeaVehicle import SeaVehicle

car1 = Motor_LandVehicle()

car1.set_brand("Renault")
car1.set_passengers(4)
car1.set_wheels(4)
car1.set_price(500000)
car1.set_productionyear(2019)
car1.set_color("red")
car1.set_speed(240)
car1.set_fueltype("diesel")

print("About \n Brand : {} \n Passengers : {} \n Wheels : {} \n Price : {} \n"
      " Production Year : {} \n Color : {} \n Speed : {} \n Fuel Type : {}"
      .format(car1.get_brand(), car1.get_passengers(), car1.get_wheels(),
              car1.get_price(), car1.get_productionyear(),car1.get_speed(), car1.get_color(),car1.get_fueltype() ))
