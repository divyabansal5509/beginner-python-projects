#1. Basic class and object: Create a class car with attributes like __brand and model. Then create an instance of the class.
#2. Class method and self: Add a method to  Car class that displays the full name of class(__brand and model).
#3. Inheritance : Create an Electric car that inherits from the Car class and has an additional attribute battery_size.
#4. Encapsulation: Modify the car class to encapsulate the brand attribute,making it private ,and providing the getter amd setter method for it.
#5. Polymorphism:Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.
#6. Class Variable : Add a class variable to Car that tracks the record of the number of car created.
#7. Static Method: Add a static method to the Car class that returns a general description of a car.
#8. Property Decorators: Use a property decorator in the Car class to make the model attribute read-only.
#9. Class Inheritance and is instance() Function: Demonstrate the use of isinstance) to check if my _tesla is an instance of Car and ElectricCar.
#10. Multiple Inheritance:Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.




class Car:
    
    total_Car = 0
    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model
        Car.total_Car+=1
        
    def get_brand(self):
        return self.__brand + " "
    
    def set_brand(self):
        if self.__brand == "Toyota":
            self.__brand = "Swift"
            return self.__brand + ". "
        
    def full_name(self):
        return f"{self.__brand} {self.__model} "
    
    def fuel_charge(self):
        return "Petrol or CNG"
    
    @staticmethod
    def general_description():
        return "This have a number of high ranked Cars."
    
    @property
    def model(self):
        return self.__model
    
class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
        
    def fuel_charge(self):
        return "Electric Charge"


# my_tesla = ElectricCar("Tesla","Model S","85 kWH")

# print(isinstance(my_tesla,Car))
# print(isinstance(my_tesla,ElectricCar))
# print(my_tesla.model)
# print(my_tesla.battery_size)
# print(my_tesla.full_name())
# print(my_tesla.fuel_charge())
        
# safari = Car("Tata","Safari")
# print(safari.fuel_charge())
# print(Car.total_Car)
# print(Car.general_description())

# print(safari.model)
        
# my_car = Car("Toyota","Corolla")
# print(my_car.get_brand())
# print(my_car.set_brand())
# print(my_car.model)
  
# my_new_car = Car("Tata","Safari")
# print(my_new_car.get_brand)
# print(my_new_car.full_name())

class Battery:
    def battery_info():
        return "This is battery."

class Engine:
    def engine_info():
        return "This is Engine."

class ElectricCar2(Battery,Engine,Car):
    pass

my_new_tesla = ElectricCar2("Tesla","Model S")
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())
