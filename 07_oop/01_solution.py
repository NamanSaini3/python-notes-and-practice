class  Car:
    total_car = 0 




    def __init__(self, brand, model): 
        self.__brand = brand
        self.__model = model  
        Car.total_car += 1


    def get_brand(self):
        return self.__brand + "!"




    def full_name(self):
        return f"{self.__brand}  {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    

    @staticmethod # ager staticmethod use kar raha ho to self nahi use karna  inka decorater bol ta hai 
    def general_description():
        return "Car are means of transport"
    



    
    @property
    def model(self):
        return self.__model






class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)   # super use kar ta hn q ki uper kaam ho ga hn uer  isliya
        self.battery_size = battery_size


    def fuel_type(self):
        return "Electric charge"
       


# my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

# print(isinstance(my_tesla, Car))             # puchna naka liya sach hn ya nahi 
# print(isinstance(my_tesla, ElectricCar))








# print(my_tesla.fuel_type())

# my_car = Car("Tata", "Safari")
# my_car.model = "city"
# Car("Tata", "Nexon")

# print(my_car.model) 










# my_car = Car('Toyota', 'Corolla')
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())


# my_new_car = Car("Tata", "Safari")
# print(my_new_car.brand)
# print(my_new_car.model)

# my_super_hero_car = Car("the Batmobile.", "Batman company")
# print(my_super_hero_car.brand)
# print(my_super_hero_car.model)


class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def Engine_info(self):
        return "this is engine"


class ElectricCarTwo(Battery, Engine, Car):
    pass


my_new_tesla = ElectricCarTwo("Tesla", "Model S")
print(my_new_tesla.Engine_info())
print(my_new_tesla.battery_info())