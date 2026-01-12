# Create a class Vehicle with an attribute speed and a method show_speed().
# Create a child class Car that inherits from Vehicle and adds an attribute brand.
# Create an object of Car and display both the brand and speed


class Vehicle:
    def __init__(self,speed):
        self.speed = speed

    def show_speed(self):
        return self.speed    


class Car(Vehicle):
    def __init__(self,speed,brand):
        super().__init__(speed)
        self.brand = brand

car_1 = Car(80,"Nano")

print("Brand",car_1.brand)
print("Speed",car_1.show_speed())