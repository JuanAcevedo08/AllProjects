class Vehicle:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.availability = True

    def purchase(self):
        if self.availability:
            self.availability = False
            print(f"Your vehicle {self.model} was successfully purchased for {self.price}.")
        else:
            print(f"{self.model} is not available at the moment.")

    def sell(self):
        self.availability = True
        print(f"Your {self.model} from the brand {self.brand} has been sold for {self.price}.")

class User:
    def __init__(self, name):
        self.name = name
        self.purchased = []
        self.sold = []

    def buy(self, vehicle):
        if vehicle.availability:
            vehicle.purchase()
            self.purchased.append(vehicle)

    def sell_vehicle(self, vehicle):
        vehicle.sell()
        self.sold.append(vehicle)
        self.purchased.remove(vehicle)

    def show_user_cars(self):
        for car in self.purchased:
            print(f"{self.name}'s cars: {car.model}")
        for car in self.sold:
            print(f"{self.name}'s sold cars: {car.model}")

class Dealership:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print(f"Vehicle added to dealership: {vehicle.model}")

    def show_vehicles(self):
        for car in self.vehicles:
            if car.availability:
                print(f"Available cars: Brand: {car.brand}, Model: {car.model}, Price: {car.price}")
            else:
                print(f"Car {car.model} is not available, it has been sold, but more will arrive soon.")

# Cars
car1 = Vehicle("Nissan", "GTR-35 v10", "$20,000")
car2 = Vehicle("Lamborghini", "Revuelto V12", "$40,000")
car3 = Vehicle("Toyota", "Prado", "$15,000")
car4 = Vehicle("Ford", "Raptor", "$15,000")

# User
user1 = User("Juan")

# Dealership
dealership = Dealership()
dealership.add_vehicle(car1)
dealership.add_vehicle(car2)
dealership.show_vehicles()

# Test
user1.buy(car1)
user1.buy(car2)
dealership.show_vehicles()
user1.sell_vehicle(car1)
dealership.show_vehicles()
user1.show_user_cars()
dealership.add_vehicle(car3)
dealership.add_vehicle(car4)
dealership.show_vehicles()
