class Vehicle():
    def __init__(self, brand="",passengers=0,wheels=0,price=0,productionyear=0,color="",speed=0):
        self._brand = brand
        self._passengers = passengers
        self._wheels = wheels
        self._price= price
        self._productionyear = productionyear
        self._color = color
        self._speed = speed
    # getter method of Brand
    def get_brand(self):
        return self._brand
    # setter method of Brand
    def set_brand(self, x):
        self._brand = x

    # getter method of Passengers
    def get_passengers(self):
        return self._passengers
    # setter method of Passengers
    def set_passengers(self, x):
        self._passengers = x

    # getter method of Wheels
    def get_wheels(self):
        return self._wheels
    # setter method of Wheels
    def set_wheels(self, x):
        self._wheels = x

    # getter method of Price
    def get_price(self):
        return self._price
    # setter method of Wheels
    def set_price(self, x):
        self._price = x

    # getter method of Productionyear
    def get_productionyear(self):
        return self._productionyear
    # setter method of Productionyear
    def set_productionyear(self, x):
        self._productionyear = x

    # getter method of Color
    def get_color(self):
        return self._color
    # setter method of Productionyear
    def set_color(self, x):
        self._color = x

    # getter method of Speed
    def get_speed(self):
        return self._speed
    # setter method of Speed
    def set_speed(self, x):
        self._speed = x


    #Vehicle Functions
    def __acceleration__(self,speed):
        pass

    def __slowdown__(self,speed):
        pass

    def __stoped__(self):
        pass
