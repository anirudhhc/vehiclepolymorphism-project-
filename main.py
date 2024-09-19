class BMW:
    def start(self):
        return "BMW starts with a roar!"
    
    def stop(self):
        return "BMW stops smoothly."

    def speed(self):
        return "BMW has a top speed of 250 km/h."


class Ferrari:
    def start(self):
        return "Ferrari starts with a powerful engine sound!"
    
    def stop(self):
        return "Ferrari stops with high-performance brakes."

    def speed(self):
        return "Ferrari has a top speed of 350 km/h."


# Polymorphism in action
def car_details(car):
    print(car.start())
    print(car.stop())
    print(car.speed())


# Creating objects of both classes
bmw_car = BMW()
ferrari_car = Ferrari()

# Demonstrating polymorphism
print("BMW Details:")
car_details(bmw_car)

print("\nFerrari Details:")
car_details(ferrari_car)